# Generated by Django 4.2.4 on 2023-08-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
