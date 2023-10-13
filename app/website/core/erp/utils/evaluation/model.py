from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ..user.model import User


class Evaluation(models.Model):
    evaluation_id = models.BigAutoField(verbose_name='evaluacion', db_column='evaluation', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='usuario', db_column='user')

    #AQUI HAY QUE PONERNOS DE ACUERDO EN LA PERSPECTIVA DEL ALUMNO
    # PESO A
    # PESO B
    # PESO C

    comment = models.TextField(verbose_name='comentario', db_column='comment', null=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "evaluacion"
        verbose_name_plural = "evaluaciones"
        db_table = "Evaluation"
