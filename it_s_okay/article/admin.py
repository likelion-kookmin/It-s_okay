from django.contrib import admin
from .models import Article, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)

class SearchAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Article, BoardAdmin)
admin.site.register(Comment)


