
from django.contrib import admin
from .models import Free

class FreeAdmin(admin.ModelAdmin):
    list_display = (
        'title',  
        'hits',
        'registered_date',
        )
    search_fields = ('title', 'content')

admin.site.register(Free, FreeAdmin)