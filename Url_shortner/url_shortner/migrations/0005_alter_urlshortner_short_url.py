# Generated by Django 4.2.7 on 2023-11-01 09:07

from django.db import migrations, models
import url_shortner.models


class Migration(migrations.Migration):

    dependencies = [
        ("url_shortner", "0004_alter_urlshortner_short_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlshortner",
            name="short_url",
            field=models.CharField(
                default=url_shortner.models.generate_default_short_url,
                max_length=100,
                unique=True,
            ),
        ),
    ]