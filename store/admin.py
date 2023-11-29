
from django.contrib import admin
from .models import Artist
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display =["name","Artist","Song"]
    list_filter =["Artist","Song"]

admin.site.register([Artist,Song])

# Register your models here.
