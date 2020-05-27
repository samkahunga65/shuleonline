from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer, MaterialSerializer, QuestionSerializer, AncwerSerializer, ScoreSerializer, AssignmentSerializer, ChoiceSerializer, MissionSerializer
from .models import Student, Teacher, Material, Question, Ancwer, Score, Assignment, Choice, Mission


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'all_students': '/students/',
        'add_student': '/student/',
        'specific_student': '/student/<str:pk>/',
        'all_teachers': '/teachers/',
        'add_teacher': '/teacher/',
        'specific_teachers': '/teacher/<str:pk>/',
        'add_material': '/add_material/',
        'get_material': '/get_material/'
    }
    return Response(api_urls)


@api_view(['GET'])
def allstudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def allass(request):
    questions = Question.objects.all()
    assignments = Assignment.objects.all()
    scores = Score.objects.all()
    choices = Choice.objects.all()
    mission = Mission.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    serializer2 = AssignmentSerializer(assignments, many=True)
    serializer1 = ScoreSerializer(scores, many=True)
    serializer4 = ChoiceSerializer(choices, many=True)
    serializer5 = MissionSerializer(mission, many=True)
    serializer3 = {'assignments': [],
                   'questions': [], 'choices': [], "scores": [], 'mission': []}
    for i in serializer.data:
        serializer3['questions'].append(i)
    for i in serializer1.data:
        serializer3['scores'].append(i)
    for i in serializer2.data:
        serializer3['assignments'].append(i)
    for i in serializer4.data:
        serializer3['choices'].append(i)
    for i in serializer5.data:
        serializer3['mission'].append(i)
    return Response(serializer3)


@api_view(['GET'])
def kilakitu(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    serializer = StudentSerializer(students, many=True)
    serializer2 = TeacherSerializer(teachers, many=True)
    serializer3 = []
    for i in serializer.data:
        serializer3.append(i)
    for i in serializer2.data:
        serializer3.append(i)
    return Response(serializer3)


@api_view(['GET'])
def specificstudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def specificstudent(request, pk):
    student = Student.objects.get(owner=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def specificstudentinclass(request, pk):
    student = Student.objects.filter(darasa=pk)
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def classStudent(request, pk):
    darasa = 'darasa'
    student = Student.objects.get(darasa['darasa'] == pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def allteachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def specificteacher(request, pk):
    teachers = Teacher.objects.get(owner=pk)
    serializer = TeacherSerializer(teachers, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addstudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        print('yes')
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def addteacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def addmaterial(request):
    seriailizer = MaterialSerializer(data=request.data)
    if seriailizer.is_valid():
        seriailizer.save()

    return Response(f"{request.data.title} added!")


@api_view(['GET'])
def getmaterial(request, title):
    material = Material.objects.filter(title=title)
    serializer = MaterialSerializer(material, many=False)

    return Response(serializer.data)
