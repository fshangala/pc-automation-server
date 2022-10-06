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