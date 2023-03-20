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