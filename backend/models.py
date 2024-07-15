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

class Test(models.Model):
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE, related_name='tests')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    answered_by = models.ForeignKey('GroupLeader', on_delete=models.SET_NULL, null=True)
    answered_at = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='answers')  # Добавлено поле ForeignKey для связи с Test

    def __str__(self):
        return f"Answer by {self.child.first_name} {self.child.last_name} to {self.question.text} in Test: {self.test.name}"


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
