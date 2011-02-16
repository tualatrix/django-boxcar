# coding: utf-8

import urllib
import hashlib

from django.db import models
from boxcar.helpers import language_tips 

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon_url = models.URLField(blank=True)
    website_url = models.URLField()
    api_secret = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def fetch_notifications(self):
        for title, link in language_tips.get_title_and_link():
            print title, link
            notification, created = Notification.objects.get_or_create(screen_name=u'酷词',
                                                                       source_url=link,
                                                                       message=title,
                                                                       service=self)
            if created:
                print notification

    def send_notifications(self):
        pass

class Notification(models.Model):
    screen_name = models.CharField(max_length=24)
    message = models.TextField()
    source_url = models.URLField(blank=True)
    service = models.ForeignKey(Service)
    is_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return self.message

    def build_url(self, feature):
        return 'http://boxcar.io/devices/providers/%s/%s' % (self.service.api_key, feature)

    def build_values(self):
        return {'notification[from_screen_name]' : self.screen_name,
                'notification[message]' : self.message,
                'notification[from_remote_service_id]' : int(time()*100),
                'notification[source_url]': self.source_url,
                'notification[icon_url]': self.service.icon_url,
                }

    def do_send_task(self, url, values):
        data = urllib.urlencode(values)

        try:
            response = urllib.urlopen(url, data)
        except IOError as e:
            if (hasattr(e, 'reason')):
                print('Error submitting http request:', e.reason)
                return 1
            if (hasattr(e, 'code')):
                print('Error submitting http request:', e.code)
                return 1
        except Exception as e:
            print('Unhandled error caught', e.str())
            return 1
        return 0

    def broadcast(self):
        url = self.build_url('notifications/broadcast')
        values = self.build_values()
        values['secret'] = self.service.api_secret

        self.do_send_task(url, values)

    def send(self, email):
        url = self.build_url('notifications')
        values = self.build_values()
        values['email'] = hashlib.md5(email).hexdigest()

        self.do_send_task(url, values)

    def subscribe(self, email):
        url = self.build_url('subscribe')
        values = self.build_values()
        values['email'] = hashlib.md5(email).hexdigest()

        self.do_send_task(url, values)
