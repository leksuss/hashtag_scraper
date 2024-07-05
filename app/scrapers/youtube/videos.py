import logging
import time

from app.scrapers.youtube import parser as yt_scraper
from app.processors import youtube as yt_processor
from app.services import service as db_service


logger = logging.getLogger(__name__)

def get_youtube_videos(campaign_id: int) -> None:

    logger.info('Youtube hashtag scraper started')

    count_total = 0
    for hashtag in db_service.get_hashtags_by(campaign_id):
        try:
            videos = yt_scraper.fetch_videos(hashtag)
        except Exception as e:
            print(e)
            logger.error(f'Failed to get videos with {hashtag.name}')
            continue

        logger.info(f'Found {len(videos)} videos')

        count_added_with_hashtag = 0
        for video in videos:
            video_prepared_for_db = yt_processor.prepare_video_for_db(video, hashtag)
            is_created = db_service.create_or_update_resource(video_prepared_for_db)
            if is_created:
                count_added_with_hashtag += 1


        # обновляем просмотры и лайки в старых публикациях
        # received_posts_for_update = vk_scraper.fetch_posts_for_update(env('VK_API_TOKEN'), posts_for_update)

        count_total += count_added_with_hashtag
        logger.info(f'Added {count_added_with_hashtag} videos with hashtag {hashtag.name}')
        time.sleep(5)

    logger.info(f'Total added {count_total} videos')
    logger.info('Youtube hashtag scraper finished')


get_youtube_videos(1)