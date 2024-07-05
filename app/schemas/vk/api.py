from pydantic import BaseModel
from typing import List, Dict, Optional


class VKResponseVideoSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    content_restricted: Optional[int] = 0
    views: Optional[int] = 0


class VKResponseAttachmentsSchema(BaseModel):
    type: str
    video: Optional[VKResponseVideoSchema] = None
    views: Optional[int] = 0


class VKResponsePostSchema(BaseModel):
    attachments: List[VKResponseAttachmentsSchema]
    date: int
    from_id: int
    id: int
    text: str
    views: Dict
    likes: Dict


class VKResponseProfileSchema(BaseModel):
    id: int
    screen_name: str


class VKResponseSchema(BaseModel):
    count: int
    next_from: Optional[str] = None
    items: List[VKResponsePostSchema]
    profiles: List[VKResponseProfileSchema]


if __name__ == '__main__':

    json_string = {
        "response": {
            "count": 204,
            "items": [
                {
                    "inner_type": "wall_wallpost",
                    "donut": {
                        "is_donut": False
                    },
                    "comments": {
                        "count": 0
                    },
                    "marked_as_ads": 0,
                    "short_text_rate": 0.8,
                    "has_translation": False,
                    "type": "post",
                    "donut_miniapp_url": "https://vk.com/app51528700#/?owner_id=-131011375&type=donut_badges&params=%257B%2522item_id%2522%253A%2522688%2522%257D&comment=1",
                    "attachments": [
                        {
                            "type": "video",
                            "video": {
                                "response_type": "full",
                                "access_key": "28c5d2d4ea8f6c67b1",
                                "can_comment": 1,
                                "can_like": 1,
                                "can_repost": 1,
                                "can_subscribe": 1,
                                "can_add_to_faves": 1,
                                "can_add": 1,
                                "comments": 0,
                                "date": 1706164223,
                                "description": "Статья о поездке в Шоанинский храм на моем сайте: https://33ways.ru/rossija/shoaninskiy-khram/",
                                "duration": 126,
                                "image": [
                                    {
                                        "url": "https://sun9-49.userapi.com/gxjG5n91HC_FiiXsz__u14dxlS6DFLH4Z9i7bA/5tIet7iBQ4Q.jpg",
                                        "width": 130,
                                        "height": 96,
                                        "with_padding": 1
                                    },
                                    {
                                        "url": "https://sun9-43.userapi.com/aaKoxSrf4WI068lbkND28E9tymgDwZHEgKnMAw/A5GY14NXipU.jpg",
                                        "width": 160,
                                        "height": 120,
                                        "with_padding": 1
                                    },
                                    {
                                        "url": "https://sun9-49.userapi.com/kQrqDsXbugndMz5o_94ytToAZdsi5v3fXIaUng/w2xtiK8CmWQ.jpg",
                                        "width": 320,
                                        "height": 240,
                                        "with_padding": 1
                                    },
                                    {
                                        "url": "https://sun9-5.userapi.com/lZFNdr9vc6BwCbwo43UotujsmrOj6vQyAmGEbQ/N5761ayFrXI.jpg",
                                        "width": 800,
                                        "height": 450,
                                        "with_padding": 1
                                    },
                                    {
                                        "url": "https://sun9-49.userapi.com/Ai1mX3iowqaN8alBZEueMCck7VXzIzjzwiIoEQ/K4Cmg3cKLa8.jpg",
                                        "width": 1280,
                                        "height": 719
                                    },
                                    {
                                        "url": "https://sun9-20.userapi.com/YALyMTVuBb2ytYIasc00fM-KENIOxxeGYs26bQ/g3XmKNk-NrY.jpg",
                                        "width": 320,
                                        "height": 180
                                    },
                                    {
                                        "url": "https://sun9-54.userapi.com/zxF0CQDcqpFpMOEczpaXhb7awlIRWH9rWV5fzQ/mV8nw-XtdAk.jpg",
                                        "width": 720,
                                        "height": 405
                                    },
                                    {
                                        "url": "https://sun9-21.userapi.com/kqHr9VbBt9VcwwAtGtTKChG70VWi4v9iVZOPsw/fMWdaNxVzRY.jpg",
                                        "width": 1024,
                                        "height": 575
                                    },
                                    {
                                        "url": "https://sun9-63.userapi.com/iJApH-mFUUdv5u1N6rPK-FseP3cA79LH37EDUg/ITpA0FZcMHc.jpg",
                                        "width": 4096,
                                        "height": 2302
                                    }
                                ],
                                "first_frame": [
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_f",
                                        "width": 720,
                                        "height": 405
                                    },
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_md",
                                        "width": 480,
                                        "height": 270
                                    },
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_d",
                                        "width": 240,
                                        "height": 135
                                    },
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_sm",
                                        "width": 128,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_w",
                                        "width": 1280,
                                        "height": 720
                                    },
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_h",
                                        "width": 960,
                                        "height": 540
                                    },
                                    {
                                        "url": "https://i.mycdn.me/getVideoPreview?id=5811400542779&idx=0&type=39&tkn=gQ73SlU0Oq-1mk2vAfUW0KsPU6k&fn=vid_w",
                                        "width": 1280,
                                        "height": 720
                                    }
                                ],
                                "width": 3840,
                                "height": 2160,
                                "id": 456239379,
                                "owner_id": -131011375,
                                "title": "Шоанинский православный храм в Карачаево-Черкесии - один из древнейших в РФ",
                                "is_favorite": False,
                                "track_code": "video_8f61d4efq5PxRtD-jO6OClDJXwiPHu5vkd49621whXQrnp-h86GFtu9G0_6N7IgMOMo4BLoo3Fyo7QrSagXruPsDbQ1pURLc3Hfjz7zfvzln_P_DRdcjo1cS9dM",
                                "type": "video",
                                "views": 36,
                                "local_views": 36,
                                "can_dislike": 1
                            }
                        }
                    ],
                    "date": 1706165288,
                    "edited": 1706264562,
                    "from_id": -131011375,
                    "id": 688,
                    "is_favorite": False,
                    "likes": {
                        "can_like": 0,
                        "count": 2,
                        "user_likes": 0
                    },
                    "reaction_set_id": "reactions",
                    "reactions": {
                        "count": 2,
                        "items": [
                            {
                                "id": 0,
                                "count": 2
                            }
                        ]
                    },
                    "owner_id": -131011375,
                    "post_type": "post",
                    "reposts": {
                        "count": 0
                    },
                    "text": "Шоанинский православный храм в Карачаево-Черкесии - один из древнейших в РФ.\n#vkвышегор",
                    "views": {
                        "count": 41
                    }
                }
            ],
            "profiles": [],
            "groups": [
                {
                    "id": 131011375,
                    "name": "33WAYS.ru - БЛОГ О ПУТЕШЕСТВИЯХ",
                    "screen_name": "33waysru",
                    "is_closed": 0,
                    "type": "group",
                    "photo_50": "https://sun9-76.userapi.com/s/v1/ig2/Y_cXkk9ZtgOdkFZ-Y7mBLX8irrQxDLQbhzmsBSFGOi2_Aar5wbWLyPrpWTA4Z2mgCiMN1wrhoBv4Tbp-kSKE3kjB.jpg?size=50x50&quality=95&crop=0,0,400,400&ava=1",
                    "photo_100": "https://sun9-76.userapi.com/s/v1/ig2/5rPpZgIjtUzKklL4mAALkz-IIP8v80UbfJOuLQdSwxxDAjp6TSmjBSOz2rm8COdnnIvTeq6An32G0n2ZJ759bO4o.jpg?size=100x100&quality=95&crop=0,0,400,400&ava=1",
                    "photo_200": "https://sun9-76.userapi.com/s/v1/ig2/Dei01tXIvDVT6tde5M2VY1aS27L-f6Kn7GyjNhGuVY2v-FK9jWaE2uvswjUgo_HTI1iXp-c6TAzcDs7hRl-C3eZZ.jpg?size=200x200&quality=95&crop=0,0,400,400&ava=1"
                }
            ],
            "reaction_sets": [
                {
                    "id": "reactions",
                    "items": [
                        {
                            "id": 0,
                            "title": "Нравится",
                            "asset": {
                                "animation_url": "https://vk.com/reaction/3-reactions-0?c_uniq_tag=83b2081a8e4adfc36ee536f5f1b4ad470174c89678369a4b9dc5547614a3955e",
                                "images": [
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-0-32?c_uniq_tag=464ba6bdc06e9f204a9b2c865a046355d835f601d8d82be4dc77e43a028741ff",
                                        "width": 32,
                                        "height": 32
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-0-48?c_uniq_tag=e6bee176471af6e4f7ca0f57ac099847d57b8101bf07944e47b42b097a6d8455",
                                        "width": 48,
                                        "height": 48
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-0-72?c_uniq_tag=d6f55fe94c0add8f817b447cbd804768752eb996c06ef222b39eb3fd35834780",
                                        "width": 72,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-0-96?c_uniq_tag=0a64c3d34d3a1368b05716ff24f94ff51b2257a2287957423ced36a00b020cb6",
                                        "width": 96,
                                        "height": 96
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-0-144?c_uniq_tag=47a911186fd9ce6d9aba1f9273e49ef70d1e0149e7470d1dae40941d81a1ece4",
                                        "width": 144,
                                        "height": 144
                                    }
                                ],
                                "title": {
                                    "color": {
                                        "foreground": {
                                            "light": "FF3347",
                                            "dark": "FF5C5C"
                                        },
                                        "background": {
                                            "light": "FFEDED",
                                            "dark": "3E2526"
                                        }
                                    }
                                },
                                "title_color": {
                                    "light": "FF3347",
                                    "dark": "FF5C5C"
                                }
                            }
                        },
                        {
                            "id": 1,
                            "title": "Смешно",
                            "asset": {
                                "animation_url": "https://vk.com/reaction/3-reactions-1?c_uniq_tag=a47193579880c0f53dd597a15d3bd57d4827820687c73d6128df2720647b42b9",
                                "images": [
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-1-32?c_uniq_tag=2119d7ea78675f5702dcf43035f5f7fe13d6dd0f444b3a7d1735699d659b49b7",
                                        "width": 32,
                                        "height": 32
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-1-48?c_uniq_tag=8f5eb3a1d6a6ec81aceff211782af3c9e9a5d1c837f0bfade6965a6844786f8b",
                                        "width": 48,
                                        "height": 48
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-1-72?c_uniq_tag=c852fcad6e67059878dcf1905e3e416fd89fbc61222ead100935a6fcc1dab4c9",
                                        "width": 72,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-1-96?c_uniq_tag=647ccf722698732a8b13033eadd1f02c5c917b0bdc3f9fb16d6cd0ade8706c99",
                                        "width": 96,
                                        "height": 96
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-1-144?c_uniq_tag=68c571ccb2f08b9e0404e5307b41a48a057454b44375480a7a89f1dc8fb8b521",
                                        "width": 144,
                                        "height": 144
                                    }
                                ],
                                "title": {
                                    "color": {
                                        "foreground": {
                                            "light": "FF8000",
                                            "dark": "FFC233"
                                        },
                                        "background": {
                                            "light": "FFF2D6",
                                            "dark": "352E23"
                                        }
                                    }
                                },
                                "title_color": {
                                    "light": "FF8000",
                                    "dark": "FFC233"
                                }
                            }
                        },
                        {
                            "id": 2,
                            "title": "Ого!",
                            "asset": {
                                "animation_url": "https://vk.com/reaction/3-reactions-2?c_uniq_tag=b946fcbe262642bc920331746b6eccd9f175bb17d8ef37e54d232fa35ca2c750",
                                "images": [
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-2-32?c_uniq_tag=e919477a3e650ebae5d810b30dcc7529a52b072f2470327f95220b778abfb449",
                                        "width": 32,
                                        "height": 32
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-2-48?c_uniq_tag=2a6544dce8827d216db7ea91eafc726cd3a823f5d465ba00216901a6de2801ad",
                                        "width": 48,
                                        "height": 48
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-2-72?c_uniq_tag=5a0663f3d38dd6fbcf3e4973610d50641420631c9df30b6cf80eee0dd5c5efee",
                                        "width": 72,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-2-96?c_uniq_tag=51275507a335aeafd7c43735d92d11a6b3acf2bb5595273a44a4f844c055b2ce",
                                        "width": 96,
                                        "height": 96
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-2-144?c_uniq_tag=223a080cabb1e69212b9b1cdb455dcfb8bcbbdc40d93ae339717ecd32ea95f4c",
                                        "width": 144,
                                        "height": 144
                                    }
                                ],
                                "title": {
                                    "color": {
                                        "foreground": {
                                            "light": "FF8000",
                                            "dark": "FFC233"
                                        },
                                        "background": {
                                            "light": "FFF2D6",
                                            "dark": "352E23"
                                        }
                                    }
                                },
                                "title_color": {
                                    "light": "FF8000",
                                    "dark": "FFC233"
                                }
                            }
                        },
                        {
                            "id": 3,
                            "title": "Восторг",
                            "asset": {
                                "animation_url": "https://vk.com/reaction/3-reactions-3?c_uniq_tag=c6ed3add99e841dccda5479c8e21779954e61e0fba15f94a2ae16706df492123",
                                "images": [
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-3-32?c_uniq_tag=a95fe4eb836477892e54dcd8f464598e49a611249ec93d5eb7d7a1401cb77cff",
                                        "width": 32,
                                        "height": 32
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-3-48?c_uniq_tag=eda1a2c18d733b356babdeed5f52cdcc64dd59f1f69776a133fc34a5627eecee",
                                        "width": 48,
                                        "height": 48
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-3-72?c_uniq_tag=be09c5080773a9ba78984406588c7371e48073e80b842eb7c9a817f7b435379b",
                                        "width": 72,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-3-96?c_uniq_tag=b08f5ff31b4bd18e465f14262708e4aac56d34f343b8d355171df7d73bb34497",
                                        "width": 96,
                                        "height": 96
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-3-144?c_uniq_tag=484984c408a4b1f82d51229ce061ccbc5ad2efffbf2b684636ecfaa60f567f89",
                                        "width": 144,
                                        "height": 144
                                    }
                                ],
                                "title": {
                                    "color": {
                                        "foreground": {
                                            "light": "FF8000",
                                            "dark": "FFC233"
                                        },
                                        "background": {
                                            "light": "FFF2D6",
                                            "dark": "352E23"
                                        }
                                    }
                                },
                                "title_color": {
                                    "light": "FF8000",
                                    "dark": "FFC233"
                                }
                            }
                        },
                        {
                            "id": 5,
                            "title": "Печаль",
                            "asset": {
                                "animation_url": "https://vk.com/reaction/3-reactions-5?c_uniq_tag=c61122c8c334154cb10ccf0e0687057bf1f0f40c2817198b2e1150df534c22c4",
                                "images": [
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-5-32?c_uniq_tag=a07ac888553814f1cbc8c9342b636bf30ca6d80d14e7e38170ea02dad0bfafbf",
                                        "width": 32,
                                        "height": 32
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-5-48?c_uniq_tag=31bcb230babad96120a62589c52af22811aaba54d4ed73a36cfd499d9d94102f",
                                        "width": 48,
                                        "height": 48
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-5-72?c_uniq_tag=a840d0eb581c133d97638ff5bf34f4b33f3fb8557b932cfe3516925b88e2f151",
                                        "width": 72,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-5-96?c_uniq_tag=8cff3bac94202cbb5bee1d598f113134e0038804a3837be750f28ff27d3ffb05",
                                        "width": 96,
                                        "height": 96
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-5-144?c_uniq_tag=8bf31a92656dd0c0d3482505bf1b6fb3d2493a3e4c93e0e62723aef81c7da052",
                                        "width": 144,
                                        "height": 144
                                    }
                                ],
                                "title": {
                                    "color": {
                                        "foreground": {
                                            "light": "4986CC",
                                            "dark": "71AAEB"
                                        },
                                        "background": {
                                            "light": "EDF3FA",
                                            "dark": "27303C"
                                        }
                                    }
                                },
                                "title_color": {
                                    "light": "4986CC",
                                    "dark": "71AAEB"
                                }
                            }
                        },
                        {
                            "id": 4,
                            "title": "&$#%!",
                            "asset": {
                                "animation_url": "https://vk.com/reaction/3-reactions-4?c_uniq_tag=063e6b2dd888bb5a9716cf6153f03bf9c0c9707713b857eed8fe1e4e09aea2b3",
                                "images": [
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-4-32?c_uniq_tag=ac5ab70367285c3fbbee7ba2adde88cbb65db2d35e05b09b4ae5593ee0bcc535",
                                        "width": 32,
                                        "height": 32
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-4-48?c_uniq_tag=c80e3224c299a73384c057ff065c9458dcd533d57a1458875eb98883c3a96783",
                                        "width": 48,
                                        "height": 48
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-4-72?c_uniq_tag=a0eddba1ec31f96adbb9afa2c6c14bec055b95f8d9f113bdf759fb5a9c9054f0",
                                        "width": 72,
                                        "height": 72
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-4-96?c_uniq_tag=5495709e616048fd43683ac693ebd09f3615c797af2493d0334402befded2885",
                                        "width": 96,
                                        "height": 96
                                    },
                                    {
                                        "url": "https://vk.com/reaction/1-reactions-4-144?c_uniq_tag=a79fce98e0d7769284290ab78936b3aa6d15a42caa50e6071bdeb5013d950251",
                                        "width": 144,
                                        "height": 144
                                    }
                                ],
                                "title": {
                                    "color": {
                                        "foreground": {
                                            "light": "EF5203",
                                            "dark": "FA5300"
                                        },
                                        "background": {
                                            "light": "FDEBE8",
                                            "dark": "3C2421"
                                        }
                                    }
                                },
                                "title_color": {
                                    "light": "EF5203",
                                    "dark": "FA5300"
                                }
                            }
                        }
                    ]
                }
            ],
            "next_from": "1/-131011375_688",
            "total_count": 204
        }
    }

    from app.scrapers.vk import prepare_post_for_db, get_posts_with_video
    from app.config import settings
    from app.services.service import get_hashtags_by

    from app.schemas.common import SocialNetworksEnum

    hashtag = get_hashtags_by(1)[0]

    print(type(hashtag), type(hashtag.name))
'''
    hashtag = get_hashtags_by(1)[0]
    post = get_posts_with_video(settings.VK_API_TOKEN, hashtag.name)[0]




    vk_response_items = VKResponse(**json_string['response'])

    print(vk_response_items.items[0].attachments[0].video.id)
    print(vk_response_items.items[0].views['count'])
    print(vk_response_items.items[0].likes['count'])

    video_url = f"https://vk.com/video{vk_response_items.items[0].from_id}_{vk_response_items.items[0].attachments[0].video.id}"
    print(video_url)
    post_url = f"https://vk.com/wall{vk_response_items.items[0].from_id}_{vk_response_items.items[0].id}"
    print(post_url)
'''


