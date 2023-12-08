# Generated by Django 4.1.13 on 2023-12-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dancersite", "0002_rename_danceclass_danceclasse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="danceclasse",
            name="image",
            field=models.ImageField(default="", upload_to="classes"),
        ),
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(default="", upload_to="events"),
        ),
    ]
