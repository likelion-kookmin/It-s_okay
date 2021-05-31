from django.contrib import admin
from .models import Article

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class SearchAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Article, BoardAdmin)
