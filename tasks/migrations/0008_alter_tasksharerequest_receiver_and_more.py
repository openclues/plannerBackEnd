# Generated by Django 4.2.4 on 2023-08-12 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_alter_tasksharerequest_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksharerequest',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_received_share_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasksharerequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_sent_share_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
