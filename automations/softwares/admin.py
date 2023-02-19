from django.contrib import admin
from softwares.models import Software, BetSite

# Register your models here.
admin.site.register(Software)

@admin.register(BetSite)
class BetSiteModelAdmin(admin.ModelAdmin):
  list_display=['id','name','url']