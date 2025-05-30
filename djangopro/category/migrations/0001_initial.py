# Generated by Django 4.1.7 on 2023-03-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('Category_image', models.ImageField(upload_to='img/categoryimg')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
