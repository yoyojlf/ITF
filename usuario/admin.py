from django.contrib import admin
from usuario.models import Usuario, TipoUsuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
