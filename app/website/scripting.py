from planrcomm.asgi import *
import openpyxl
from core.erp.models import Subject
from core.professors.models import Professor

def populate_subjects():
    data = "/home/devusr/project/ModularP-evidences/resources/data.xlsx"
    wb = openpyxl.load_workbook(data)
    sheet = wb.active

    for value in sheet.iter_rows(min_col=2, max_col=2, values_only=True):
        if value[0] != None:
            subject = Subject(name= value[0],)
            #print(value[0])
            subject.save()

    print("\n Tabla de materias llenada éxitosamente")

def populate_professors():
    data = "/home/devusr/project/ModularP-evidences/resources/data.xlsx"
    wb = openpyxl.load_workbook(data)
    sheet = wb.active

    for value in sheet.iter_rows(min_col=1, max_col=1, values_only=True):
        professor = Professor(name= value[0],)
        #print(value[0])
        professor.save()

def default_evaluate():
    profesores = Professor.objects.all()
    default_value = 8.0
    for registro in profesores:
        registro.global_knowledge = default_value
        registro.global_punctuality = default_value
        registro.global_difficult = default_value
        registro.global_dedication = default_value
        registro.save()

    print("\n Evaluaciones por default ingresadas en la poblacion de profesores")
