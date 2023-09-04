from django.db import models
#from django.forms import model_to_dict
from ..professors.models import Professor
from ..users.models import Student

class Schedule(models.Model):
    schedule_id = models.BigAutoField(verbose_name='id_horario', primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, verbose_name='id_estudiante')
    json_schedule = models.JSONField(verbose_name='horario_JSON', null=False)

    def __str__(self):
       return str(self.horario_id)
    
    def get_schedule(self):
        return self.json_schedule
    
    class Meta:
        verbose_name = "horario"
        verbose_name_plural = "horarios"
        db_table = "Schedule"


class Comment(models.Model):
    comment_id = models.BigAutoField(verbose_name='id_comentario', primary_key=True)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE, null=False, verbose_name='id_profesor')
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, verbose_name='id_estudiante')
    opinion = models.TextField(verbose_name='opinion', null=False)

    def __str__(self):
        return self.opinion

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"
        db_table = "Comment"


class Subject(models.Model):
    cve = models.AutoField(verbose_name='clave', primary_key=True, null=False)
    name = models.CharField(verbose_name='materia', null=False, max_length=150)
    professors = models.ManyToManyField(Professor)

    def __str__(self):
        return self.cve

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        db_table = "Subject"