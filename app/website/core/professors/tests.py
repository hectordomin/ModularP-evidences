from django.test import TestCase
import openpyxl
from .models import Professor  

# Create your tests here.

class test(TestCase):
    
    def populate_professors(self):
        data = "/home/devusr/project/ModularP-evidences/resources/data.xlsx"
        wb = openpyxl.load_workbook(data)
        sheet = wb.active

        for value in sheet.iter_rows(min_col=1, max_col=1, values_only=True):
            professor = Professor(name= value[0],)
            #print(value[0])
            professor.save()

        print("Tabla de profesores llenada éxitosamente")

    def add_professor(self):
        professor = Professor(
            name='Juan',
        )
        professor.save()
        print("Profesor creado exitosamente")

    def default_evaluate(self):
        profesores = Professor.objects.all()
        default_value = 8.0
        for registro in profesores:
            registro.global_knowledge = default_value
            registro.global_punctuality = default_value
            registro.global_difficult = default_value
            registro.global_dedication = default_value
            registro.save()

        print("\n Evaluaciones por default ingresadas en la poblacion de profesores")