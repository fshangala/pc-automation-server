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
from django.urls import path, include
from django.views.generic import RedirectView
from softwares.views import SoftwareListView, SoftwareDetailView, UploadBetsites, UploadSoftwares
from pcautomation.views import AutomationView, SoftwareVersion
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from pcautomation.urls import router as pcautomationRouter
from softwares.urls import router as softwareRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.registry.extend(pcautomationRouter.registry)
router.registry.extend(softwareRouter.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SoftwareListView.as_view(),name="softwares-list"),
    path('detail/<pk>/',SoftwareDetailView.as_view(),name="softwares-detail"),
    path('upload/',UploadBetsites.as_view(),name="upload-betsites"),
    path('upload/softwares/',UploadSoftwares.as_view(),name="upload-softwares"),
    path('api/pcautomation/<code>/',AutomationView.as_view(),name="apiauto"),
    path('api/version/',SoftwareVersion.as_view(),name="version"),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL+'images/favicon.ico')),
    path('monitor/',include("monitor.urls")),
    path('accounts/',include("accounts.urls")),
    path('api/',include(router.urls))
]
