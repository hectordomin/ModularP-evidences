from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student (models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, null=False, verbose_name='id_usuario')
    career = models.CharField(verbose_name='carrera', null=False, max_length=30)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"
        db_table = "Student"  