from django.urls import path
from rest_framework.authtoken import views
from accounts.views import LoggedInUser

app_name="accounts"
urlpatterns = [
  path('api/token-auth/',views.obtain_auth_token),
  path('api/loggedin-user/',LoggedInUser.as_view(),name="loggedin-user"),
]
