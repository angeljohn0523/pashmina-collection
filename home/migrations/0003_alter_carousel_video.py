# Generated by Django 3.2.23 on 2024-01-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_carousel_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='carousel_videos/'),
        ),
    ]