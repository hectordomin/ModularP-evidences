from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Professor
from ..erp.forms import EvaluationForm, CommentForm
from ..erp.models import Evaluation


# Create your views here.


class ProfeView(DetailView):
    model = Professor
    template_name = 'profesor/profe_view.html'
    context_object_name = 'profesor'  # Esto define el nombre con el que se accederá al objeto en el template
    form_class = EvaluationForm  # Agrega tu formulario aquí si es necesario

    def get_object(self, queryset=None):
        profesor_id = self.kwargs.get('pk')
        objeto = Professor.objects.get(pk=profesor_id)
        return objeto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Detalles"
        context['subtitle'] = "Profesor"
        professor = self.get_object()
        evaluacion = Evaluation.objects.filter(professor_id = professor)
        context['evaluacion'] = evaluacion
        context['form'] = self.form_class()
        context['comment_form'] = CommentForm()
        return context


    def post(self, request, *args, **kwargs):
        profesor = self.get_object()
        user = self.request.user
        form = self.form_class(request.POST or None)
        comment_form = CommentForm(request.POST or None)
        exist = Evaluation.objects.filter(professor_id=profesor.professor_id, user_id=user.id).first()
        if form.is_valid():
            if exist:
                exist.dedication = form.cleaned_data['dedication']
                exist.difficult = form.cleaned_data['difficult']
                exist.punctuality = form.cleaned_data['punctuality']
                exist.knowledge = form.cleaned_data['knowledge']
                exist.save()
            else:
                # Creamos una instancia de Evaluation relacionada con el profesor y el usuario
                evaluation = form.save(commit=False)
                evaluation.professor_id = profesor
                evaluation.user_id = user
                evaluation.save()
        exist = Evaluation.objects.filter(professor_id=profesor.professor_id, user_id=user.id).first()
        if comment_form.is_valid():
            if exist:
                exist.comment = comment_form.cleaned_data['comment']
                exist.save()
            else:
                # Creamos una instancia de Evaluation relacionada con el profesor y el usuario
                comment = comment_form.save(commit=False)
                comment.professor_id = profesor
                comment.user_id = user
                comment.save()
        
        return redirect('biografia', pk=profesor.professor_id)

class ProfessorList(ListView):
    model = Professor
    template_name = 'busqueda/professor.html'
    context_object_name = 'profes'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            queryset = Professor.objects.filter(name__icontains=query)
        else:
            queryset = Professor.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Explorar'
        context['subtitle'] = 'Profesores'
        context['search'] = self.request.GET.get('search_query', '')
        profesores = context['profes']
        for registro in profesores:
            registro.promedio = (registro.global_knowledge + registro.global_punctuality + registro.global_difficult + registro.global_dedication) / 4
        return context


