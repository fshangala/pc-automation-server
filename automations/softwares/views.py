import mimetypes
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Software, BetSite, BetSiteDesktop
from .serializers import BetSiteSerializer, BetSiteDesktopSerializer
from django.contrib.auth.decorators import login_required
import os
from softwares.serializers import SoftwareSerializer
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework import viewsets
from .forms import UploadBetSitesForm, UploadSoftwaresForm
from django.shortcuts import reverse
import pandas

class UploadSoftwares(TemplateView):
    template_name="softwares/upload_softwares.html"
    
    def get(self, request):
        context = {
            "form":UploadSoftwaresForm(),
            "softwares":Software.objects.all()
        }
        return render(request, self.template_name,context=context)
    
    def post(self,request,*args,**kwargs):
        form = UploadSoftwaresForm(request.POST,request.FILES)
        context = {
            "form":form,
            "softwares":Software.objects.all()
        }
        
        if form.is_valid():
            form.save()
            
        return render(request, self.template_name,context=context)

class UploadBetsites(TemplateView):
    template_name="softwares/upload_betsites.html"
    
    def get(self, request):
        context = {
            "form":UploadBetSitesForm(),
            "mobiles":BetSite.objects.all(),
            "desktops":BetSiteDesktop.objects.all()
        }
        return render(request, self.template_name,context=context)
    
    def post(self,request,*args,**kwargs):
        form = UploadBetSitesForm(request.POST,request.FILES)
        context = {
            "form":form,
            "mobiles":BetSite.objects.all(),
            "desktops":BetSiteDesktop.objects.all()
        }
        
        if form.is_valid():
            form.save()
            
        return render(request, self.template_name,context=context)

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

class BetSiteDesktopViewset(viewsets.ReadOnlyModelViewSet):
    queryset=BetSiteDesktop.objects.all()
    serializer_class=BetSiteDesktopSerializer
