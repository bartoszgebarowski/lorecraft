# Generated by Django 4.1.2 on 2022-10-25 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="author",
            new_name="authors",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="genre",
            new_name="genres",
        ),
    ]
