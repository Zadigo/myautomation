from campaigns import consumers
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/campaigns/(?P<campaign_id>\d+)/$', consumers.ScrappingConsumer.as_asgi())
]
