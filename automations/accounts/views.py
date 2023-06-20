from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token

# Create your views here.
class LoggedInUser(APIView):
  def get(self,request):
    token = request.GET.get("token",None)
    if token:
      try:
        token_object = Token.objects.get(key=token)
      except Exception as e:
        return Response({"error":"invalid token"})
      else:
        user = UserSerializer(token_object.user)
        return Response(user.data)
    else:
      return Response({"error":"no token provided"})