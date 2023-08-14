from django.conf import settings

def settings_processor(request):
  return {
    "django_settings":{
      "debug":settings.DEBUG
    }
  }