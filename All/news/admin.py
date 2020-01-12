from django.contrib import admin
from .models import Album, Song
# Register your models here.

class albumAdmin(admin.ModelAdmin):
    list_display = ("title","artist")
    list_filter = ("artist",)
    search_fields = ("title",)


admin.site.register(Album, albumAdmin)
admin.site.register(Song)