import datetime
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from pcautomation.models import Connection

class PCAutomationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        #join room
        async_to_sync(self.channel_layer.group_add)("public",self.channel_name)
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)

        return self.accept()
    
    def disconnect(self, code):
        #leave room
        async_to_sync(self.channel_layer.group_discard)("public",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
        try:
            connection = Connection.objects.get(channel=self.channel_name)
            connection.delete()
        except Exception as e:
            print(e)
    
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        
        handle = f"event_{text_data_json['event_type']}"
        if hasattr(self,handle) and callable(func := getattr(self,handle)):
            func(text_data_json)
        else:
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    'type':'automation_message',
                    'data':text_data_json
                }
            )        
    
    #receive from room
    def automation_message(self,event):
        data = event["data"]

        #send to websocket
        self.send(text_data=json.dumps(data))
        
    def disconnect_channel(self,event):
        if event["event"] == self.channel_name:
            self.close()
    
    def event_connection(self,event):
        connection_data = {
            "devicetype":event["event"],
            "channel":self.channel_name,
            "datetime":datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        }
        Connection.objects.create(**connection_data)
    
    def event_disconnection(self,event):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type':'automation_message',
                'data':event
            }
        )