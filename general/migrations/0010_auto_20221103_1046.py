# Generated by Django 3.0.14 on 2022-11-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0009_questionreport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="object_type",
            field=models.CharField(
                choices=[
                    ("Question", "Question"),
                    ("User", "User"),
                    ("Submission", "Submission"),
                    ("Course", "Course"),
                    ("Event", "Event"),
                    ("Course Registration", "Course Registration"),
                    ("Goal", "Goal"),
                    ("Goal Item", "Goal Item"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
