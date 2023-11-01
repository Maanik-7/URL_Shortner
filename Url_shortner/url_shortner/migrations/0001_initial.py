# Generated by Django 4.2.7 on 2023-11-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="url_short",
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
                ("long_url", models.CharField(max_length=100)),
                ("short_url", models.URLField()),
            ],
        ),
    ]