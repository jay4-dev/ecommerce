# Generated by Django 4.1.5 on 2023-04-04 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_checkout_checkout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='Payment_type',
            field=models.CharField(choices=[('COD', 'COD'), ('Online', 'Online')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 4, 13, 18, 45, 727922, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
