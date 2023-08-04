from rest_framework.serializers import ModelSerializer,RelatedField
from django.contrib.auth.models import User
from accounts.models import Profile

class ProfileSerializer(ModelSerializer):
  class Meta:
    model=Profile
    fields="__all__"
    
class UserSerializer(ModelSerializer):
  profile=ProfileSerializer(read_only=True)
  class Meta:
    model=User
    fields=["id","username","first_name","last_name","email","is_superuser","is_staff","profile"]