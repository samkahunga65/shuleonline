from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Subject(models.Model):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.subject


class Darasa(models.Model):
    darasa = models.CharField(max_length=30)

    def __str__(self):
        return self.darasa


class Student(models.Model):
    # student_id = models.AutoField(primary_key=False)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number = PhoneNumberField(default=None, null=True)
    age = models.IntegerField(default=0)
    darasa = models.ForeignKey(
        Darasa, on_delete=models.CASCADE, related_name='darasa_student')

    def __str__(self):
        return f"{self.id}{self.fname}{self.lname} in class{self.darasa.darasa}"


class Teacher(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number = PhoneNumberField(default=None)
    age = models.IntegerField(default=0)
    darasa = models.ForeignKey(
        Darasa, on_delete=models.CASCADE, related_name='darasa_teacher')
    subjects = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='subjects_teacher')

    def __str__(self):
        return f"Mr/Ms {self.fname} teaches class:{self.darasa.darasa} {self.subjects.subject}"


class Material(models.Model):
    title = models.CharField(max_length=120, default='')
    text_books = models.FileField(upload_to='pdf', default=None, blank=True)
    homework = models.FileField(upload_to='pdf', default=None, blank=True)
    exams = models.FileField(upload_to='pdf', default=None, blank=True)
    notes = models.FileField(upload_to='pdf', default=None, blank=True)
    subjects = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='subjects_material')

    def __str__(self):
        return self.title
