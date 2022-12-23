from django.contrib import admin
from pcautomation.models import LamboConnection

@admin.register(LamboConnection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display=["devicetype","user","datetime"]