from datetime import datetime
import pandas as pd

from app.storage.db_connection import session



query = '''
    SELECT
        p.social_network as "Социальная сеть", 
        p.type as "Тип публикации",
        CASE
            WHEN p.type = 'wall' THEN
                CONCAT('https://vk.com/wall', p.author_id, '_', p.resource_id)
            WHEN p.type = 'clip' THEN
                CONCAT('https://vk.com/clips/hashtag/', h.name, '?z=clip', p.author_id, '_', p.resource_id)
            WHEN p.type = 'video' THEN
                CONCAT('https://www.youtube.com/watch?v=', p.resource_id)
        END AS "ссылка на публикацию",
        p.date_published as "Дата публикации",
        p.views as "Просмотры",
        p.likes as "Лайки",
        CASE
            WHEN p.social_network = 'VK' THEN
                CASE
                    WHEN CAST(p.author_id AS INTEGER) < 0 THEN
                        CONCAT('https://vk.com/club', ABS(CAST(p.author_id AS INTEGER)))
                    ELSE
                        CONCAT('https://vk.com/id', CAST(p.author_id AS INTEGER))
                END
            WHEN p.social_network = 'YT' THEN
                CONCAT('https://www.youtube.com/channel/', p.author_id)
        END AS "Автор",
        h.name as "Хэштег"
    FROM post p
    LEFT JOIN hashtag h on h.id=p.hashtag_id
    WHERE p.date_published BETWEEN '2024-06-10' AND '2024-07-05'
    ORDER BY p.date_published;
'''


data_frame = pd.read_sql(query, session.connection())

datetime_str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

with pd.ExcelWriter(f'VK_posts_{datetime_str}.xlsx', engine="xlsxwriter") as writer:
    data_frame.to_excel(writer, index=False, sheet_name='processing')
