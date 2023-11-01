from django.db import models

class Subject(models.Model):
    name = models.CharField(verbose_name='materia', db_column='name', null=False, max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        db_table = "subject"