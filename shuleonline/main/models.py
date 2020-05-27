from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import User


class Student(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number = PhoneNumberField(default=None, null=True)
    age = models.IntegerField(default=0)
    owner = models.OneToOneField(
        User, related_name="student", on_delete=models.CASCADE, null=True)
    darasa = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}{self.fname}{self.lname} in class{self.darasa}"


class Teacher(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number = PhoneNumberField(default=None)
    age = models.IntegerField(default=0)
    owner = models.OneToOneField(
        User, related_name="teacher", on_delete=models.CASCADE, null=True)
    darasa = models.IntegerField(default=0)
    subjects = models.CharField(max_length=20)

    def __str__(self):
        return f"Mr/Ms {self.fname} teaches class:{self.darasa} {self.subjects}"


class Assignment(models.Model):
    title = models.CharField(max_length=120, null=True)
    darasa = models.IntegerField(default=0)
    educator = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=120)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    pub_date = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.question


class Ancwer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ancwer = models.CharField(max_length=120)


class Score(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    done = models.IntegerField(default=0)
    score = models.IntegerField(default=0)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, null=True, on_delete=models.CASCADE)
    is_ancwer = models.BooleanField(default=False, null=True)
    choice_text = models.CharField(max_length=120)

    def __str__(self):
        return self.choice_text


class Mission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)


class Material(models.Model):
    title = models.CharField(max_length=120, default='')
    text_books = models.FileField(upload_to='pdf', default=None, blank=True)
    homework = models.FileField(upload_to='pdf', default=None, blank=True)
    exams = models.FileField(upload_to='pdf', default=None, blank=True)
    notes = models.FileField(upload_to='pdf', default=None, blank=True)
    subjects = models.CharField(max_length=20)

    def __str__(self):
        return self.title
