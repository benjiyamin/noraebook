from django.contrib import admin
from .models import Company, Song, UserProfile

# Register your models here.

class SongInline(admin.StackedInline):
    model = Song
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [SongInline]


class SongAdmin(admin.ModelAdmin):
    list_display = ('code', 'company', 'title', 'likes', 'approved')
    list_filter = ['likes', 'approved']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(UserProfile)