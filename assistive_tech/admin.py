from django.contrib import admin
from .models import (
    Deficiencia,
    IncapacidadeFuncional,
    Plataforma,
    Preferencia,
    ContextoUso,
    TecnologiaAssistiva,
    TA_Deficiencia,
    TA_Incapacidade,
    TA_Plataforma,
    TA_Contexto
)

admin.site.register(Deficiencia)
admin.site.register(IncapacidadeFuncional)
admin.site.register(Plataforma)
admin.site.register(Preferencia)
admin.site.register(ContextoUso)
admin.site.register(TecnologiaAssistiva)

admin.site.register(TA_Deficiencia)
admin.site.register(TA_Incapacidade)
admin.site.register(TA_Plataforma)
admin.site.register(TA_Contexto)