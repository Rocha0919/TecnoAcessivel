from django.db import models
from tecnoAcessivel.utils import RECOMMENDATION_METHOD_CHOICES

class UsuarioFeatureVector(models.Model):
    usuario = models.OneToOneField('user.Usuario', on_delete=models.CASCADE, primary_key=True)
    vector = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Vector usuario {self.usuario_id}'


class TAFeatureVector(models.Model):
    tecnologia = models.OneToOneField('assistive_tech.TecnologiaAssistiva', on_delete=models.CASCADE, primary_key=True)
    vector = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Vector ta {self.tecnologia_id}'


class RecomendacaoLog(models.Model):
    usuario = models.ForeignKey('user.Usuario', on_delete=models.CASCADE, related_name='recomendacoes_log')
    tecnologia = models.ForeignKey('assistive_tech.TecnologiaAssistiva', on_delete=models.CASCADE, related_name='recomendacoes_log')
    snapshot_usuario = models.JSONField()
    score = models.FloatField()
    metodo = models.CharField(max_length=20, choices=RECOMMENDATION_METHOD_CHOICES, default='content-based')
    contexto = models.JSONField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Log {self.id} u={self.usuario_id} ta={self.tecnologia_id}'