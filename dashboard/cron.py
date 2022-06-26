import datetime
from .api import get_latest_videos
from .models import VideoModel


def update_videos():
    """Corn job function which will run after every 5 minute and do the following task
    1. get the new video data form api
    2. add new videos in modal
    3. display the total new video added in log file
    """

    res = get_latest_videos()
    if not res:
        return

    videos = res["items"]
    count_of_videos = 0

    for i in range(len(videos)):

        video = videos[i]
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
            count_of_videos += 1
        except Exception as e:
            # if video found the same pass
            # print(e)
            pass

    print(f"Added {count_of_videos} videos at {datetime.datetime.now()}")
