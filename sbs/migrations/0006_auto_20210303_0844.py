# Generated by Django 3.1.7 on 2021-03-03 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sbs', '0005_auto_20210303_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='user',
            field=models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
