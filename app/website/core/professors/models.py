from django.db import models

# Create your models here.

class Professor(models.Model):
    professor_id = models.AutoField(verbose_name='id profesor', db_column='professor_id', primary_key=True)
    name = models.CharField(max_length=40, verbose_name='nombre', db_column='name', null=False)
    global_knowledge = models.FloatField(
        null = True,
        db_column='g_knowledge',
        verbose_name='campo conocimiento',
        default=8.0
    )
    global_punctuality = models.FloatField(
        null = True,
        db_column='g_punctuality',
        verbose_name='campo puntualidad',
        default=8.0
    )
    global_difficult = models.FloatField(
        null = True,
        db_column='g_difficult',
        verbose_name='campo dificultad',
        default=8.0
    )
    global_dedication = models.FloatField(
        null = True,
        db_column='g_dedication',
        verbose_name='campo dedicacion',
        default=8.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        db_table = "Professor"