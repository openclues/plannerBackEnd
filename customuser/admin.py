from django.contrib import admin

# Register your models here.
from .models import CustomUser, PartnerRequest

admin.site.register(CustomUser)
admin.site.register(PartnerRequest)