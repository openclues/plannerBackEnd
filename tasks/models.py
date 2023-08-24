from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField
from rest_framework.exceptions import ValidationError

from customuser.models import CustomUser
from tasks.shared_content import SharedContent
from tasks.shared_mixin_model import SharedContentMixin


class TaskShareRequest(SharedContentMixin, models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.approve_and_share(self.task)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sender} -> {self.receiver} ({self.task})"


class Task(SharedContent):
    class RepeatOptions(models.TextChoices):
        REPEATED = 'repeated', 'Repeated'
        NOREAPTING = 'not repeated', 'Not repeated'

    class IntervalOptions(models.TextChoices):
        HOURS = 'hours', 'Hours'
        DAYS = 'days', 'Days'
        WEEKS = 'weeks', 'Weeks'
        MONTHS = 'months', 'Months'

    DAYS_OF_WEEK = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]
    interval_option = models.CharField(max_length=10, choices=IntervalOptions.choices, default=IntervalOptions.DAYS)
    interval_value = models.PositiveIntegerField(default=1)

    repeating = models.CharField(max_length=30, choices=RepeatOptions.choices, default=RepeatOptions.REPEATED)
    task_amount = models.FloatField(blank=True, null=True)
    task_unit = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    exact_day = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    who_has_to_make = models.ManyToManyField(CustomUser, blank=True,related_name="duties")
    custom_days = MultiSelectField(max_length=10, choices=DAYS_OF_WEEK, blank=True, null=True, )
    start_date = models.DateTimeField(blank=True, null=True)  # Start time of the task


    def __str__(self):
        return self.title or 'Untitled Task'

