from django.contrib import admin

# Register your models here.
from tasks.models import Task,TaskShareRequest

admin.site.register(Task)
admin.site.register(TaskShareRequest)
