import dateparser

from app.schemas.youtube.api import YouTubeResponseVideoSchema
from app.schemas.common import SocialNetworksEnum


def prepare_video_for_db(video: YouTubeResponseVideoSchema, hashtag) -> dict:

    date = dateparser.parse(video.publishedTime, languages=['en'])
    views_str = video.viewCount['text'].split()[0].replace(',', '')
    views = int(views_str.isdigit()) and int(views_str)

    video_for_db = {
        'social_network': SocialNetworksEnum.YT,
        'date_published': date,
        'type': 'video',
        'views': views,
        'likes': None,
        'author_id': video.channel.id,
        'nickname': video.channel.name,
        'resource_id': video.id,
        'hashtag_id': hashtag.id,
    }
    return video_for_db


if __name__ == '__main__':
    d = {
        "type": "video",
        "id": "MPNqeRGDDVY",
        "title": "ЭТО ПРОСТО БОМБА😍 #cat #pets #funnycats #memes #funny #ozonхочумиллион",
        "publishedTime": "13 days ago",
        "duration": "0:36",
        "viewCount": {"text": "1,550,684 views", "short": "1.5M views"},
        "thumbnails": [
            {
                "url": "https://i.ytimg.com/vi/MPNqeRGDDVY/hqdefault.jpg?sqp=-oaymwE1CKgBEF5IVfKriqkDKAgBFQAAiEIYAHABwAEG8AEB-AG2CIACgA-KAgwIABABGH8gKChFMA8=&rs=AOn4CLDix1HOFD0KRLuvESCcBa_nREpSLg",
                "width": 168,
                "height": 94,
            },
            {
                "url": "https://i.ytimg.com/vi/MPNqeRGDDVY/hqdefault.jpg?sqp=-oaymwE1CMQBEG5IVfKriqkDKAgBFQAAiEIYAHABwAEG8AEB-AG2CIACgA-KAgwIABABGH8gKChFMA8=&rs=AOn4CLD-WjpLRN7yfdVqRybQAfbca61tIw",
                "width": 196,
                "height": 110,
            },
            {
                "url": "https://i.ytimg.com/vi/MPNqeRGDDVY/hqdefault.jpg?sqp=-oaymwE2CPYBEIoBSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBtgiAAoAPigIMCAAQARh_ICgoRTAP&rs=AOn4CLALH0ZYn5T7PDS6DKV3Ctfn69bGrg",
                "width": 246,
                "height": 138,
            },
            {
                "url": "https://i.ytimg.com/vi/MPNqeRGDDVY/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGABwAcABBvABAfgBtgiAAoAPigIMCAAQARh_ICgoRTAP&rs=AOn4CLANAqTa5bu-o52g9-T8OptBBt3bxg",
                "width": 336,
                "height": 188,
            },
        ],
        "richThumbnail": {
            "url": "https://i.ytimg.com/an_webp/MPNqeRGDDVY/mqdefault_6s.webp?du=3000&sqp=CMbGlbQG&rs=AOn4CLD-ukHlbc5-f4nOT-luZh77U60RDw",
            "width": 320,
            "height": 180,
        },
        "descriptionSnippet": None,
        "channel": {
            "name": "SOFIADELMONSTRO",
            "id": "UC5T9LVyv2x_kK5Auh6N8HpA",
            "thumbnails": [
                {
                    "url": "https://yt3.ggpht.com/AZbJvWFwz2c0UG_KwKsLSZcw0q5vz2HzJCZx90c22n2I6V3oqyBeYbpqGn8vEPcRRaZrQ0YOXw=s68-c-k-c0x00ffffff-no-rj",
                    "width": 68,
                    "height": 68,
                }
            ],
            "link": "https://www.youtube.com/channel/UC5T9LVyv2x_kK5Auh6N8HpA",
        },
        "accessibility": {
            "title": "ЭТО ПРОСТО БОМБА😍 #cat #pets #funnycats #memes #funny #ozonхочумиллион by SOFIADELMONSTRO 1,550,684 views 13 days ago 36 seconds - play Short",
            "duration": "36 seconds",
        },
        "link": "https://www.youtube.com/watch?v=MPNqeRGDDVY",
        "shelfTitle": None,
    }

    schema = YouTubeResponseVideoSchema(**d)
    print(prepare_video_for_db(schema, 'озонхочумиллион'))