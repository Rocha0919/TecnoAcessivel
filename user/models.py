from django.db import models
from tecnoAcessivel.utils import DISABILITY_DEGREE_CHOICES, GENDER_CHOICES, LEVEL_CHOICES

class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    consentimento_dados = models.BooleanField(default=False)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, choices=GENDER_CHOICES, default='NaoInformado')
    nivel_tecnologico = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='medio')
    orcamento = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='medio')
    idioma_preferido = models.CharField(max_length=10, default='pt-BR')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
class Usuario_Deficiencia(models.Model):
    usuario = models.ForeignKey('user.Usuario', on_delete=models.CASCADE, related_name='usuario_deficiencias')
    deficiencia = models.ForeignKey('assistive_tech.Deficiencia', on_delete=models.CASCADE, related_name='usuario_deficiencias')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['usuario','deficiencia'], name='ux_usuario_deficiencia')]
        verbose_name = 'Usuário x Deficiência'

class Usuario_Incapacidade(models.Model):
    usuario = models.ForeignKey('user.Usuario', on_delete=models.CASCADE, related_name='usuario_incapacidades')
    incapacidade = models.ForeignKey('assistive_tech.IncapacidadeFuncional', on_delete=models.CASCADE, related_name='usuario_incapacidades')
    grau = models.CharField(max_length=10, choices=DISABILITY_DEGREE_CHOICES, default='moderado')
    observacao = models.TextField(blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['usuario','incapacidade'], name='ux_usuario_incapacidade')]
        verbose_name = 'Usuário x Incapacidade'

class Usuario_Plataforma(models.Model):
    usuario = models.ForeignKey('user.Usuario', on_delete=models.CASCADE, related_name='usuario_plataformas')
    plataforma = models.ForeignKey('assistive_tech.Plataforma', on_delete=models.CASCADE, related_name='usuario_plataformas')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['usuario','plataforma'], name='ux_usuario_plataforma')]
        verbose_name = 'Usuário x Plataforma'

class Usuario_Preferencia(models.Model):
    usuario = models.ForeignKey('user.Usuario', on_delete=models.CASCADE, related_name='usuario_preferencias')
    preferencia = models.ForeignKey('assistive_tech.Preferencia', on_delete=models.CASCADE, related_name='usuario_preferencias')
    valor = models.CharField(max_length=200, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['usuario','preferencia'], name='ux_usuario_preferencia')]
        verbose_name = 'Usuário x Preferência'

