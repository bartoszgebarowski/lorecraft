# Generated by Django 4.1.2 on 2022-11-24 13:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_rename_context_review_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MaxValueValidator(10),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
