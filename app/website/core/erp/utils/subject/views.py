from django.views.generic import ListView, DetailView
from django.db.models import Avg
from .model import Subject
from ..evaluation.model import Evaluation
from ..evaluation.forms import ExperienceForm, RateForm, CommentForm

class SubjectDetail(DetailView):
    model = Subject
    template_name = 'subject/details.html'
    context_object_name = 'materia'

    def post(self, request, *args, **kwargs):
        mat = self.get_object()

        experience_form = ExperienceForm(request.POST, prefix='experience_form')
        comment_form = CommentForm(request.POST, prefix='comment_form')
        rate_form = RateForm(request.POST, prefix='rate_form')

        exist = Evaluation.objects.filter(user=self.request.user).first()

        if experience_form.is_valid() and 'submit_experience' in request.POST:
            if exist:
                exist.professor = experience_form.cleaned_data['professor']
                exist.learning = experience_form.cleaned_data['learning']
                exist.difficult = experience_form.cleaned_data['difficult']
                exist.punctuality = experience_form.cleaned_data['punctuality']
                exist.save()
            else:
                experience = experience_form.save(commit=False)
                experience.subject = mat
                experience.user = self.request.user
                experience.save()
            return self.get(request, *args, **kwargs)

        if comment_form.is_valid() and 'submit_comment' in request.POST:
            if exist:
                exist.comment = comment_form.cleaned_data['comment']
                exist.save()
            else:
                comment = comment_form.save(commit=False)
                comment.subject = mat
                comment.user = self.request.user
                comment.save()
            return self.get(request, *args, **kwargs)

        if rate_form.is_valid() and 'submit_rate' in request.POST:
            if exist:
                exist.complexity = rate_form.cleaned_data['complexity']
                exist.save()
            else:
                rate = rate_form.save(commit=False)
                rate.subject = mat
                rate.user = self.request.user
                rate.save()
            return self.get(request, *args, **kwargs)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Detalles"
        context['subtitle'] = "Materia"

        i = context['materia']
        i.count = Evaluation.objects.filter(subject=i).count()
        avg_complexity = Evaluation.objects.filter(subject=i).aggregate(avg_complexity=Avg('complexity'))
        i.avg = avg_complexity['avg_complexity'] if avg_complexity['avg_complexity'] is not None else "N/A"

        evaluations = Evaluation.objects.filter(subject=i)
        context['evaluacion'] = evaluations

        context['experience_form'] = ExperienceForm(prefix='experience_form')
        context['rate_form'] = RateForm(prefix='rate_form')
        context['comment_form'] = CommentForm(prefix='comment_form')

        return context
    
class SubjectList(ListView):
    model = Subject
    template_name = 'subject/explore.html'
    context_object_name = 'materias'
    paginate_by = 9

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
        for i in context['materias']:
            i.count = Evaluation.objects.filter(subject=i).count()
            avg_complexity = Evaluation.objects.filter(subject=i).aggregate(avg_complexity=Avg('complexity'))
            i.avg = avg_complexity['avg_complexity'] if avg_complexity['avg_complexity'] is not None else "N/A"
        return context