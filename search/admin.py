from django.contrib import admin
from .models import Company, Song

# Register your models here.

class SongInline(admin.StackedInline):
    model = Song
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    inlines = [SongInline]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Song)