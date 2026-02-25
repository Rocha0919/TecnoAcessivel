from django.contrib import admin
from .models import UsuarioFeatureVector, TAFeatureVector, RecomendacaoLog

admin.site.register(UsuarioFeatureVector)
admin.site.register(TAFeatureVector)
admin.site.register(RecomendacaoLog)