from main.models import Student, Teacher, Material, Assignment, Choice, Question, Ancwer, Score, Mission
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, TeacherSerializer, MaterialSerializer, AssignmentSerializer, ChoiceSerializer, UserSerializer, AncwerSerializer, QuestionSerializer, ScoreSerializer, MissionSerializer
from accounts.models import User


class MissionViewset(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    permission_classes = {
        permissions.IsAuthenticated
    }
    serializer_class = MissionSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = {
        permissions.IsAuthenticated
    }
    serializer_class = UserSerializer


class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = {
        permissions.IsAuthenticated
    }
    serializer_class = QuestionSerializer


class AncwerViewset(viewsets.ModelViewSet):
    queryset = Ancwer.objects.all()
    permission_classes = {
        permissions.IsAuthenticated
    }
    serializer_class = AncwerSerializer


class ScoreViewset(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    permission_classes = {
        permissions.IsAuthenticated
    }
    serializer_class = ScoreSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    permission_classes = {
        permissions.IsAuthenticated

    }
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = TeacherSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = MaterialSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = AssignmentSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    permission_classes = {
        permissions.AllowAny
    }
    serializer_class = ChoiceSerializer
