from django.contrib import admin

# Register your models here.
from categories.models import Category, CategoryShareRequest

admin.site.register(Category)
admin.site.register(CategoryShareRequest)
