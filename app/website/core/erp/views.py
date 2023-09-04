from typing import Any, Dict
from django.shortcuts import render
from celery.result import AsyncResult
from .tasks import horario
import json
import random
from django.views.generic import ListView
from .models import Subject
from .forms import ScheduleForm

# Create your views here.
def Home(request):
    weekly_events = [
        {
            'title': 'Estructura de Datos 1',
            'daysOfWeek': [2,4],  # Lunes (0 para Domingo, 1 para Lunes, etc.)
            'startTime': '09:00:00',
            'endTime': '11:00:00',
            'color': 'orange',
        },
        {
            'title': 'Administración de Servidores',
            'daysOfWeek': [2,4],  # Lunes (0 para Domingo, 1 para Lunes, etc.)
            'startTime': '11:00:00',
            'endTime': '13:00:00',
            'color': 'dodgerblue',
        },
        {
            'title': 'Ingeniería de Software 2',
            'daysOfWeek': [3,5],  # Miércoles
            'startTime': '13:00:00',
            'endTime': '15:00:00',
            'color': 'darksalmon'
        },
        {
            'title': 'Minería de datos',
            'daysOfWeek': [6],  # Sabado
            'startTime': '07:00:00',
            'endTime': '11:00:00',
            'color': 'limegreen'
        },
        {
            'title': 'Inteligencia Artificial 1',
            'daysOfWeek': [3,5],  # Miércoles
            'startTime': '11:00:00',
            'endTime': '13:00:00',
            'color': 'Teal'
        },
       
    ]
    weekly_events = json.dumps(weekly_events)
    context = {'weeklyEvents':weekly_events, 'title':'Community Planner',
               'subtitle': 'Inicio'}
    
    return render(request,'base/welcome.html', context)

def celery_test(request):
    weekly_events = []

    resultado = horario.delay("202310", "INCO", ["I7040","I7032","I5890","I7038","I5888","I7041"],
                              {'I':[15,21], 'V':[15, 21], 'S':[7, 15]} )
    
    subjects = resultado.get()
    colors = []
    css_colors = [
        "#C44850", "#42BEB6", "#42BE78", "#5B38AF", "#C88FB1", "#F5B041 ",
        "#15AF5F", "#27AE60", "#797D7F", "#5B4636", "#5CC2B0", "#C8A2C8",
        "#5CA5C2" , "#2F4F4F", "#D8A27F", "#1AB0D0", "#C2BC6B", "#006400",
        "#2E8B57", "#91DF8F"
    ]

    for materia in subjects:
        event = { 'title': str,
            'daysOfWeek': [], #(0 para Domingo, 1 para Lunes, etc.)
            'startTime': str,
            'endTime': str,
            'color': str,}
        event['title'] = materia["nrc"]
        days, hours = extract_days_and_hours(materia["horas"])
        event['daysOfWeek'] = days
        event['startTime'] = hours[0]
        event['endTime'] = hours[1]
        event['color'] = choose_color(css_colors, colors)
        weekly_events.append(event)
    
    weekly_events = json.dumps(weekly_events)
    context = {'sesion':True, 'weeklyEvents':weekly_events, 'title':'Community Planner'}

    return render(request,'test/celery.html', context)

def extract_days_and_hours(dict_dh):
    week = {'L':1, 'M':2, 'I':3, 'J':4, 'V':5, 'S':6}
    days = []
    hours = []

    for day in list(dict_dh.keys()):
       days.append(week[day])
       d = dict_dh[day][0]
       minuto  = d[2:]
       hora_inicio = d[0:2] + ":" + minuto + ":" + "00"
       d = dict_dh[day][1] 
       minuto  = d[2:]
       hora_final = d[0:2] + ":" + minuto + ":" + "00" 
       hours += [hora_inicio, hora_final] 

    return days, hours

def choose_color(color, selected_colors):
    c = None
    while True:
        c = random.choice(color)
        if c not in selected_colors:
            break
    return c        


class SubjectList(ListView):
    model = Subject
    template_name = 'busqueda/subjects.html'
    context_object_name = 'materias'
    paginate_by = 12

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

def subject_test(request):
    materia = [{"materia": "Luis", "Clave": "1255"}, {"materia": "Rodrigo", "Clave": "1200"},
                {"materia": "Luis", "Clave": "1255"}]
    context = {'materias':materia}
    return render(request,'busqueda/subjects.html', context)

def test(request):
    return render(request, 'hector/Plantilla.html')

"""
def generador(request):

    context = {'title':'Generador de Horarios Inteligente','subtitle': 'Formulario'}

    return render(request, 'components/data-form.html', context)
"""

def generador(request):
    form = ScheduleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            Schedule=Schedule.save()
            carrera=carrera.save()
            ciclo=ciclo.save()
            materias = materias.save()
            lunes = lunes.save()
            inicioL = inicioL.save()
            finL = finL.save()
            martes = martes.save()
            inicioM = inicioM.save()
            finM = finM.save()
            miercoles = miercoles.save()
            inicioMi = inicioMi.save()
            finMi = finMi.save()
            jueves = jueves.save()
            inicioJ = inicioJ.save()
            finJ = finJ.save()
            viernes = viernes.save()
            inicioV = inicioV.save()
            finV = finV.save()
            sabado = sabado.save()
            inicioS = inicioS.save()
            finS = finS.save()
        else:
            form = ScheduleForm()
    context={'form':form,'title':'Generador de Horarios Inteligente','subtitle': 'Formulario'}
    return render(request, 'components/data-form.html', context)
