from typing import List

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql import literal_column

from app.storage.db_connection import session as db
from app.storage.models import Post, Hashtag
from app.schemas.common import SocialNetworksEnum


def get_updated_links_by(sn: SocialNetworksEnum, type: str) -> List[str]:
    query = sa.select(
        Post.author_id,
        Post.resource_id
    ).where(
        Post.social_network == sn,
        Post.type == type,
        sa.cast(Post.updated_at, sa.Date) == sa.cast(sa.func.current_date(), sa.Date),
    )
    return db.execute(query).all()


def create_or_update_post(post: dict) -> bool | None:
    stmt = insert(Post).values(**post)
    update_condition = sa.cast(Post.updated_at, sa.Date) < sa.cast(sa.func.current_date(), sa.Date)
    upsert_stmt = stmt.on_conflict_do_update(  # Postgres only
        index_elements=['author_id', 'resource_id', 'type'],
        where=update_condition,
        set_={
            'views': post['views'],
            'likes': post['likes'],
            'updated_at': sa.func.now(),
        },
    ).returning(Post.id, literal_column("(xmax = 0) AS inserted"))  # Postgres only

    result  = db.execute(upsert_stmt)
    db.commit()

    return result.one_or_none()

def get_hashtags_by(campaign) -> List[Hashtag]:
    query = sa.select(Hashtag).where(Hashtag.campaign_id == campaign)
    return db.execute(query).scalars().all()


if __name__ == '__main__':
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
        'author_id': 580791178,
        'resource_id': 1933,
        'hashtag_id': 2
    }

#    links = get_updated_links_by(SocialNetworksEnum.VK, 'clip')
#    print(len(links))

    create_or_update_post(post_for_db)


