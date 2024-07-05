from datetime import datetime
import logging
import requests
import time
from typing import List, Dict
import urllib.parse

import dateparser

from app.schemas.vk import VKResponse, VKResponsePost, VKResponseProfile
from app.schemas.common import SocialNetworksEnum, Post, HashtagSchema
from app.config import settings

logger = logging.getLogger(__name__)

VK_WALL_URL = 'https://api.vk.com/method/newsfeed.search'
VK_POST_URL = 'https://api.vk.com/method/wall.getById'
VK_API_VERSION = 5.199
CHUNK_SIZE = 50


def fetch_chunk_posts(vk_api_token: str, hashtag_name: str, start_from: str, period:dict[str, int] = None) -> VKResponse:
    vk_wall_url = 'https://api.vk.com/method/newsfeed.search'
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

    response = requests.get(vk_wall_url, params=payload)
    response.raise_for_status()
    res = response.json()

    if 'error' in res:
        logger.error('VK API error: %s', res['error']['error_msg'])
        raise Exception(res['error']['error_msg'])
    vk_response_items = VKResponse(**res['response'])
    return vk_response_items


def fetch_posts_for_update(vk_api_token: str, posts: List[Dict[str, int]]) -> VKResponse:
    vk_post_url = 'https://api.vk.com/method/wall.getById'

    payload = {
        'access_token': vk_api_token,
        'v': VK_API_VERSION,
        'posts': ','.join([f"{post['owner_id']}_{post['post_id']}" for post in posts]),
    }

    response = requests.get(vk_post_url, params=payload)
    response.raise_for_status()
    res = response.json()

    if 'error' in res:
        logger.error('VK API error: %s', res['error']['error_msg'])
        raise Exception(res['error']['error_msg'])
    vk_response_items = VKResponse(**res['response'])
    return vk_response_items


def has_video(post: VKResponsePost) -> bool:
    for attachment in post.attachments:
        if attachment.type == 'video':
            return True
    return False


def prepare_post_for_db(post: VKResponsePost, hashtag) -> dict:
    post_for_db = {
        'social_network': SocialNetworksEnum.VK,
        'date_published': datetime.fromtimestamp(post.date, settings.TIMEZONE),
        'type': 'wall',
        'views': post.attachments[0].video.views,
        'likes': post.likes['count'],
        'author_vk_id': post.from_id,
        'resource_vk_id': post.id,
        'hashtag_id': hashtag.id,
    }
    return post_for_db


def prepare_clip_for_db(page, hashtag) -> dict:
    views_text = page.query_selector('#mv_views').inner_text().strip()
    views_text = views_text.replace('\xa0', ' ').replace('&nbsp;', ' ')
    if 'тыс' in views_text:
        views = int(float(views_text.split()[0].replace(',', '.')) * 1000)
    else:
        views = int(views_text.split()[0])

    human_date_string = page.query_selector('.VerticalVideoLayerInfo__date').inner_text()
    date = dateparser.parse(human_date_string, languages=['ru'])

    author_vk_id, resource_vk_id = page.url.split('z=clip')[1].split('_')

    clip_for_db = {
        'social_network': SocialNetworksEnum.VK,
        'date_published': date,
        'type': 'clip',
        'views': views,
        'likes': int(page.query_selector('.like_button_count').inner_text().strip().replace(' ', '') or 0),
        'author_vk_id': int(author_vk_id),
        'resource_vk_id': int(resource_vk_id),
        'hashtag_id': hashtag.id,
    }
    return clip_for_db


def get_posts_with_video(vk_api_token: str, hashtag_name: str, period:dict[str, int] = None) -> (List[VKResponsePost], List[VKResponseProfile]):
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


if __name__ == '__main__':
    post = get_posts_with_video(settings.VK_API_TOKEN, '#ozonхочумиллион')
    print(len(post[0]))
