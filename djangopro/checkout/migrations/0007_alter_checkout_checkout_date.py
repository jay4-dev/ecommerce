# Generated by Django 4.1.7 on 2023-03-29 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_checkout_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 28, 10, 53, 4, 240756, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
