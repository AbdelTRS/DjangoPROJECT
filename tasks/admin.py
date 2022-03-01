from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ['name', 'status']

admin.site.register(Task)