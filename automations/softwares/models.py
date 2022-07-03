from django.db import models

# Create your models here.
class Software(models.Model):
    sfname=models.CharField(max_length=200)
    sffile=models.FileField(upload_to="static/softwares")

    def __str__(self) -> str:
        return self.sfname