from rest_framework import routers
from .api import StudentViewSet, TeacherViewSet, SubjectViewSet, DarasaViewSet, MaterialViewSet

router = routers.DefaultRouter()
router.register('api/students', StudentViewSet, 'Students')
router.register('api/teacher', TeacherViewSet, 'Teacher')
router.register('api/subject', SubjectViewSet, 'Subject')
router.register('api/darasa', DarasaViewSet, 'Darasa')
router.register('api/material', MaterialViewSet, 'Material')

urlpatterns = router.urls