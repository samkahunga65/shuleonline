from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer, MaterialSerializer, DarasaSerializer, DarasaStudentSerializer, StudentCircular
from .models import Student, Teacher, Material, Darasa
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
    serializer = StudentCircular(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def allclass(request):
    drs = Darasa.objects.all()
    serializer = DarasaSerializer(drs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def specificstudent(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def allteachers(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def specificteacher(request, pk):
    teachers = Teacher.objects.get(id=pk)
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
def addstudentcls(request):
    serializer = DarasaStudentSerializer(data=request.data)
    if serializer.is_valid():
        print('yes')
        serializer.save()
    print('no')

    return Response(serializer.data)


@api_view(['POST'])
def addclass(request):
    serializer = DarasaSerializer(data=request.data)
    if serializer.is_valid():
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
