from django.urls import path
from .views import (
  MonitorView,
  TestingView
)

app_name="monitor"
urlpatterns=[
  path('',MonitorView.as_view(),name="index"),
  path('testing/',TestingView.as_view(),name="testing")
]