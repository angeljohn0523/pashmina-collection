# Generated by Django 3.2.23 on 2024-01-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]