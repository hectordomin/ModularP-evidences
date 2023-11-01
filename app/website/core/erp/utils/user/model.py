from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(verbose_name='id usuario', db_column='user_id', primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='correo electronico', unique=True, null= False)
    is_superuser = None
    username = None
    career = models.CharField(verbose_name='carrera', db_column='career', null=False, max_length=30)
    json_tasks = models.JSONField(verbose_name='pendientes', db_column='json_tasks', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        db_table = "user"   