# Generated by Django 5.1.6 on 2025-02-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tijo_portfolio', '0006_alter_profile_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
