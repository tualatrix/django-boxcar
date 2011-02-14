import urllib

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
        return self.message

    def send(self):
        url = 'http://boxcar.io/devices/providers/L2Kjdc4c1yDDEH8YiADH/notifications'
        values = {
                'email': '3aa394e5aef22274b9d36a74adb787e9',
                'notification[from_screen_name]' : '英语热词',
                'notification[message]' : '返工忧郁症 back-to-work blues',
                'notification[source_url]': 'http://edu.qq.com/a/20110211/000192.htm',
                'notification[icon_url]': 'http://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Gnomelogo.svg/125px-Gnomelogo.svg.png',
                'notification[from_remote_service_id]' : int(time()*100)
                }

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
