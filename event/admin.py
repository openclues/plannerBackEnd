from django.contrib import admin

# Register your models here.
from .models import Event, EventShareRequest

admin.site.register(Event)
admin.site.register(EventShareRequest)