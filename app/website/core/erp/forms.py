from django import forms

class ScheduleForm(forms.Form):
    opciones_carrera = (
        ('INCE', 'INCE'),
        ('IGFO', 'IGFO'),
        ('INBI', 'INBI'),
        ('INRO', 'INRO'),
        ('INNI', 'INNI'),
        ('INCO', 'INCO'),
        ('INFO', 'INFO'),
        ('ICOM', 'ICOM'),
    )
    opciones_ciclo = (
        ('202410', '202410 - Calendario 24 A'),
        ('2023Z', '2023Z - Calendario 23Z Cuatrimestre'),
        ('2023Y', '2023Y - Calendario 23Y Cuatrimestre'),
        ('2023X', '2023X - Calendario 23X Cuatrimestre'),
    )
    opciones_inicio = (
        ('07:00', '07:00'),
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
    )
    opciones_fin = (
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
        ('20:00', '20:00'),
        ('21:00', '21:00'),
    )
    carrera = forms.ChoiceField(choices=opciones_carrera, label='Carrera')
    ciclo = forms.ChoiceField(choices=opciones_ciclo, label='Ciclo')
    materias = forms.CharField(max_length=50, label='Materias')
    lunes = forms.BooleanField(required=False, label='Lunes')
    inicioL = forms.ChoiceField(choices=opciones_inicio, label='Inicio')
    finL = forms.ChoiceField(choices=opciones_fin, label='Inicio')
    martes = forms.BooleanField(required=False, label='Martes')
    inicioM = forms.ChoiceField(choices=opciones_inicio, label='Inicio')
    finM = forms.ChoiceField(choices=opciones_fin, label='Inicio')
    miercoles = forms.BooleanField(required=False, label='Miercoles')
    inicioMi = forms.ChoiceField(choices=opciones_inicio, label='Inicio')
    finMi = forms.ChoiceField(choices=opciones_fin, label='Inicio')
    jueves = forms.BooleanField(required=False, label='Jueves')
    inicioJ = forms.ChoiceField(choices=opciones_inicio, label='Inicio')
    finJ = forms.ChoiceField(choices=opciones_fin, label='Inicio')
    Viernes = forms.BooleanField(required=False, label='Viernes')
    inicioV = forms.ChoiceField(choices=opciones_inicio, label='Inicio')
    finV = forms.ChoiceField(choices=opciones_fin, label='Inicio')
    sabado = forms.BooleanField(required=False, label='Sabado')
    inicioS = forms.ChoiceField(choices=opciones_inicio, label='Inicio')
    finS = forms.ChoiceField(choices=opciones_fin, label='Inicio')
    
    def save(self, commit=True):
        Schedule = super().save(commit=False)
        if commit:
            Schedule.save()
        return Schedule