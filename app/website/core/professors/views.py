from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Professor


# Create your views here.
def profesor_v(request, profesor_id):
    profesor = get_object_or_404(Professor, pk=profesor_id)
    return render(request, 'profesor/profe_view.html', {'profesor': profesor})

class ProfeView(ListView):
    model=Professor
    template_name='profesor/profe_view.html'
    context_object_name='profesor'

    def get_queryset(self):
        # Obtén el profesor específico por su ID
        profesor_id = self.kwargs['profesor_id']
        return Professor.objects.filter(pk=profesor_id)

    def get_context_data(self, **kwargs):
        profesor = self.get_queryset()
        context = super().get_context_data(**kwargs)
        context['Profesor'] = context['profesor'][0]
        return context

class ProfessorList(ListView):
    model = Professor
    template_name = 'busqueda/professor.html'
    context_object_name = 'professors'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Explorar'
        context['subtitle'] = 'Profesores'
        pairs = []
        for i in range (int(len(context['professors'])/2)):
            pairs.append((context['professors'][i+(1*i)], context['professors'][i+1+(1*i)]))
        context['pairs'] = pairs
        #context['list_url'] = reverse_lazy('vivienda_list')
        return context

def search(request):
    context = {'sesion':False, 'topic':'Guia de profesores'}
    return render(request, 'base/listing.html', context)

