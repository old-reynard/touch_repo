# Generated by Django 2.1.4 on 2018-12-28 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20181228_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='from_whom',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='from_whom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='to_whom',
            field=models.ForeignKey(default=2, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='to_whom', to=settings.AUTH_USER_MODEL),
        ),
    ]
