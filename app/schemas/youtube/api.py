from pydantic import BaseModel
from typing import List, Dict

class YouTubeResponseChannelSchema(BaseModel):
    name: str
    id: str


class YouTubeResponseVideoSchema(BaseModel):
    id: str
    viewCount: Dict
    publishedTime: str
    channel: YouTubeResponseChannelSchema


class YouTubeResponseSchema(BaseModel):
    result: List[YouTubeResponseVideoSchema]
