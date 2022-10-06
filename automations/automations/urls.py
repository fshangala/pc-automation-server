"""automations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from softwares.views import SoftwareListView, SoftwareDetailView
from pcautomation.views import AutomationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SoftwareListView.as_view(),name="softwares-list"),
    path('detail/<pk>/',SoftwareDetailView.as_view(),name="softwares-detail"),
    path('api/pcautomation/<code>/',AutomationView.as_view(),name="apiauto"),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL+'images/favicon.ico')),
]
