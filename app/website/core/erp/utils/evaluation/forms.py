from django import forms
from .model import Evaluation

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['professor', 'difficult', 'punctuality',
                  'learning']
        widgets = {
            'professor': forms.Select(attrs={'class': 'form-control select2', 'id': 'profesorSelect'}),
            'difficult': forms.Select(attrs={'class': 'form-control select2 select2-secondary', 'data-dropdown-css-class': 'select2-secondary', 'style': 'width: 100%;', 'id': 'dificultadSelect', 'disabled': 'disabled'}),
            'punctuality': forms.Select(attrs={'class': 'form-control select2 select2-secondary', 'data-dropdown-css-class': 'select2-secondary', 'style': 'width: 100%;', 'id': 'puntualidadSelect', 'disabled': 'disabled'}),
            'learning': forms.Select(attrs={'class': 'form-control select2 select2-secondary', 'data-dropdown-css-class': 'select2-secondary', 'style': 'width: 100%;', 'id': 'aprendizajeSelect', 'disabled': 'disabled'}),
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['complexity']
        widgets = {
            'complexity': forms.Select(attrs={'class': 'form-control select2 select2-secondary', 'data-dropdown-css-class': 'select2-secondary', 'style': 'width: 100%;'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control','rows': 2, 'type':'text', 'name':'message', 'placeholder': 'Tomé este curso con Carlos Alberto Guzman Montes, me pareció un profe a todo dar, es relajado y ...'}),
        }