from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.conf import settings
from pcautomation.models import Connection, Loggedin
from pcautomation.serializers import ConnectionSerializer

class MonitorView(TemplateView):
  template_name="monitor/index.html"

class TestingView(TemplateView):
  template_name="monitor/testing.html"

class ConnectionsList(ListView):
  model=Connection
  context_object_name="connections"
  template_name="monitor/connection_list.html"

class ConnectionDetail(DetailView):
  model=Connection
  context_object_name="connection"
  template_name="monitor/connection_detail.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["logins"] = Loggedin.objects.filter(devicetype=context["connection"].devicetype)
    return context

class SpyView(View):
  def get(self,request):
    template_name="monitor/spy.html"
    context={}
    
    connections = Connection.objects.all()
    context["connections"]=connections
    return render(request,template_name,context)

class SpyConnectionView(View):
  def get(self,request,pk):
    template_name="monitor/spy-connection.html"
    context={}
    
    connection = Connection.objects.get(pk=pk)
    context["connection"]=ConnectionSerializer(connection).data
    return render(request,template_name,context)

class SpyAllView(View):
  def get(self,request):
    template_name="monitor/spy-all.html"
    context={}
    
    return render(request,template_name,context)