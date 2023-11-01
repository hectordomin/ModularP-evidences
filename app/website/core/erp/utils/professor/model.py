from django.db import models

class Professor(models.Model):
    name = models.CharField(verbose_name='profesor', db_column='name', null=False, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        db_table = "professor"