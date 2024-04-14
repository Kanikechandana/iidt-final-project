# Generated by Django 4.1.7 on 2023-04-02 06:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_rename_booked_till_book_end_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
