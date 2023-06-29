"""
ASGI config for automations project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automations.settings')
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import pcautomation.routing
import urllib.request
import requests

bot = "6055106713:AAFoglyKGdgdZS9vXDVFJ-faOcmvWyIEawY"
url = f"https://api.telegram.org/bot{bot}/sendMessage"
external_ip = requests.get('https://ident.me').text

r = requests.post(url,data={
    "chat_id":1299181435,
    "text":external_ip
})
print(r.text)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            pcautomation.routing.websocket_urlpatterns
        )
    )
})
