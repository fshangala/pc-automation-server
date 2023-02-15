from django.urls import path
from .views import (
  MonitorView,
  TestingView,
  ConnectionsList,
  ConnectionDetail
)

app_name="monitor"
urlpatterns=[
  path('',MonitorView.as_view(),name="index"),
  path('testing/',TestingView.as_view(),name="testing"),
  path('connections/',ConnectionsList.as_view(),name="connections"),
  path('connections/id/<pk>/',ConnectionDetail.as_view(),name="connection"),
]