from django.contrib import admin
from pcautomation.models import Connection

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display=["devicetype","user","datetime"]