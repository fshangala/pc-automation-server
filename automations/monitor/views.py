from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from pcautomation.models import Connection
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