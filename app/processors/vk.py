from datetime import datetime

import dateparser
from playwright.sync_api import Page

from app.schemas.vk.api import VKResponsePostSchema
from app.schemas.common import SocialNetworksEnum
from app.config import settings


def prepare_post_for_db(post: VKResponsePostSchema, hashtag) -> dict:
    post_for_db = {
        'social_network': SocialNetworksEnum.VK,
        'date_published': datetime.fromtimestamp(post.date, settings.TIMEZONE),
        'type': 'wall',
        'views': post.attachments[0].video.views,
        'likes': post.likes['count'],
        'author_id': post.from_id,
        'resource_id': post.id,
        'hashtag_id': hashtag.id,
    }
    return post_for_db


def prepare_clip_for_db(page:Page, hashtag) -> dict:
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
        'author_id': int(author_vk_id),
        'resource_id': int(resource_vk_id),
        'hashtag_id': hashtag.id,
    }
    return clip_for_db
