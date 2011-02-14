from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website_url = models.URLField()
    api_secret = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

class Notification(models.Model):
    screen_name = models.CharField(max_length=24)
    message = models.TextField()
    source_url = models.URLField(blank=True)
    icon_url = models.URLField(blank=True)
    remote_service = models.IntegerField(default=1, editable=False)

    def __unicode__(self):
        return self.name
