from django.db import models

class Subject(models.Model):
    cve = models.AutoField(verbose_name='clave', db_column='CVE', primary_key=True, null=False)
    name = models.CharField(verbose_name='materia', db_column='Name', null=False, max_length=150)

    def __str__(self):
        return self.cve

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        db_table = "Subject"