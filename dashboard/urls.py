from django.urls import path
from .views import video_list, home


urlpatterns = [
    path("", home, name="home"),
    path("videos/<int:page>/<int:per_page_items>", video_list, name="video_list"),
]
