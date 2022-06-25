# API client library
from googleapiclient.discovery import build
from django.conf import settings
import requests
from googleapiclient.errors import HttpError
from .models import KeyModel


def get_youtube_client():
    """
    Returns:
        _object_: Used to make request for get the data form api
    """
    # API information
    api_service_name = "youtube"
    api_version = "v3"
    yt_api_key_index = KeyModel.objects.get(type="YT").index
    DEVELOPER_KEY = settings.YT_API_KEYS[yt_api_key_index]
    # API client
    youtube = build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
    return youtube


def get_latest_videos(query="football", type="video", maxResults=50, order="date"):
    """Return the latest video of give query
    Args:
        query (str, optional): _Category of item. Defaults to "football".
        type (str, optional): _Response item type_. Defaults to "video".
        maxResults (int, optional): _description_. Defaults to 50.
        order (int, optional): _description_. Defaults to 50.
    Returns:
        _Object_: _List of videos_
    """

    try:
        part = "snippet"
        # base IST 2022-06-24-21:00:00
        publishedAfter = "2022-06-24T15:30:00Z"
        youtube = get_youtube_client()
        request = youtube.search().list(
            part=part,
            order=order,
            publishedAfter=publishedAfter,
            q=query,
            type=type,
            maxResults=maxResults,
        )
        response = request.execute()
        return response
    except HttpError as e:
        # if status code is 403 than change the api key index for next call
        if e.status_code == 403:
            print("Change Api-Key")
            size = len(settings.YT_API_KEYS)
            yt_api_key_index = KeyModel.objects.get(type="YT")
            yt_api_key_index.index = (yt_api_key_index.index + 1) % size
            yt_api_key_index.save()
        return False
