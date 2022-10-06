from django.db import models

# Create your models here.
class Software(models.Model):
    repositoryname=models.CharField(max_length=200)
    repositoryowner=models.CharField(max_length=200,default="fshangala")

    def __str__(self) -> str:
        return self.repositoryname