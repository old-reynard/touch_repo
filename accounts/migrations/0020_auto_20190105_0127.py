# Generated by Django 2.1.4 on 2019-01-05 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20190105_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appuser',
            old_name='confirmed_date',
            new_name='confirmed_at',
        ),
    ]