from django.contrib import admin
from .models import (
    Usuario,
    Usuario_Deficiencia,
    Usuario_Incapacidade,
    Usuario_Plataforma,
    Usuario_Preferencia
)

admin.site.register(Usuario)

admin.site.register(Usuario_Deficiencia)
admin.site.register(Usuario_Incapacidade)
admin.site.register(Usuario_Plataforma)
admin.site.register(Usuario_Preferencia)