from django.db import models

class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, related_name='ChildrenGroup')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Group(models.Model):
    name = models.CharField(max_length=100)
    kindergarten = models.ForeignKey('Kindergarten', on_delete=models.SET_NULL, null=True, related_name='Kindergarten')

    def __str__(self):
        return self.name
    
class Kindergarten(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TestType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AgeRange(models.Model):
    name = models.CharField(max_length=50)
    min_age = models.IntegerField()
    max_age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.min_age}-{self.max_age})"
    
class Test(models.Model):
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE)

    def __str__(self):
        return f"Test: {self.test_type.name} ({self.age_range})"
    
class Question(models.Model):
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return str(self.test)
    
class AnswerQuestion(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    answer = [
        ('choice1', 'Вариант 1'),
        ('choice2', 'Вариант 2'),
        ('choice3', 'Вариант 3'),
        ('choice4', 'Вариант 4'),
    ]
    text = models.CharField(max_length=20, choices=answer)

    def __str__(self):
        return str(self.children)



class GroupLeader(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, related_name='GroupLeaderGroup')

    def __str__(self):
        return self.name

class Methodologist(models.Model):
    name = models.CharField(max_length=100)
    kindergarten = models.ForeignKey('Kindergarten', on_delete=models.SET_NULL, null=True, related_name='MethodologistKindergarten')

    def __str__(self):
        return self.name
