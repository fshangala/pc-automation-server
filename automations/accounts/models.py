from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.    
class Room(models.Model):
  name=models.CharField(max_length=200)
  
class Profile(models.Model):
  user=models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
  online=models.BooleanField(default=False)
  channel=models.CharField(max_length=200,null=True)
  rooms=models.ManyToManyField(Room,related_name="profile")
  
  @receiver(post_save, sender=User)
  def _post_save_receiver(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)
      Token.objects.create(user=instance)
    else:
      instance.profile.save()
  