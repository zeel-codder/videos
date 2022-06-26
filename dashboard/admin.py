from django.contrib import admin

# Register your models here.
from .models import VideoModel, KeyModel


admin.site.register(VideoModel)
admin.site.register(KeyModel)
