from apps.core.models import BaseModel
from apps.users.models import User

from django.db import models


class Patient(BaseModel):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Masculino'
        FEMALE = 'female', 'Feminino'
        OTHER = 'other', 'Outro'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nome completo', max_length=255)
    document = models.CharField('Nº Documento', max_length=20)
    birth_date = models.DateField('Data de nascimento')
    gender = models.CharField('Sexo', max_length=10, choices=GenderChoices.choices)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.name
