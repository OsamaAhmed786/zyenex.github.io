# Generated by Django 5.0.4 on 2024-06-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Zyenex_A", "0003_newslettersubscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="items",
            name="video",
            field=models.FileField(
                blank=True, null=True, upload_to="static\\DB_upload\x0bideos"
            ),
        ),
        migrations.AlterField(
            model_name="items",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="static\\DB_upload"
            ),
        ),
    ]
