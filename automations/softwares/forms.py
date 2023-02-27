from django import forms
import pandas
from softwares.models import (
  Software
)

class UploadSoftwaresForm(forms.Form):
  softwarescsv = forms.FileField(required=True,widget=forms.FileInput(attrs={
    "class":"form-control"
  }))
  
  def save(self):
    df = pandas.read_csv(self.cleaned_data["softwarescsv"])
    for index, row in df.iterrows():
      Software.objects.update_or_create(
        repositoryname=row["repositoryname"],
        defaults={
          "repositoryowner":row["repositoryowner"]
        }
      )
  
class UploadBetSitesForm(forms.Form):
  betcsv = forms.FileField(required=True,widget=forms.FileInput(attrs={
    "class":"form-control"
  }))
  
  def save(self):
    df = pandas.read_csv(form.cleaned_data["betcsv"])
    for index, row in df.iterrows():
      defaults = {
        "url":row["url"],
        "bet_buttons":row["bet_buttons"],
        "input_elements":row["input_elements"],
        "odds_input":row["odds_input"],
        "stake_input":row["stake_input"],
        "alt_stake_input":row["alt_stake_input"],
        "betslip_buttons":row["betslip_buttons"],
        "confirm_button":row["confirm_button"],
        "username_input":row["username_input"],
        "login_button":row["login_button"]
      }
      if row["platform"] == "desktop":
        BetSiteDesktop.objects.update_or_create(
          name=row["name"],
          defaults=defaults
        )
      elif row["platform"] == "mobile":
        BetSite.objects.update_or_create(
          name=row["name"],
          defaults=defaults
        )