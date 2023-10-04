from django.shortcuts import render, redirect
from .forms import UserForm, StudentForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import LoginForm

class MyLogin(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = 'welcome'

def registro(request):
    form = UserForm(request.POST or None)
    student_form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and student_form.is_valid():
            user = form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()

            messages.success(request,'La cuenta ha sido creada con exito')
            return redirect('welcome')
    context = {'form':form, 'student_form':student_form,'title':'Registrar','subtitle': 'Nuevo usuario',
    'list_url': reverse_lazy('inquilino_list'),'action': 'add'}
    return render(request, 'users/register.html', context)

def forgot_pwd(request):
    return render(request, 'users/fgtpwd.html')

