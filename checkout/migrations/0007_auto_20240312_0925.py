# Generated by Django 3.2.23 on 2024-03-12 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_coupon_discount_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='discount_amount',
        ),
    ]