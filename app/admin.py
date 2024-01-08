from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Topic)
class customizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','age','location']
    list_display_links=['name']
    list_filter=['topic_name']
    search_fields=['name']
    #list_editable=['location']


class customizeAccess (admin.ModelAdmin):
    list_display=['name','date','author']
   
    list_editable=['date',]
    list_display_links=['author']
    list_filter=['name']
    search_fields=['author']
    #list_per_page=1
    

admin.site.register(Webpage,customizeWebpage)

admin.site.register(Access,customizeAccess)
