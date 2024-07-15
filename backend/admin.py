from django.contrib import admin
from .models import Child, Group, Kindergarten, TestType, Test, Question, Answer, GroupLeader, Methodologist

# Inline-модель для ответов

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

# Регистрация моделей в админке Django

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'test_type')
    list_filter = ('test_type',)
    search_fields = ('name',)
    inlines = [AnswerInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test')
    list_filter = ('test',)
    search_fields = ('text',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('child', 'question', 'answered_by', 'answered_at')
    list_filter = ('child__group__kindergarten', 'question__test')
    search_fields = ('child__first_name', 'child__last_name', 'question__text')

# Остальные модели зарегистрированы как ранее

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'group')
    list_filter = ('group__kindergarten',)
    search_fields = ('first_name', 'last_name')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'kindergarten')
    list_filter = ('kindergarten',)
    search_fields = ('name',)

@admin.register(Kindergarten)
class KindergartenAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(TestType)
class TestTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GroupLeader)
class GroupLeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group__kindergarten',)
    search_fields = ('name',)

@admin.register(Methodologist)
class MethodologistAdmin(admin.ModelAdmin):
    list_display = ('name', 'kindergarten')
    list_filter = ('kindergarten',)
    search_fields = ('name',)
