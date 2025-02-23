# Generated by Django 5.1.4 on 2025-01-20 06:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_author_category_librarysettings_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='borrowingrecord',
            options={'verbose_name': 'Запись о выдаче', 'verbose_name_plural': 'Записи о выдачах'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='electronicbook',
            options={'verbose_name': 'Электронная книга', 'verbose_name_plural': 'Электронные книги'},
        ),
        migrations.AlterModelOptions(
            name='librarysettings',
            options={'verbose_name': 'Настройки библиотеки', 'verbose_name_plural': 'Настройки библиотеки'},
        ),
        migrations.AlterModelOptions(
            name='physicalbook',
            options={'verbose_name': 'Физическая книга', 'verbose_name_plural': 'Физические книги'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.physicalbook', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='borrow_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='is_returned',
            field=models.BooleanField(default=False, verbose_name='Возвращено'),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата возврата'),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='academic_year',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Академический год'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='course',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='education_form',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='education_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип образования'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Администратор'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(blank=True, null=True, verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(blank=True, null=True, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='jshshir_code',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Код JSHSHIR'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='passport_issue_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выдачи паспорта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/', verbose_name='Фото профиля'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='semester',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Семестр'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='specialization',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='electronicbook',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='electronicbook',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='electronicbook',
            name='file',
            field=models.FileField(upload_to='ebooks/', verbose_name='Файл книги'),
        ),
        migrations.AlterField(
            model_name='electronicbook',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='librarysettings',
            name='max_borrow_days',
            field=models.PositiveIntegerField(default=14, verbose_name='Максимальные дни аренды'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='available_copies',
            field=models.PositiveIntegerField(default=1, verbose_name='Доступные копии'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='barcode',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Штрихкод'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Изображение обложки'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='pages',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='publication_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='physicalbook',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.physicalbook', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(verbose_name='Содержание отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
