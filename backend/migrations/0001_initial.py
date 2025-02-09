# Generated by Django 5.1.4 on 2025-01-07 10:54

import django.contrib.auth.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='ebooks/')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateField()),
                ('available_copies', models.PositiveIntegerField(default=1)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('isbn', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('pages', models.PositiveIntegerField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('passport_issue_date', models.DateField(blank=True, null=True)),
                ('jshshir_code', models.CharField(blank=True, max_length=14, null=True)),
                ('course', models.CharField(blank=True, max_length=10, null=True)),
                ('group', models.CharField(blank=True, max_length=10, null=True)),
                ('academic_year', models.CharField(blank=True, max_length=20, null=True)),
                ('semester', models.CharField(blank=True, max_length=10, null=True)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('education_type', models.CharField(blank=True, max_length=50, null=True)),
                ('education_form', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
