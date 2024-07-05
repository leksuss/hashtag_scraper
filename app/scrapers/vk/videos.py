from datetime import datetime
import logging
import time

from environs import Env

from app.log_handlers import TelegramLogsHandler
from app.scrapers.vk import parser as vk_scraper
from app.processors import vk as vk_processor
from app.services import service as db_service


logger = logging.getLogger(__name__)

def get_vk_videos(campaign_id: int, start_date: str, end_date: str=None) -> None:

    env = Env()
    env.read_env()

    if env('TG_LOGBOT_TOKEN', None) and env('TG_LOGBOT_CHAT_ID', None):
        handler = TelegramLogsHandler(env('TG_LOGBOT_TOKEN'), env('TG_LOGBOT_CHAT_ID'))
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    start_date_obj = datetime.strptime(start_date, '%d.%m.%Y')
    start_time_stamp = int(time.mktime(start_date_obj.timetuple()))

    if end_date:
        end_date_obj = datetime.strptime(start_date, '%d.%m.%Y')
        end_time_stamp = int(time.mktime(end_date_obj.timetuple()))
    else:
        end_time_stamp = int(time.time())

    logger.info('VK hashtag scraper started')

    count_total = 0
    for hashtag in db_service.get_hashtags_by(campaign_id):
        try:
            posts, profiles = vk_scraper.get_posts_profiles_with_video(
                env('VK_API_TOKEN'),
                hashtag.name,
                period={
                    'start_time': start_time_stamp,
                    'end_time': end_time_stamp,
                }
            )
        except:
            logger.error(f'Failed to get posts with {hashtag}')
            continue

        logger.info(f'Found {len(posts)} posts')

        count_added_with_hashtag = 0
        # posts_for_update = []
        for post in posts:
            post_prepared_for_db = vk_processor.prepare_post_for_db(post, hashtag)
            is_created = db_service.create_or_update_resource(post_prepared_for_db)
            if is_created:
                count_added_with_hashtag += 1

        # обновляем просмотры и лайки в старых публикациях
        # received_posts_for_update = vk_scraper.fetch_posts_for_update(env('VK_API_TOKEN'), posts_for_update)

        count_total += count_added_with_hashtag
        logger.info(f'Added {count_added_with_hashtag} posts with hashtag {hashtag.name}')
        time.sleep(5)

    logger.info(f'Total added {count_total} posts')
    logger.info('VK hashtag scraper finished')

get_vk_videos(1, '10.06.2024')