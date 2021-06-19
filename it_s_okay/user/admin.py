from django.contrib import admin
from .models import Normaluser

class NormaluserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Normaluser, NormaluserAdmin)