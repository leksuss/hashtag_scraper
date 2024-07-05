import enum
from datetime import date
from typing import List, Dict, Optional

from pydantic import BaseModel


class SocialNetworksEnum(enum.Enum):
    VK = 'vk'
    IG = 'ig'


class PostTypeEnum(enum.Enum):
    VK = 'videopost'
    IG = 'clip'


class Campaign(BaseModel):
    name: str

    class Config:
        from_attributes = True


class HashtagSchema(BaseModel):
    name: str
    campaign: Campaign

    class Config:
        from_attributes = True


class Post(BaseModel):
    social_network: SocialNetworksEnum
    link: str
    date_published: date
    views: int
    likes: int
    author: str
    hashtag: HashtagSchema

    class Config:
        from_attributes = True