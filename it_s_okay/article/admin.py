from django.contrib import admin
from .models import Article

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


admin.site.register(Article, BoardAdmin)
