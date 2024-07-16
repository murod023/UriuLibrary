from django.contrib import admin
from .models import Child, Group, Kindergarten, TestType, AgeRange, Test, Question, GroupLeader, Methodologist, AnswerQuestion

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'group')
    list_filter = ('group', 'age')
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

@admin.register(AgeRange)
class AgeRangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_age', 'max_age')
    search_fields = ('name',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_type', 'age_range')
    list_filter = ('test_type', 'age_range')
    search_fields = ('test_type__name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test',)
    list_filter = ('test',)

@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'child', 'answer')

@admin.register(GroupLeader)
class GroupLeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)
    search_fields = ('name',)

@admin.register(Methodologist)
class MethodologistAdmin(admin.ModelAdmin):
    list_display = ('name', 'kindergarten')
    list_filter = ('kindergarten',)
    search_fields = ('name',)

