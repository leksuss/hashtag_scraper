from typing import List

import youtubesearchpython as ysp

from app.schemas.youtube import api as yt_api_schema


LIMIT_PER_REQUEST = 100

def fetch_videos(hashtag) -> List[yt_api_schema.YouTubeResponseVideoSchema]:
    hashtag_page = ysp.Hashtag(hashtag.name, limit=LIMIT_PER_REQUEST)
    videos = {}
    while True:
        chunk_videos = yt_api_schema.YouTubeResponseSchema(**hashtag_page.result())
        if not len(chunk_videos.result):
            break
        chunk_videos = {video.id: video for video in chunk_videos.result}
        videos.update(chunk_videos)
        hashtag_page.next()

    return list(videos.values())
