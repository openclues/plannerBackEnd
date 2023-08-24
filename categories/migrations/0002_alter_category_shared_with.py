# Generated by Django 4.2.4 on 2023-08-12 18:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_category', to=settings.AUTH_USER_MODEL),
        ),
    ]
