# Generated by Django 4.1.13 on 2023-12-09 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="danceClasse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(default="", upload_to="classes")),
                ("description", models.TextField()),
                ("startDate", models.DateField()),
                ("duration", models.CharField(max_length=10)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(default="", upload_to="events")),
                ("date", models.DateField()),
                ("location", models.TextField()),
                ("ticketPrice", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("purchaser_name", models.CharField(max_length=255)),
                ("purchaser_email", models.EmailField(max_length=254)),
                ("purchase_date", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="site4life.event",
                    ),
                ),
            ],
        ),
    ]
