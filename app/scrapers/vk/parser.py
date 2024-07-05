import logging
import requests
import time
from typing import List, Dict

from playwright.sync_api import Page

from app.schemas.vk.api import VKResponseSchema, VKResponsePostSchema, VKResponseProfileSchema

logger = logging.getLogger(__name__)

VK_WALL_URL = 'https://api.vk.com/method/newsfeed.search'
VK_POST_URL = 'https://api.vk.com/method/wall.getById'
VK_API_VERSION = 5.199
CHUNK_SIZE = 50


def fetch_chunk_posts(vk_api_token: str, hashtag_name: str, start_from: str, period:dict[str, int] = None) -> VKResponseSchema:
    payload = {
        'access_token': vk_api_token,
        'v': VK_API_VERSION,
        'q': f'#{hashtag_name}',
        'count': CHUNK_SIZE,
        'start_from': start_from,
        'extended': 1,
    }
    if period:
        payload.update(period)

    response = requests.get(VK_WALL_URL, params=payload)
    response.raise_for_status()
    res = response.json()

    if 'error' in res:
        logger.error('VK API error: %s', res['error']['error_msg'])
        raise Exception(res['error']['error_msg'])

    return VKResponseSchema(**res['response'])


def fetch_posts_for_update(vk_api_token: str, posts: List[Dict[str, int]]) -> VKResponseSchema:
    payload = {
        'access_token': vk_api_token,
        'v': VK_API_VERSION,
        'posts': ','.join([f"{post['owner_id']}_{post['post_id']}" for post in posts]),
    }

    response = requests.get(VK_POST_URL, params=payload)
    response.raise_for_status()
    res = response.json()

    if 'error' in res:
        logger.error('VK API error: %s', res['error']['error_msg'])
        raise Exception(res['error']['error_msg'])

    return VKResponseSchema(**res['response'])


def has_video(post: VKResponsePostSchema) -> bool:
    for attachment in post.attachments:
        if attachment.type == 'video':
            return True
    return False


def get_posts_profiles_with_video(vk_api_token: str, hashtag_name: str, period:dict[str, int] = None) -> (List[VKResponsePostSchema], List[VKResponseProfileSchema]):
    all_posts = []
    all_profiles = []
    start_from = ''
    while True:
        chunk_posts = fetch_chunk_posts(vk_api_token, hashtag_name, start_from, period)
        all_posts += list(filter(has_video, chunk_posts.items))
        all_profiles += chunk_posts.profiles

        if chunk_posts.next_from is None:
            break
        start_from = chunk_posts.next_from
        time.sleep(1)
    return all_posts, all_profiles


def fetch_clips_params(page: Page, clips_hashtag_link:str) -> List[tuple]:
    page.goto(clips_hashtag_link)

    count_links = 0
    while True:
        time.sleep(1)
        page.keyboard.down('End')
        page.wait_for_selector('div.ShortVideoGrid__list')
        links = page.query_selector_all('div.ShortVideoGrid__list a')
        if len(links) == count_links:
            break
        count_links = len(links)

    clips_params = []
    for clip_link in links:
        link_uri = clip_link.get_attribute('href')[1:]
        clips_params.append(tuple(map(int, link_uri.strip('clip').split('_'))))

    return clips_params


def fetch_clip_page(page: Page, clip_params: tuple, clips_hashtag_link: str) -> Page:
    author_id, clip_id = clip_params
    full_clip_link = f'{clips_hashtag_link}?z=clip{author_id}_{clip_id}'

    try:
        page.goto(full_clip_link)
        page.wait_for_selector('#mv_views')
    except Exception as e:
        print("ERROR WITH", full_clip_link)
        raise e
    return page
