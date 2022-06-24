# API client library
from googleapiclient.discovery import build

def get_youtube_client():
    """
    Returns:
        _object_: Used to make request for get the data form api
    """
    # API information
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDguaxTyVONqo0jMf3PyQ2f4klZvC0mhgM"
    # API client
    youtube = build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    return youtube; 


def get_latest_videos(query="football",type="video",maxResults=50,order="date"):
    """Return the latest video of give query 
    Args:
        query (str, optional): _Category of item. Defaults to "football".
        type (str, optional): _Response item type_. Defaults to "video".
        maxResults (int, optional): _description_. Defaults to 50.
        order (int, optional): _description_. Defaults to 50.
    Returns:
        _type_: _description_
    """
    
    part="snippet"
    #base IST 2022-06-24-21:00:00
    publishedAfter="2022-06-24T15:30:00Z";
        
    youtube=get_youtube_client()
    request = youtube.search().list(
            part=part,
            order=order,
            publishedAfter=publishedAfter,
            q=query,
            type=type,
            maxResults=maxResults
    )
    response = request.execute()
    return response;
