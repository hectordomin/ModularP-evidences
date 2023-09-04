from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Professor(models.Model):
    CHOICES = [ (6, "Muy malo"), (7, "Malo"), (8, "Regular"), (9, "Bueno"), (10, "Muy bueno")]
    VALIDATOR = [
        MinValueValidator(6, message="La puntuación debe ser igual o mayor a 6."),
        MaxValueValidator(10, message="La puntuación debe ser igual o menor a 10.")
    ]
    professor_id = models.AutoField(verbose_name='id_profesor', primary_key=True)
    name = models.CharField(max_length=40, verbose_name='nombre', null=False)
    knowledge = models.PositiveSmallIntegerField(verbose_name='conocimiento',default=8, validators=VALIDATOR, null=False, choices=CHOICES)
    punctuality = models.PositiveSmallIntegerField(verbose_name='puntualidad', default=8, validators=VALIDATOR, null=False, choices=CHOICES)
    difficult = models.PositiveSmallIntegerField(verbose_name='dificultad',default=8, validators=VALIDATOR, null=False, choices=CHOICES)
    following = models.PositiveSmallIntegerField(verbose_name='seguimiento', default=8, validators=VALIDATOR, null=False, choices=CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"
        db_table = "Professor"