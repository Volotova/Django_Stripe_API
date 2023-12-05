from django.contrib import admin

from .models import *


class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

admin.site.register(Item, AppAdmin)