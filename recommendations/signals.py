from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from assistive_tech.models import (
    TecnologiaAssistiva,
    TA_Deficiencia,
    TA_Incapacidade,
    TA_Plataforma,
    TA_Contexto
)

from user.models import (
    Usuario,
    Usuario_Deficiencia,
    Usuario_Incapacidade,
    Usuario_Plataforma,
    Usuario_Preferencia
)

from .models import TAFeatureVector, UsuarioFeatureVector
from .utils import build_ta_feature_vector, build_usuario_feature_vector

def update_ta_vector(tecnologia):
    vector_data = build_ta_feature_vector(tecnologia)

    TAFeatureVector.objects.update_or_create(
        tecnologia=tecnologia,
        defaults={"vector": vector_data}
    )

@receiver(post_save, sender=TecnologiaAssistiva)
def create_or_update_ta_vector(sender, instance, **kwargs):
    update_ta_vector(instance)


@receiver([post_save, post_delete], sender=TA_Deficiencia)
def ta_deficiencia_changed(sender, instance, **kwargs):
    update_ta_vector(instance.tecnologia)


@receiver([post_save, post_delete], sender=TA_Incapacidade)
def ta_incapacidade_changed(sender, instance, **kwargs):
    update_ta_vector(instance.tecnologia)


@receiver([post_save, post_delete], sender=TA_Plataforma)
def ta_plataforma_changed(sender, instance, **kwargs):
    update_ta_vector(instance.tecnologia)


@receiver([post_save, post_delete], sender=TA_Contexto)
def ta_contexto_changed(sender, instance, **kwargs):
    update_ta_vector(instance.tecnologia)

# Para usuário

def update_usuario_vector(usuario):
    vector_data = build_usuario_feature_vector(usuario)

    UsuarioFeatureVector.objects.update_or_create(
        usuario=usuario,
        defaults={"vector": vector_data}
    )

@receiver(post_save, sender=Usuario)
def create_or_update_usuario_vector(sender, instance, **kwargs):
    update_usuario_vector(instance)

@receiver([post_save, post_delete], sender=Usuario_Deficiencia)
def usuario_deficiencia_changed(sender, instance, **kwargs):
    update_usuario_vector(instance.usuario)


@receiver([post_save, post_delete], sender=Usuario_Incapacidade)
def usuario_incapacidade_changed(sender, instance, **kwargs):
    update_usuario_vector(instance.usuario)


@receiver([post_save, post_delete], sender=Usuario_Plataforma)
def usuario_plataforma_changed(sender, instance, **kwargs):
    update_usuario_vector(instance.usuario)


@receiver([post_save, post_delete], sender=Usuario_Preferencia)
def usuario_preferencia_changed(sender, instance, **kwargs):
    update_usuario_vector(instance.usuario)