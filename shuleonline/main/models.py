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
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number =  PhoneNumberField(default=None, null=True)
    age = models.IntegerField(default=0)
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE, related_name='darasa_student')
    def __str__(self):
        return f"{self.fname}{self.lname}"
    

class Teacher(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number =  PhoneNumberField(default=None)
    age = models.IntegerField(default=0)
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE, related_name='darasa_teacher')
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects_teacher')

    def __str__(self):
        return f"Mr/Ms{self.fname}"
    


class Material(models.Model):
    text_books = models.FileField(upload_to='pdf')
    homework = models.FileField(upload_to='pdf')
    exams = models.FileField(upload_to='pdf')
    notes = models.FileField(upload_to='pdf')
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects_material')


    

    
