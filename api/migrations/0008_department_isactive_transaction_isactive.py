# Generated by Django 4.1.4 on 2023-10-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_activity_isactive"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="isActive",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="transaction",
            name="isActive",
            field=models.BooleanField(default=True),
        ),
    ]