from django.db import models
import uuid
from django.utils import timezone

# Create your models here.


class VideoModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500)
    description = models.TextField()
    video_id = models.CharField(unique=True, max_length=255)
    thumbnail = models.URLField()
    publish_time = models.DateTimeField()
    channel_title = models.CharField(max_length=255)

    def __str__(self):
        """
        str(timezone.localtime(self.publish_time)) this line is converting UTC time to local time string
        Returns:
            _string_: video id | time at video publish
        """
        return self.video_id + " | " + str(timezone.localtime(self.publish_time))
