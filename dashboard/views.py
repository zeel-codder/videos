import json
from django.http import HttpResponse
from django.shortcuts import render
from .api import get_latest_videos

# Create your views here.
def test(request):
    return HttpResponse(json.dumps(get_latest_videos()), content_type="application/json")
    