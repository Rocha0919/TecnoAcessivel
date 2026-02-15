from django.db import models
from django.conf import settings
from tecnoAcessivel.utils import FEEDBACK_TYPE_CHOICES

class Feedback(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    tecnologia = models.ForeignKey('assistive_tech.TecnologiaAssistiva', on_delete=models.CASCADE, related_name='feedbacks')
    tipo = models.CharField(max_length=30, choices=FEEDBACK_TYPE_CHOICES, default='avaliacao')
    avaliacao = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True)
    eficaz = models.BooleanField(null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback u={self.usuario_id} ta={self.tecnologia_id}'
