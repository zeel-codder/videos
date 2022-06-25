import json
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import VideoModel
from django.core.paginator import Paginator
from django.conf import settings
from .cron import update_videos

# Create your views here.
def home(request):
    return render(request, "dashboard/home.html")


def video_list(request, page, per_page_items):
    if request.method == "GET":
        if per_page_items < 0 or per_page_items > 50:
            return JsonResponse(
                status=400, data={"message": "per_page_items should be >0 and <=50"}
            )

        all_videos = VideoModel.objects.order_by("-publish_time")
        paginator = Paginator(all_videos, per_page_items)
        page_obj = paginator.get_page(page)
        data = list(page_obj.object_list.values())
        payload = {
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
            "data": data,
        }
        return JsonResponse(payload)
