# from rest_framework import routers
from . import views
from django.urls import path
from rest_framework import routers
from .api import StudentViewSet, TeacherViewSet,  MaterialViewSet, ChoiceViewSet, AssignmentViewSet, UserViewset, QuestionViewset, ScoreViewset, AncwerSerializer

router = routers.DefaultRouter()
router.register('student', StudentViewSet, 'Students')
router.register('users', UserViewset, 'Users')
router.register('teacher', TeacherViewSet, 'Teacher')
router.register('choice', ChoiceViewSet, 'Choice')
router.register('assignment', AssignmentViewSet, 'Assignment')
router.register('question', QuestionViewset, 'question')
router.register('ancwer', AssignmentViewSet, 'ancwer')
router.register('score', ScoreViewset, 'score')
router.register('material', MaterialViewSet, 'Material')

# urlpatterns = router.urls
urlpatterns = [
    path('students/', views.allstudents, name="all_students"),
    path('all/', views.kilakitu, name="all"),
    path('allassignments/', views.allass, name="allass"),
    path('studentme/<int:pk>/', views.specificstudent, name="specificstudent"),
    path('studentcls/<int:pk>/', views.specificstudentinclass,
         name="specificstudentinclass"),
    path('student/', views.addstudent, name="addstudent"),
    path('teachers/', views.allteachers, name="allteachers"),
    path('teacher/<str:pk>/', views.specificteacher, name="specificteacher"),
    path('teacher/', views.addteacher, name="addteacher"),
    path('add_material/', views.addmaterial, name='addmaterial'),
    path('material/<str:title>', views.getmaterial, name='getmaterial')
] + router.urls
