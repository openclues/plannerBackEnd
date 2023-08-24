from django.db import models


# Create your models here.
class Onboarding(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='boarding_images/')

    def __str__(self):
        return self.title
