import datetime
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class PCAutomationConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        #join room
        async_to_sync(self.channel_layer.group_add)(self.room_name,self.channel_name)

        return self.accept()
    
    def disconnect(self, code):
        #leave room
        async_to_sync(self.channel_layer.group_discard)(self.room_name,self.channel_name)
    
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        text_data_json["timestamp"] = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        
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