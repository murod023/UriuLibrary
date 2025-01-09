from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, PhysicalBook, ElectronicBook

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'full_name', 'is_admin', 'is_active']
    search_fields = ['username', 'full_name']

# Админ-панель для физических книг
class PhysicalBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'available_copies', 'isbn', 'category', 'language', 'publisher')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('category', 'language', 'publication_date')
    ordering = ('-publication_date',)
    list_per_page = 20  # Количество объектов на странице

# Админ-панель для электронных книг
class ElectronicBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'file')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category',)
    ordering = ('-title',)

# Регистрация моделей в админ-панели
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PhysicalBook, PhysicalBookAdmin)
admin.site.register(ElectronicBook, ElectronicBookAdmin)
