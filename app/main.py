from environs import Env
import logging

from log_handlers import TelegramLogsHandler
from services import vk as vk_service

logger = logging.getLogger(__name__)


def main():
    env = Env()
    env.read_env()

    if env('TG_LOGBOT_TOKEN', None) and env('TG_LOGBOT_CHAT_ID', None):
        handler = TelegramLogsHandler(env('TG_LOGBOT_TOKEN'), env('TG_LOGBOT_CHAT_ID'))
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    # logger.info('VK hashtag scraper started')
    all_posts = vk_service.get_all_posts(env('VK_API_TOKEN'), '#vkвышегор')
    print(len(all_posts))
    # logger.info('VK hashtag scraper finished')

if __name__ == '__main__':
    main()