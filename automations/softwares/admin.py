from django.contrib import admin
from softwares.models import Software, BetSite, BetSiteDesktop

# Register your models here.
admin.site.register(Software)

@admin.register(BetSite)
class BetSiteModelAdmin(admin.ModelAdmin):
  list_display=['id','name','url']

@admin.register(BetSiteDesktop)
class BetSiteDesktopModelAdmin(admin.ModelAdmin):
  list_display=['id','name','url']