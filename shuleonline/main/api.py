from main.models import Student, Teacher, Subject, Darasa, Material
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, TeacherSerializer, SubjectSerializer, DarasaSerializer, MaterialSerializer

#viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = SubjectSerializer

class DarasaViewSet(viewsets.ModelViewSet):
    queryset = Darasa.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = DarasaSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = MaterialSerializer