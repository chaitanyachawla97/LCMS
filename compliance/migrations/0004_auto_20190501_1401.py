# Generated by Django 2.2 on 2019-05-01 08:31

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0003_auto_20190501_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplo',
            name='emp_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(6)], verbose_name=django.contrib.auth.models.User),
        ),
    ]
