from django.contrib import admin
from usuario.models import Usuario, TipoUsuario, Pregunta, Evaluacion, Departamento, EvaluacionPregunta, UsuarioEvaluacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Pregunta)
admin.site.register(Evaluacion)
admin.site.register(Departamento)
admin.site.register(EvaluacionPregunta)
admin.site.register(UsuarioEvaluacion)


