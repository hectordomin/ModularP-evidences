from django.shortcuts import render, redirect
from .forms import UserForm
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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'La cuenta ha sido creada con exito')
            return redirect('welcome')
    context = {'form':form,'title':'Registrar','subtitle': 'Nuevo usuario','action': 'add'}
    return render(request, 'users/register.html', context)

def forgot_pwd(request):
    return render(request, 'users/fgtpwd.html')

def disclaimer(request):
    return render(request, 'users/disclaimer.html')