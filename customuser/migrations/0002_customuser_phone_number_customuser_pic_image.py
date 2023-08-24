# Generated by Django 4.2.4 on 2023-08-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pic_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]