# Generated by Django 3.1.1 on 2021-09-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everythingmusic', '0005_auto_20210929_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Song Image'),
        ),
    ]
