# Generated by Django 5.1.4 on 2025-01-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_customuser_validate_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона'),
        ),
    ]
