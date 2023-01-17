from django.contrib import admin

from .models import *

class HomelessAdmin(admin.ModelAdmin):
    list_filter = ['created_at']

class PetsAdmin(admin.ModelAdmin):
    list_filter = ['create']  

class ChildrenAdmin(admin.ModelAdmin):
    list_filter = ['create']

class Children_HouseAdmin(admin.ModelAdmin):
    list_filter = ['create']  

class Narsing_HouseAdmin(admin.ModelAdmin):
    list_filter = ['create']            

admin.site.register(Children, ChildrenAdmin)
admin.site.register(Pets,PetsAdmin)
admin.site.register(Narsing_House,Narsing_HouseAdmin)
admin.site.register(Children_House,Children_HouseAdmin)
admin.site.register(Homeless,HomelessAdmin)



