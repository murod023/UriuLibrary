from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Talaba ID (логин)
    username = models.CharField(max_length=20, unique=True, blank=False, null=False)
    
    # Текущие дополнительные поля
    full_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    passport_issue_date = models.DateField(null=True, blank=True)
    jshshir_code = models.CharField(max_length=14, blank=True, null=True)  # JSHSHIR-код
    course = models.CharField(max_length=10, blank=True, null=True)
    group = models.CharField(max_length=10, blank=True, null=True)
    academic_year = models.CharField(max_length=20, blank=True, null=True)
    semester = models.CharField(max_length=10, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    education_type = models.CharField(max_length=50, blank=True, null=True)  # "O‘quv yili"
    education_form = models.CharField(max_length=50, blank=True, null=True)  # "Ta’lim shakli"
    
    # Поле для хранения изображения профиля (опционально)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    # Поле для того, чтобы пометить администратора
    is_admin = models.BooleanField(default=False)  # Admin flag
    
    def __str__(self):
        return self.full_name if self.full_name else self.username


# Модель для физических книг
class PhysicalBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class ElectronicBook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='ebooks/')

    def __str__(self):
        return self.title
