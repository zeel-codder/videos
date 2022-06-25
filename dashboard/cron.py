import datetime
from .api import get_latest_videos
from .models import VideoModel


def update_videos():
    res = get_latest_videos()
    videos_list = res["items"]
    count_videos = 0
    for i in range(len(videos_list)):
        video = videos_list[i]
        snippet = video["snippet"]
        video_id = video["id"]["videoId"]
        title = snippet["title"]
        description = snippet["description"]
        thumbnail = snippet["thumbnails"]["high"]["url"]
        channel_title = snippet["channelTitle"]
        publish_time = snippet["publishTime"]
        try:
            video_to_add = VideoModel(
                video_id=video_id,
                title=title,
                description=description,
                thumbnail=thumbnail,
                channel_title=channel_title,
                publish_time=publish_time,
            )
            video_to_add.save()
            count_videos += 1
        except Exception as e:
            print(e)
            break

    print(f"Added {count_videos} videos at {datetime.datetime.now()}")
