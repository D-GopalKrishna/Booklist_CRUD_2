# Generated by Django 3.1.3 on 2020-11-13 07:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookdetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ratings',
            field=models.PositiveIntegerField(default=6, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]