from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from boxcar.models import Service

class Command(BaseCommand):
    def handle(self, *args, **options):
        sync_list = []
        if args:
            for name in args:
                sync_list.extend(Service.objects.filter(name=name))
        else:
            sync_list.extend(list(Service.objects.all()))

        for service in sync_list:
            service.fetch_notifications()
            service.create_notification_pages()
            service.send_notifications()
