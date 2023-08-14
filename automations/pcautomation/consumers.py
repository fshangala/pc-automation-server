import datetime
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import django
django.setup()
from pcautomation.models import Connection, Loggedin
from pcautomation.serializers import ConnectionSerializer
from django.utils import timezone

class AutomationConsumer(WebsocketConsumer):
    def connect(self):
        pass
    
    def disconnect(self,code):
        pass
    
    def receive(self,text_data=None,bytes_data=None):
        pass

class PCAutomationConsumer(WebsocketConsumer):
    def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        #save connection
        connection_data = {
            "devicetype":self.scope["devicetype"],
            "channel":self.channel_name,
            "datetime":timezone.now().strftime("%d-%b-%Y %H:%M:%S"),
            "code":self.room_name
        }
        if not self.scope["user"].is_anonymous:
            connection_data["l_user"]=self.scope["user"]
        
        Connection.objects.create(**connection_data)

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
        text_data_json["channel"] = self.channel_name
        text_data_json["code"] = self.room_name
        
        connection = Connection.objects.get(channel=self.channel_name)
        text_data_json["connection"] = ConnectionSerializer(connection).data
        
        async_to_sync(self.channel_layer.group_send)(
            "admin",
            {
                'type':'automation_message',
                'data':text_data_json
            }
        )
        
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
        if event["data"]["event"] == self.channel_name:
            self.close()
    
    def event_user(self,event):
        conn = Connection.objects.get(channel=self.channel_name)
        conn.user = event["args"][0]
        conn.save()
        luser = Loggedin.objects.create(
            devicetype=conn.devicetype,
            user=event["args"][0]
        )
        if len(event["args"]) == 3:
            luser.url = event["args"][1]
            luser.datetime = event["args"][2]
            luser.save()
    
    def event_connection(self,event):
        connection_data = {
            "devicetype":event["event"],
            "datetime":timezone.now().strftime("%d-%b-%Y %H:%M:%S")
        }
        if len(event["args"]) > 0:
            connection_data["devicetype"] = event["args"][0]
        
        user = self.scope["user"]
        if user.is_anonymous:
            pass
        else:
            connection_data["l_user"]=user
            
        Connection.objects.update_or_create(channel=self.channel_name,defaults=connection_data)
        
        logins = event["kwargs"].get("logins",[])
        for l in logins:
            Loggedin.objects.create(
                devicetype=connection_data["devicetype"],
                **l
            )
    
    def event_disconnection(self,event):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type':'automation_message',
                'data':event
            }
        )