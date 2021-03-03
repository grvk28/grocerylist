# Generated by Django 3.1.7 on 2021-02-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('sbs', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='follow',
        ),
        migrations.DeleteModel(
            name='notif',
        ),
        migrations.DeleteModel(
            name='tag',
        ),
        migrations.DeleteModel(
            name='view',
        ),
        migrations.RenameField(
            model_name='channel',
            old_name='c_art',
            new_name='channel_art',
        ),
        migrations.RenameField(
            model_name='channel',
            old_name='c_icon',
            new_name='channel_icon',
        ),
        migrations.AddField(
            model_name='channel',
            name='category',
            field=models.CharField(default='education', max_length=50),
        ),
        migrations.AlterField(
            model_name='channel',
            name='slug',
            field=models.SlugField(default='grv'),
        ),
    ]