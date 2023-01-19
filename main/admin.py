from django.contrib import admin

from .models import *

class HomelessAdmin(admin.ModelAdmin):
    list_filter = ['created_at']

class PetsAdmin(admin.ModelAdmin):
    list_filter = ['created_at']  

class ChildrenAdmin(admin.ModelAdmin):
    list_filter = ['created_at']

class Children_HouseAdmin(admin.ModelAdmin):
    list_filter = ['created_at']  

class Narsing_HouseAdmin(admin.ModelAdmin):
    list_filter = ['created_at']            

admin.site.register(Children, ChildrenAdmin)
admin.site.register(Pets, PetsAdmin)
admin.site.register(NarsingHouse, Narsing_HouseAdmin)
admin.site.register(ChildrenHouse, Children_HouseAdmin)
admin.site.register(Homeless, HomelessAdmin)