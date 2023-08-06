from django.test import TestCase
from django.urls import path
from channels.testing import WebsocketCommunicator
from channels.routing import URLRouter
from channels.db import database_sync_to_async
from pcautomation.consumers import PCAutomationConsumer
from accounts.middlewares import TokenAuthMiddleWare
from rich import print
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

# Create your tests here.
class PCAutomationTestCase(TestCase):
  application = None
  def setUp(self):
    self.application = TokenAuthMiddleWare(URLRouter([
      path("ws/pcautomation/<room_name>/",PCAutomationConsumer.as_asgi())
    ]))
    
  async def test_connection(self):
    user = await database_sync_to_async(User.objects.create)(username="test",password="test")
    communicator = WebsocketCommunicator(self.application,f"/ws/pcautomation/sample/?token={user.auth_token}")
    connected, subprotocol = await communicator.connect()
    self.assertTrue(connected)
    self.assertFalse(communicator.scope["user"].is_anonymous)
    
    await communicator.disconnect()