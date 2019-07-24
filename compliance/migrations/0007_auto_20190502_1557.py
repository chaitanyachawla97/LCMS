# Generated by Django 2.2 on 2019-05-02 10:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0006_auto_20190502_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplo',
            name='emp_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(6)]),
        ),
    ]