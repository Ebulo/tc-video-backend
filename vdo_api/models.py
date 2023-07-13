from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    class VideoManager(models.Manager):
        class VideoQuerySet(models.QuerySet):
            def user_search(self, user):
                if user:
                    return self.filter(user__username__in=user)
                return self

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to="videos/upload/")
    subtitle = models.TextField(null=True, blank=True)
    subtitle_file = models.FileField(upload_to="subtitles/upload/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.BigIntegerField(default=0)
    views = models.BigIntegerField(default=0)

    # We can use these as additional features in a more production like settings
    # tags = models.ManyToManyField('Tags')
    # comments = models.ManyToManyField('Comments')