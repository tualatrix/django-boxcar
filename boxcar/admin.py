from django.contrib import admin

from boxcar.models import Service, Notification, NotificationPage

admin.site.register(Service)
admin.site.register(Notification)
admin.site.register(NotificationPage)
