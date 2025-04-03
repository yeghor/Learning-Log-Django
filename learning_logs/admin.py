from django.contrib import admin

# Register your models here.

from .models import Topics, Entry
admin.site.register(Topics)
admin.site.register(Entry)
