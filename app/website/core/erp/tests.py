from django.test import TestCase
import openpyxl
from .models import Subject

# Create your tests here.

class testSubject(TestCase):
    
    def populate_subjects(self):
        data = "/home/devusr/project/ModularP-evidences/resources/data.xlsx"
        wb = openpyxl.load_workbook(data)
        sheet = wb.active

        for value in sheet.iter_rows(min_col=2, max_col=2, values_only=True):
            if value[0] != None:
                subject = Subject(name= value[0],)
                print(value[0])
                subject.save()

        print("\n Tabla de materias llenada éxitosamente")

    def add_subject(self):
        professor = Subject(
            name='Juan',
        )
        professor.save()
        print("Profesor creado exitosamente")