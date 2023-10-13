from django.views.generic import ListView, DetailView
from .model import Subject
from django.shortcuts import render, redirect


class SubjectDetail(DetailView):
    model = Subject
    template_name = 'busqueda/subjects.html'
    context_object_name = 'materias'

    
class SubjectList(ListView):
    model = Subject
    template_name = 'subject/explore.html'
    context_object_name = 'materias'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        if query:
            queryset = Subject.objects.filter(name__icontains=query)
        else:
            queryset = Subject.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Catálogo"
        context['subtitle'] = "Materias"
        context['search'] = self.request.GET.get('search_query', '')
        return context

def subject_test(request):
    materia = [{"materia": "Luis", "Clave": "1255"}, {"materia": "Rodrigo", "Clave": "1200"},
                {"materia": "Luis", "Clave": "1255"}]
    context = {'materias':materia}
    return render(request,'busqueda/subjects.html', context)