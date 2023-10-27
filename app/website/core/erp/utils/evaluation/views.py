from django.views.generic import ListView
from .model import Evaluation

class SubjectDetail(ListView):
    model = Evaluation
    template_name = 'subject/details.html'
    context_object_name = 'evaluations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Detalles"
        context['subtitle'] = "Materia"
        return context