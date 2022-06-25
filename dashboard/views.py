import json
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from .api import get_latest_videos
from .models import VideoModel

# Create your views here.
def home(request):
    return HttpResponse("Home")


def test(request):
    videos = list(VideoModel.objects.all().values())
    return JsonResponse(videos, safe=False)
