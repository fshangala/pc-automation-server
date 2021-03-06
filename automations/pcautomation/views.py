from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json, datetime

# Create your views here.
class AutomationView(APIView):
    def post(self,request,code,format=None):
        text_data_json = dict(request.data)
        text_data_json["timestamp"] = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(code,{
            'type':'automation_message',
            'data':text_data_json
        })
        return Response(text_data_json)