from django.conf.urls.defaults import *
from boxcar.models import NotificationPage

page_dict = {
    'queryset': NotificationPage.objects.all(),
}

urlpatterns = patterns('',
    url(r'^notifications/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', page_dict, name='notification_page_detail'),
)
