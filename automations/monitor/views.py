from django.shortcuts import render
from django.views.generic import TemplateView

class MonitorView(TemplateView):
  template_name="monitor/index.html"

class TestingView(TemplateView):
  template_name="monitor/testing.html"