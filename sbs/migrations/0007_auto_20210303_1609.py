# Generated by Django 3.1.7 on 2021-03-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbs', '0006_auto_20210303_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
