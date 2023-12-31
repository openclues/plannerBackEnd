# Generated by Django 4.2.4 on 2023-08-12 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_customuser_partners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='partners',
            field=models.ManyToManyField(blank=True, related_name='partner_of', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PartnerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_approved', models.BooleanField(default=False, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_partner_requests', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_partner_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
