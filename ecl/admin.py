from django.contrib import admin

# Register your models here.
from .models import Entry, Tag

admin.site.register(Entry)
admin.site.register(Tag)