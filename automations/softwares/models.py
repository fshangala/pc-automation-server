from django.db import models
from django.urls import reverse

# Create your models here.
class Software(models.Model):
    repositoryname=models.CharField(max_length=200)
    repositoryowner=models.CharField(max_length=200,default="fshangala")
    
    def get_absolute_url(self):
        return reverse("softwares-detail",kwargs={'pk':self.pk})

    def __str__(self) -> str:
        return self.repositoryname

class BetSite(models.Model):
    name=models.CharField(max_length=200)
    url=models.URLField()
    bet_buttons=models.CharField(max_length=200)
    input_elements=models.CharField(max_length=200)
    odds_input=models.IntegerField()
    stake_input=models.IntegerField()
    alt_stake_input=models.IntegerField()
    betslip_buttons=models.CharField(max_length=200)
    confirm_button=models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    