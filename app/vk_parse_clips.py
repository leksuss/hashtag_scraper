import time
from playwright.sync_api import Playwright, sync_playwright

from app.scrapers import vk as vk_scraper
from app.services import service as db_service

from app.schemas.common import SocialNetworksEnum


COUNT_PRESS_DOWN = 20
CLIPS_URL = "https://vk.com/clips/hashtag/"
CAMPAIGN_ID = 1

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()
    page.goto("https://vk.com/")
    time.sleep(2)

    updated_links = set(db_service.get_updated_links_by(SocialNetworksEnum.VK, 'clip'))
    count_total = 0
    for hashtag in db_service.get_hashtags_by(CAMPAIGN_ID):
        clips_hashtag_link = CLIPS_URL + hashtag.name
        page.goto(clips_hashtag_link)
        count_links = 0
        for _ in range(COUNT_PRESS_DOWN):
            time.sleep(1)
            page.keyboard.down('End')
            page.wait_for_selector('div.ShortVideoGrid__list')
            links = page.query_selector_all('div.ShortVideoGrid__list a')
            if len(links) == count_links:
                break
            count_links = len(links)

        clip_links = [clip_link.get_attribute('href')[1:] for clip_link in links]

        count_added_with_hashtag = 0
        for clip_link in clip_links:
            author_id, clip_id = map(int, clip_link.strip('clip').split('_'))
            full_clip_link = f'{clips_hashtag_link}?z=clip{author_id}_{clip_id}'

            if (author_id, clip_id) in updated_links:
                continue

            try:
                page.goto(full_clip_link)
                page.wait_for_selector('#mv_views')
                clip_prepared_for_db = vk_scraper.prepare_clip_for_db(page, hashtag)
                db_service.create_or_update_post(clip_prepared_for_db)
                count_added_with_hashtag += 1
            except Exception as e:
                print("ERROR WITH", full_clip_link)
                raise e

            time.sleep(1)

        print(f'Added {count_added_with_hashtag} posts with hashtag {hashtag.name}')
        count_total += count_added_with_hashtag
        print(f'Added {count_added_with_hashtag} posts')
        time.sleep(3)
    print(f'Added {count_total} posts')

    context.close()
    browser.close()


def main():
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == '__main__':
    main()
