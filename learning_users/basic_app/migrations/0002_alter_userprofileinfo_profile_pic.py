# Generated by Django 4.1 on 2023-06-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofileinfo",
            name="profile_pic",
            field=models.ImageField(blank=True, upload_to="profile_pics/"),
        ),
    ]
