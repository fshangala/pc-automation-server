from django import forms

class UploadBetSitesForm(forms.Form):
  betcsv = forms.FileField(required=True,widget=forms.FileInput(attrs={
    "class":"form-control"
  }))