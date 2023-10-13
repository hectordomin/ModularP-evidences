from django.db import models
from ..user.model import User

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