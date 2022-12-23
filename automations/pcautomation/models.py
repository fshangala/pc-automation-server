from django.db import models

# Create your models here.
class Connection(models.Model):
    devicetype=models.CharField(max_length=200)
    channel=models.CharField(max_length=200,unique=True)
    user=models.CharField(max_length=200,null=True)
    datetime=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.devicetype + " " + self.datetime
