from django.urls import re_path
from pcautomation.consumers import PCAutomationConsumer

websocket_urlpatterns = [
    re_path(r'ws/pcautomation/(?P<room_name>\w+)/$', PCAutomationConsumer.as_asgi()),
]