from django.db import models

# Create your models here.
from customuser.models import CustomUser

#
from tasks.models import SharedContentMixin
from tasks.shared_content import SharedContent


class CategoryShareRequest(SharedContentMixin,models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.approve_and_share(self.category)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.category})"


class Category(SharedContent):
    image = models.ImageField(blank=True, null=True, upload_to='categories')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.title + str(self.id)
