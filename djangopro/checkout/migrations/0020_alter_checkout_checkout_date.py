# Generated by Django 4.2 on 2023-05-05 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 5, 9, 22, 57, 868850, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
