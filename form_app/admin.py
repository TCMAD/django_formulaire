from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Formulaire

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'gender', 'email', 'info', 'phone')
    list_display_links = ('id','name')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender','date_added')

admin.site.register(Formulaire, FormAdmin)
admin.site.unregister(Group)
