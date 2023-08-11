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
from pcautomation.routing import websocket_urlpatterns
from pcautomation.models import Connection
from pcautomation.serializers import ConnectionSerializer

# Create your tests here.
class PCAutomationTestCase(TestCase):
  application = None
  def setUp(self):
    self.application = TokenAuthMiddleWare(URLRouter(websocket_urlpatterns))
    
  async def test_connection(self):
    print("->",self.id())
    user = await database_sync_to_async(User.objects.create)(username="test",password="test")
    communicator = WebsocketCommunicator(self.application,f"/ws/pcautomation/sample/?token={user.auth_token}")
    connected, subprotocol = await communicator.connect()
    self.assertTrue(connected)
    self.assertFalse(communicator.scope["user"].is_anonymous)
    
    await communicator.disconnect()
  
  async def test_event(self):
    print("->",self.id())
    #connect client and admin
    client_communicator = WebsocketCommunicator(self.application,"/ws/pcautomation/sample/")
    admin_communicator = WebsocketCommunicator(self.application,"/ws/pcautomation/admin/")
    client_connection = await client_communicator.connect()
    admin_connection = await admin_communicator.connect()
    self.assertTrue(client_connection[0])
    self.assertTrue(admin_connection[0])
    
    #client send click command
    await client_communicator.send_json_to({
      "event_type":"mouse",
      "event":"mouse_click",
      "args":[],
      "kwargs":{}
    })
    
    #admin receive command
    json_payload = await admin_communicator.receive_json_from()
    connection_event = await database_sync_to_async(Connection.objects.get)(channel=json_payload["channel"])
    self.assertEqual(connection_event.channel,json_payload["channel"])
    
    #admin get connection from api
    #response = self.client.get("/api/connections/get_by_channel")
    #print(response)
    
    await client_communicator.disconnect()
    await admin_communicator.disconnect()