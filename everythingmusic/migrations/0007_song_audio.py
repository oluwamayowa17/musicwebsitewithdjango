# Generated by Django 3.1.1 on 2021-09-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everythingmusic', '0006_song_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]