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
from django.contrib.auth import views as auth_views

urlpatterns = [

    # INICIO
    path('admin/', admin.site.urls),
    path('', Home, name='welcome'),
    path('inicio/', Home, name='welcome'),
    path('disclaimer/', disclaimer, name='disclaimer'),

    #MATERIAS
    path('catalogo/', SubjectList.as_view(),name='materias'),
    path('catalogo/<int:pk>/<str:name>/', SubjectDetail.as_view() ,name='evaluacion'),

    # OTROS
    path('horario/', celery_worker, name='celery'),


    #IA GENERATOR
    path('generador/', generador, name='generador'),
    path('generador/proceso/<str:parameters>/', celery_worker, name='procesar'),

    #USUARIO
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='welcome'), name='logout'),
    path('forgot_pwd/', forgot_pwd, name='fgtpwd'),
    path('registro/', registro, name='registro'),
]
