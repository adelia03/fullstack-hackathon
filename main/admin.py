from django.contrib import admin

from .models import *

class HomelessAdmin(admin.ModelAdmin):
    list_filter = ['created_at']

class PetsAdmin(admin.ModelAdmin):
    list_filter = ['created_at']  

class ChildrenAdmin(admin.ModelAdmin):
    list_filter = ['created_at']

class ChildrenHouseAdmin(admin.ModelAdmin):
    list_filter = ['created_at']  

class NarsingHouseAdmin(admin.ModelAdmin):
    list_filter = ['created_at']  

class VolunteerAdmin(admin.ModelAdmin):
    list_filter = ['first_name', 'last_name']

class PartnerAdmin(admin.ModelAdmin):
    list_filter = ['title']          

admin.site.register(Children, ChildrenAdmin)
admin.site.register(ChildrenHouse, ChildrenHouseAdmin)
admin.site.register(Pets, PetsAdmin)
admin.site.register(NarsingHouse, NarsingHouseAdmin)
admin.site.register(Homeless, HomelessAdmin)
admin.site.register(Volunteer,VolunteerAdmin)
admin.site.register(Partner, PartnerAdmin)