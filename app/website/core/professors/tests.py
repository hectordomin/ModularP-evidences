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