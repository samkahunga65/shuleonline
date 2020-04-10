# from rest_framework import routers
from . import views
from django.urls import path
# from .api import StudentViewSet, TeacherViewSet, SubjectViewSet, DarasaViewSet, MaterialViewSet

# router = routers.DefaultRouter()
# router.register('api/student', StudentViewSet, 'Students')
# router.register('api/teacher', TeacherViewSet, 'Teacher')
# router.register('api/subject', SubjectViewSet, 'Subject')
# router.register('api/darasa', DarasaViewSet, 'Darasa')
# router.register('api/material', MaterialViewSet, 'Material')

# urlpatterns = router.urls
urlpatterns = [
    path('students/', views.allstudents, name="all_students"),
    path('class/', views.allclass, name="allclass"),
    path('student/<str:pk>/', views.specificstudent, name="specificstudent"),
    path('student/', views.addstudent, name="addstudent"),
    path('studentcls/', views.addstudentcls, name="addstudentcls"),
    path('teachers/', views.allteachers, name="allteachers"),
    path('teacher/<str:pk>/', views.specificteacher, name="specificteacher"),
    path('teacher/', views.addteacher, name="addteacher"),
    path('add_material/', views.addmaterial, name='addmaterial'),
    path('material/<str:title>', views.getmaterial, name='getmaterial')
]
