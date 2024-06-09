import logging
import requests

from app.schemas.vk import VKResponse

logger = logging.getLogger(__name__)

VK_API_URL = 'https://api.vk.com/method/newsfeed.search'
VK_API_VERSION = 5.199


def fetch_chunk_posts(vk_api_token, query, start_from):
    payload = {
        'access_token': vk_api_token,
        'v': VK_API_VERSION,
        'q': query,
        'count': 100,
        'start_from': start_from,
    }

    response = requests.get(VK_API_URL, params=payload)
    response.raise_for_status()
    res = response.json()

    if 'error' in res:
        logger.error('VK API error: %s', res['error']['error_msg'])
        raise Exception(res['error']['error_msg'])

    vk_response_items = VKResponse(**res['response'])
    return vk_response_items


def has_video(post):
    for attachment in post.attachments:
        if attachment.type == 'video':
            return True
    return False


def get_all_posts(vk_api_token, query):
    all_posts = []
    start_from = ''
    while True:
        chunk_posts = fetch_chunk_posts(vk_api_token, query, start_from)
        all_posts += list(filter(has_video, chunk_posts.items))

        if chunk_posts.next_from is None:
            break
        start_from = chunk_posts.next_from

    return all_posts
