from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.
class Connection(models.Model):
    devicetype=models.CharField(max_length=200)
    channel=models.CharField(max_length=200,unique=True)
    user=models.CharField(max_length=200,null=True)
    datetime=models.CharField(max_length=200)
    
    @receiver(post_delete)
    def disconnect_channel(sender,instance,**kwargs):
        if sender == Connection:
            text_data_json={
                "event_type":"disconnection",
                "event":instance.channel,
                "args":[],
                "kwargs":{}
            }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("public",{
                'type':'disconnect_channel',
                'data':text_data_json
            })
    
    def __str__(self) -> str:
        return self.devicetype + " " + self.datetime