# Generated by Django 4.2.4 on 2023-08-14 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0002_onboarding_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onboarding',
            old_name='subTitle',
            new_name='sub_title',
        ),
    ]
