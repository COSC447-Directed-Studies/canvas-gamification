# Generated by Django 3.0.7 on 2020-10-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_myuser_student_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConsent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('student_number', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
