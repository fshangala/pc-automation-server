import mimetypes
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Software, BetSite
from .serializers import BetSiteSerializer
from django.contrib.auth.decorators import login_required
import os
from softwares.serializers import SoftwareSerializer
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

class SoftwareListView(ListView):
    model=Software
    context_object_name="softwares"

class SoftwareDetailView(DetailView):
    model=Software
    context_object_name="software"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["software"] = SoftwareSerializer(context["software"]).data
        
        return context

class BetSiteViewset(viewsets.ReadOnlyModelViewSet):
    queryset=BetSite.objects.all()
    serializer_class=BetSiteSerializer
