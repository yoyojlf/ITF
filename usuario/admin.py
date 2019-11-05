from django.contrib import admin
from usuario.models import Usuario, TipoUsuario, Pregunta, Evaluacion, Departamento, EvaluacionPregunta, UsuarioEvaluacion
from usuario.forms import UsuarioFormAdm

# Register your models here.
class UserAdm(admin.ModelAdmin):
    form = UsuarioFormAdm


admin.site.register(Usuario, UserAdm)
admin.site.register(TipoUsuario)
admin.site.register(Pregunta)
admin.site.register(Evaluacion)
admin.site.register(Departamento)
admin.site.register(EvaluacionPregunta)
admin.site.register(UsuarioEvaluacion)


