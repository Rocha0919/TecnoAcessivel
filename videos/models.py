from django.db import models

class VideoTutorial(models.Model):
    tecnologia = models.ForeignKey('assistive_tech.TecnologiaAssistiva', on_delete=models.CASCADE, related_name='videos')
    youtube_video_id = models.CharField(max_length=50)
    titulo = models.CharField(max_length=300)
    descricao = models.TextField(blank=True)
    canal_id = models.CharField(max_length=100, blank=True)
    canal_nome = models.CharField(max_length=200, blank=True)
    idioma = models.CharField(max_length=10, blank=True)
    duracao_sec = models.IntegerField(null=True, blank=True)
    publicado_em = models.DateTimeField(null=True, blank=True)
    thumbnail_url = models.URLField(max_length=500, blank=True)
    relevancia = models.FloatField(default=0.0)
    fonte = models.CharField(max_length=255, blank=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo