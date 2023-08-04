from django.test import TestCase
from accounts.models import Profile
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer

# Create your tests here.
class ProfileTestCase(TestCase):
  def test_profile_created(self):
    user = User.objects.create(username="test",password="test")
    user_json = UserSerializer(user).data
    print(user_json)