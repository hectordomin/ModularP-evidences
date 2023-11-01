from django.db import models
from ..user.model import User
from ..subject.model import Subject
from ..professor.model import Professor

class Evaluation(models.Model):
    evaluation_id = models.BigAutoField(verbose_name='evaluacion', db_column='evaluation', primary_key=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='usuario', db_column='user')
    comment = models.TextField(verbose_name='comentario', db_column='comment', null=True)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, verbose_name='materia', db_column='subject')
    COMPLEXITY_CHOICES = [
        (6, 'Muy desafiante'),
        (7, 'Exigente'),
        (8, 'Moderadamente demandante'),
        (9, 'Manejable'),
        (10, 'Muy accesible'),
    ]
    complexity = models.IntegerField(choices=COMPLEXITY_CHOICES, null=True)
    
    professor = models.ForeignKey(Professor,  on_delete=models.CASCADE, null=True, verbose_name='profesor', db_column='professor')
    DIFFICULT_CHOICES = [
        (6, 'Altamente desafiante'),
        (7, 'Exigente'),
        (8, 'Moderado'),
        (9, 'Manejable'),
        (10, 'Muy asequible'),
    ]
    difficult = models.IntegerField(choices=DIFFICULT_CHOICES, null=True)
    PUNCTUALITY_CHOICES = [
        (6, 'Insatisfactorio'),
        (7, 'Regular'),
        (8, 'Aceptable'),
        (9, 'Muy bien'),
        (10, 'Excelente'),
    ]
    punctuality = models.IntegerField(choices=PUNCTUALITY_CHOICES, null=True)
    LEARNING_CHOICES = [
        (6, 'Poco enriquecedor'),
        (7, 'Mejorable'),
        (8, 'Aceptable'),
        (9, 'Positiva'),
        (10, 'Muy enriquecedor'),
    ]
    learning = models.IntegerField(choices=LEARNING_CHOICES, null=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "evaluacion"
        verbose_name_plural = "evaluaciones"
        db_table = "evaluation"
