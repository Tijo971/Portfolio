# Generated by Django 5.1.6 on 2025-02-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tijo_portfolio', '0004_remove_profile_age_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
