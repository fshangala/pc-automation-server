from django.contrib import admin
from pcautomation.models import Connection, Loggedin

@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display=["devicetype","user","datetime"]

@admin.register(Loggedin)
class LoggedinAdmin(admin.ModelAdmin):
    list_display=["devicetype","user","url","datetime"]