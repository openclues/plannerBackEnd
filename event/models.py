from django.db import models


# Create your models here.
from customuser.models import CustomUser
from tasks.shared_content import SharedContent
from tasks.shared_mixin_model import SharedContentMixin


class EventShareRequest(SharedContentMixin, models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.approve_and_share(self.event)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.event})"


class Event(SharedContent):
    def __str__(self):
        return self.title + str(self.id)
