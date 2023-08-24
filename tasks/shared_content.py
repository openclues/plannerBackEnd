from django.db import models

from customuser.models import CustomUser


class SharedContent(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE,
                              related_name='%(class)s_owner')
    shared_with = models.ManyToManyField(CustomUser, blank=True,
                                         related_name="%(class)s_shared_with", null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title or 'Untitled'
