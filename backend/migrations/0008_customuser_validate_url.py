# Generated by Django 5.1.4 on 2025-01-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_electronicbook_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='validate_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка для проверки'),
        ),
    ]
