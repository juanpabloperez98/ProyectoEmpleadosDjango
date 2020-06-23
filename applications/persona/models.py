from django.db import models

from applications.departamento.models import Departamento

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','Contador'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),        
    )
    first_name = models.CharField('Primer Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    jobs = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to='empleado', blank=True, null = True)
    habilidades = models.ManyToManyField(Habilidades)


    def __str__(self):
        return self.first_name + ' ' + self.last_name

