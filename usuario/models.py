from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TipoUsuario(models.Model):
    name = models.CharField(max_length=50,blank=False)
    description = models.CharField(max_length=100,blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

#Se agrega tabla de departamento
class Departamento(models.Model):
    name = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Usuario(AbstractUser):
    rut = models.CharField(max_length=11,blank=True)
    birthday = models.DateField(auto_now_add=True,blank=True)
    address = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=12,blank=True)
    bio = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tipo_usuario = models.ForeignKey(TipoUsuario,null=True,blank=True,on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.username

#Se añade tabla Pregunta
class Pregunta(models.Model):
    question = models.CharField(max_length=100,blank=True)
    max_score = models.FloatField(blank=True)
    min_score = models.FloatField(blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.question

#Se añade tabla Evaluacion
class Evaluacion(models.Model):
    acum_score = models.FloatField(blank=True)
    evaluator = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.DO_NOTHING)
    def __str__(self):
        return "Puntaje Acumulado: {0}".format(self.acum_score)

class UsuarioEvaluacion(models.Model):
    user = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.DO_NOTHING)
    evaluation = models.ForeignKey(Evaluacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    def __str__(self):
        return "Evaluado: {0} Puntaje Acumulado: {1}".format(self.user.get_full_name(),self.evaluation.acum_score)

class EvaluacionPregunta(models.Model):
    evaluation = models.ForeignKey(Evaluacion, null=True, blank=True, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Pregunta, null=True, blank=True, on_delete=models.DO_NOTHING)
    score = models.FloatField(blank=True)
    def __str__(self):
        return "Pregunta: {0} Puntaje: {1}".format(self.question.question, self.score)

