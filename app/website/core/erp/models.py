from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ..professors.models import Professor
from ..users.models import User

class Schedule(models.Model):
    schedule_id = models.BigAutoField(verbose_name='id horario', db_column='schedule_id', primary_key=True)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='id estudiante', db_column='student_id')
    json_schedule = models.JSONField(verbose_name='horario_JSON', db_column='json_schedule', null=True)

    def __str__(self):
       return str(self.schedule_id)
    
    def get_schedule(self):
        return self.json_schedule
    
    class Meta:
        verbose_name = "horario"
        verbose_name_plural = "horarios"
        db_table = "Schedule"


class Evaluation(models.Model):
    K = [ (6, "... (6)"), (7, "No es su area (7)"), (8, "Regular (8)"), (9, "Le sabe (9)"), (10, "Eminencia (10)") ]
    P = [ (6, "Casi ni lo conozco (6)"), (7, "Llega muy tarde (7)"), (8, "Muy estricto con la hora de llegada (8)"), 
          (9, "Llega a tiempo"), (10, "Flexible '+- 10 minutos' (10)") ]
    DI = [ (6, "Peligro (6)"), (7, "Es complicado (7)"), (8, "Sencillo (8)"), (9, "Aceptable (9)"), (10, "Perfeccion (10)") ]
    DE = [ (6, "Nulo interes (6)"), (7, "Le cuesta explicar (7)"), (8, "Regular (8)"), 
           (9, "Volvería a tomar su clase (9)"), (10, "Experiencia religiosa (10)") ]
    VALIDATOR = [
        MinValueValidator(6, message="La puntuación debe ser igual o mayor a 6."),
        MaxValueValidator(10, message="La puntuación debe ser igual o menor a 10.")
    ]

    evaluation_id = models.BigAutoField(verbose_name='id evaluacion', db_column='evaluation_id', primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='id_usuario', db_column='user_id')
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE, null=False, verbose_name='id profesor', db_column='professor_id')

    knowledge = models.PositiveSmallIntegerField(verbose_name='conocimiento', db_column='knowledge', validators=VALIDATOR, null=True, choices=K)
    punctuality = models.PositiveSmallIntegerField(verbose_name='puntualidad', db_column='punctuality', validators=VALIDATOR, null=True, choices=P)
    difficult = models.PositiveSmallIntegerField(verbose_name='dificultad', db_column='difficult', validators=VALIDATOR, null=True, choices=DI)
    dedication = models.PositiveSmallIntegerField(verbose_name='dedicacion', db_column='dedication', validators=VALIDATOR, null=True, choices=DE)

    comment = models.TextField(verbose_name='comentario', db_column='comment', null=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "evaluacion"
        verbose_name_plural = "evaluaciones"
        db_table = "Evaluation"


class Subject(models.Model):
    cve = models.AutoField(verbose_name='clave', db_column='CVE', primary_key=True, null=False)
    name = models.CharField(verbose_name='materia', db_column='Name', null=False, max_length=150)

    def __str__(self):
        return self.cve

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        db_table = "Subject"