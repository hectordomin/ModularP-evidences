"""
URL configuration for planrcomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.erp.views import *
from core.professors.views import *
from core.users.views import *
#SubjectList.as_view()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='welcome'),
    path('inicio/', Home, name='welcome'),
    path('horario/', celery_test, name='celery'),
    path('materias/', SubjectList.as_view(),name='materias'),
    path('test/', test, name='pruebas'),
    path('profesor/<int:profesor_id>/', ProfeView.as_view(), name='biografia'),
    path('busqueda/', search, name='busqueda'),
    path('explorar/profesores/', ProfessorList.as_view(), name='explorar_profesores'),
    path('login/',login, name='login'),
    path('registro/',registro, name='registro'),
    path('generador/', generador, name='generador'),
    path('forgot_pwd/', forgot_pwd, name='fgtpwd'),
]
