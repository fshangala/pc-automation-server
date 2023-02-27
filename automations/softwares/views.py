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
from .forms import UploadBetSitesForm
from django.shortcuts import reverse
import pandas

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
            df = pandas.read_csv(form.cleaned_data["betcsv"])
            for index, row in df.iterrows():
                if row["platform"] == "desktop":
                    BetSiteDesktop.objects.update_or_create(
                        name=row["name"],
                        defaults={
                            "url":row["url"],
                            "bet_buttons":row["bet_buttons"],
                            "input_elements":row["input_elements"],
                            "odds_input":row["odds_input"],
                            "stake_input":row["stake_input"],
                            "alt_stake_input":row["alt_stake_input"],
                            "betslip_buttons":row["betslip_buttons"],
                            "confirm_button":row["confirm_button"]
                        }
                    )
                elif row["platform"] == "mobile":
                    BetSite.objects.update_or_create(
                        name=row["name"],
                        defaults={
                            "url":row["url"],
                            "bet_buttons":row["bet_buttons"],
                            "input_elements":row["input_elements"],
                            "odds_input":row["odds_input"],
                            "stake_input":row["stake_input"],
                            "alt_stake_input":row["alt_stake_input"],
                            "betslip_buttons":row["betslip_buttons"],
                            "confirm_button":row["confirm_button"]
                        }
                    )
            
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
