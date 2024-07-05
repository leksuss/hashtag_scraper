import time
from playwright.sync_api import Playwright, sync_playwright

from app.scrapers.vk import parser as vk_scraper
from app.processors import vk as vk_processor
from app.services import service as db_service

from app.schemas.common import SocialNetworksEnum


CLIPS_URL = "https://vk.com/clips/hashtag/"

def run(playwright: Playwright, context_file: str, campaign_id: int) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=context_file)
    page = context.new_page()
    page.goto("https://vk.com/")
    time.sleep(2)

    updated_clips = set(db_service.get_updated_links_by(SocialNetworksEnum.VK, 'clip'))
    count_total = 0
    for hashtag in db_service.get_hashtags_by(campaign_id):
        clips_hashtag_link = CLIPS_URL + hashtag.name
        clips_params = vk_scraper.fetch_clips_params(page, clips_hashtag_link)

        count_added_with_hashtag = 0
        for clip_params in clips_params:
            if clip_params in updated_clips:
                continue
            clip_page = vk_scraper.fetch_clip_page(page, clip_params, clips_hashtag_link)
            clip_prepared_for_db = vk_processor.prepare_clip_for_db(clip_page, hashtag)
            db_service.create_or_update_post(clip_prepared_for_db)
            count_added_with_hashtag += 1
            time.sleep(1)

        print(f'Added {count_added_with_hashtag} posts with hashtag {hashtag.name}')
        count_total += count_added_with_hashtag
        print(f'Added {count_added_with_hashtag} posts')
        time.sleep(3)

    print(f'Added {count_total} posts')

    context.close()
    browser.close()


def get_vk_clips(campaign_id: int, context_file: str) -> None:
    with sync_playwright() as playwright:
        run(playwright, context_file, campaign_id)


# get_vk_clips(1, '../../../auth.json')