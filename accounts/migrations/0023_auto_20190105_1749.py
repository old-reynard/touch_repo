# Generated by Django 2.1.4 on 2019-01-05 22:49

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20190105_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=accounts.models.upload_location, width_field='width_field'),
        ),
    ]
