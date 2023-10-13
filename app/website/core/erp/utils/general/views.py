from django.shortcuts import render, redirect
from ...tasks import horario
import json
import random
from ..schedule.forms import ScheduleForm

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
    context = {
        'weeklyEvents':weekly_events, 
        'title':'Community Planner',
        'subtitle': 'Inicio',
        'welcome':True
    }
    
    return render(request,'index.html', context)

def celery_test(request):
    weekly_events = []

    resultado = horario.delay("202310", "INCO", ["I7040","I7031","I5890","I7038","I5888","I7041"],
                              {'I':[15,21], 'V':[15, 21], 'S':[7, 15]} )
    
    subjects = resultado.get()
    colors = []
    css_colors = [
        "#C44850", "#42BEB6", "#42BE78", "#5B38AF", "#C88FB1", "#F5B041 ",
        "#15AF5F", "#27AE60", "#797D7F", "#5B4636", "#5CC2B0", "#C8A2C8",
        "#5CA5C2" , "#2F4F4F", "#D8A27F", "#1AB0D0", "#C2BC6B", "#006400",
        "#2E8B57", "#91DF8F"
    ]
    if subjects:
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
    else:
        message = "No hay un horario disponible :()"
        context = {'sesion': True, 'weeklyEvents': message}
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
            selected_colors.append(c)
            break
    return c        

def celery_worker(request, parameters):
    weekly_events = []
    data = json.loads(parameters)
    # resultado = horario.delay("202310", "INCO", ["I7040","I7031","I5890","I7038","I5888","I7041"],
                            #   {'I':[15,21], 'V':[15, 21], 'S':[7, 15]} )
    week = {'lunes': "L",
            'martes': "M",
            'miercoles': "I",
            'jueves': "J",
            'viernes': "V",
            'sabado': "S"}
    horas = {}
    ciclo = data["ciclo"]
    carrera = data["carrera"]
    materias = data["materias"].split(",")
    keys = list(data.keys())
    for index, key in enumerate(keys):
        if data[key] == True:
            horas[week[key]] = [ int(data[keys[index+1]]), int(data[keys[index+2]]) ]
    resultado = horario.delay(ciclo, carrera, materias, horas)
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
        event['title'] = str(f"{materia['topic']} - {materia['nrc']}")
        days, hours = extract_days_and_hours(materia["horas"])
        event['daysOfWeek'] = days
        event['startTime'] = hours[0]
        event['endTime'] = hours[1]
        event['color'] = choose_color(css_colors, colors)
        weekly_events.append(event)
    
    weekly_events = json.dumps(weekly_events)
    context = {'sesion':True, 'weeklyEvents':weekly_events, 'title':'Community Planner'}
    # context = {
    #     'title':'Recepcion de datos IA',
    #     'subtitle': subjects
    # }
    return render(request, 'test/celery.html', context)



def generador(request):
    form = ScheduleForm(request.POST)
    if request.method == 'POST':
        #form = ScheduleForm(request.POST)

        if form.is_valid():
            form_json = json.dumps(form.cleaned_data)

            return redirect('procesar', parameters=form_json) 

    context = {'form': form, 'title': 'Generador de Horarios Inteligente', 'subtitle': 'Formulario'}
    return render(request, 'components/data-form.html', context)
