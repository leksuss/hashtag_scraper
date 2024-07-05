from typing import List

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import insert

from app.storage.db_connection import session as db
from app.storage.models import Post, Hashtag
from app.schemas.common import SocialNetworksEnum


def get_updated_links_by(sn: SocialNetworksEnum, type: str) -> List[str]:
    query = sa.select(
        Post.author_vk_id,
        Post.resource_vk_id
    ).where(
        Post.social_network == sn,
        Post.type == type,
        sa.cast(Post.updated_at, sa.Date) == sa.cast(sa.func.current_date(), sa.Date),
    )
    return db.execute(query).all()


def create_or_update_post(post: dict) -> None:
    stmt = insert(Post).values(**post)
    update_condition = sa.cast(Post.updated_at, sa.Date) < sa.cast(sa.func.current_date(), sa.Date)
    upsert_stmt = stmt.on_conflict_do_update(
        index_elements=['author_vk_id', 'resource_vk_id', 'type'],
        where=update_condition,
        set_={
            'views': post['views'],
            'likes': post['likes'],
            'updated_at': sa.func.now(),
        },
    )

    db.execute(upsert_stmt)
    db.commit()


def get_hashtags_by(campaign) -> List[Hashtag]:
    query = sa.select(Hashtag).where(Hashtag.campaign_id == campaign)
    return db.execute(query).scalars().all()


if __name__ == '__main__':
    from app.scrapers.vk import prepare_post_for_db, get_posts_with_video
    from app.config import settings
    from app.storage.db_connection import session
    from datetime import datetime
    import zoneinfo

    from app.schemas.common import SocialNetworksEnum

    hashtag = get_hashtags_by(1)[0]
    # post = get_posts_with_video(settings.VK_API_TOKEN, hashtag.name)[0][2]
    # post = prepare_post_for_db(post, hashtag)
    post_for_db = {
        'social_network': SocialNetworksEnum.VK,
        'date_published': datetime(2024, 7, 2, 13, 36, 36, tzinfo=zoneinfo.ZoneInfo(key='Europe/Moscow')),
        'type': 'wall',
        'views': 1,
        'likes': 0,
        'author_vk_id': 580791178,
        'resource_vk_id': 1933,
        'hashtag_id': 2
    }

    links = get_updated_links_by(SocialNetworksEnum.VK, 'clip')
    print(len(links))

    # create_or_update_post(post_for_db)


