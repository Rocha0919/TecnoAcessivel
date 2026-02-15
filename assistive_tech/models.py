from django.db import models
from tecnoAcessivel.utils import ASSISTIVE_TECH_TYPE_CHOICES, COMPLEXITY_LEVEL_CHOICES, LICENSE_CHOICES

class Deficiencia(models.Model):
    codigo = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class IncapacidadeFuncional(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Preferencia(models.Model):
    chave = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class ContextoUso(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nome


class TecnologiaAssistiva(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=ASSISTIVE_TECH_TYPE_CHOICES)
    categoria_iso = models.CharField(max_length=20, blank=True, null=True)
    subtipo = models.CharField(max_length=80, blank=True)
    fabricante = models.CharField(max_length=150, blank=True)
    versao = models.CharField(max_length=50, blank=True)
    licenca = models.CharField(max_length=20, choices=LICENSE_CHOICES, default='gratuito')
    nivel_complexidade = models.CharField(max_length=10, choices=COMPLEXITY_LEVEL_CHOICES, default='medio')
    custo_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    idiomas_supported = models.CharField(max_length=200, blank=True)
    requisitos = models.TextField(blank=True)
    possui_video = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    fonte = models.CharField(max_length=255, blank=True)
    data_importacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class TA_Deficiencia(models.Model):
    tecnologia = models.ForeignKey(TecnologiaAssistiva, on_delete=models.CASCADE, related_name='ta_deficiencias')
    deficiencia = models.ForeignKey(Deficiencia, on_delete=models.CASCADE, related_name='def_tas')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['tecnologia','deficiencia'], name='ux_tecnologia_deficiencia')]
        verbose_name = 'TA x Deficiência'
        verbose_name_plural = 'TAs x Deficiências'

class TA_Incapacidade(models.Model):
    tecnologia = models.ForeignKey(TecnologiaAssistiva, on_delete=models.CASCADE, related_name='ta_incapacidades')
    incapacidade = models.ForeignKey(IncapacidadeFuncional, on_delete=models.CASCADE, related_name='inc_tas')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['tecnologia','incapacidade'], name='ux_tecnologia_incapacidade')]
        verbose_name = 'TA x Incapacidade'
        verbose_name_plural = 'TAs x Incapacidades'

class TA_Plataforma(models.Model):
    tecnologia = models.ForeignKey(TecnologiaAssistiva, on_delete=models.CASCADE, related_name='ta_plataformas')
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name='plataforma_tas')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['tecnologia','plataforma'], name='ux_tecnologia_plataforma')]
        verbose_name = 'TA x Plataforma'
        verbose_name_plural = 'TAs x Plataformas'

class TA_Contexto(models.Model):
    tecnologia = models.ForeignKey(TecnologiaAssistiva, on_delete=models.CASCADE, related_name='ta_contextos')
    contexto = models.ForeignKey(ContextoUso, on_delete=models.CASCADE, related_name='contexto_tas')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['tecnologia','contexto'], name='ux_tecnologia_contexto')]
        verbose_name = 'TA x Contexto'
        verbose_name_plural = 'TAs x Contextos'


TecnologiaAssistiva.deficiencias = models.ManyToManyField(
    Deficiencia, through=TA_Deficiencia, blank=True, related_name='tecnologias'
)
TecnologiaAssistiva.incapacidades = models.ManyToManyField(
    IncapacidadeFuncional, through=TA_Incapacidade, blank=True, related_name='tecnologias'
)
TecnologiaAssistiva.plataformas = models.ManyToManyField(
    Plataforma, through=TA_Plataforma, blank=True, related_name='tecnologias'
)
TecnologiaAssistiva.contextos = models.ManyToManyField(
    ContextoUso, through=TA_Contexto, blank=True, related_name='tecnologias'
)