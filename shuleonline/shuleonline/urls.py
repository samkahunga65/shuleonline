from django.contrib import admin
from django.urls import path, include
from frontend.views import index

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include('main.urls')),
    path('api/', include('accounts.urls')),
    path('admin/', admin. site. urls),
    path('', index, name='index')
]
