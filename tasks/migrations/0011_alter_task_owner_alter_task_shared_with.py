# Generated by Django 4.2.4 on 2023-08-12 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0010_task_who_has_to_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='shared_with',
            field=models.ManyToManyField(blank=True, null=True, related_name='%(class)s_shared_with', to=settings.AUTH_USER_MODEL),
        ),
    ]
