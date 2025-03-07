# Generated by Django 3.0.14 on 2021-08-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0006_auto_20210829_1847"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="verb",
            field=models.CharField(
                choices=[
                    ("Created", "Created"),
                    ("Completed", "Completed"),
                    ("Opened", "Opened"),
                    ("Deleted", "Deleted"),
                    ("Delivered", "Delivered"),
                    ("Read", "Read"),
                    ("Solved", "Solved"),
                    ("Submitted", "Submitted"),
                    ("Sent", "Sent"),
                    ("Started", "Started"),
                    ("Used", "Used"),
                    ("Registered", "Registered"),
                    ("Edited", "Edited"),
                    ("Unread", "Unread"),
                    ("Skipped", "Skipped"),
                    ("Logged In", "Logged In"),
                    ("Logged Out", "Logged Out"),
                    ("Evaluated", "Evaluated"),
                ],
                max_length=100,
            ),
        ),
    ]
