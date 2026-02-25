import unicodedata
import re
from .models import TAFeatureVector, UsuarioFeatureVector
from .similarity import cosine_similarity

def normalize_key(text):
    if not text:
        return ""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def build_ta_feature_vector(tecnologia):
    vector = {}

    for rel in tecnologia.ta_deficiencias.all():
        key = f"def_{normalize_key(rel.deficiencia.nome)}"
        vector[key] = 1

    for rel in tecnologia.ta_incapacidades.all():
        key = f"inc_{normalize_key(rel.incapacidade.nome)}"
        vector[key] = 1

    for rel in tecnologia.ta_plataformas.all():
        key = f"plataforma_{normalize_key(rel.plataforma.nome)}"
        vector[key] = 1

    for rel in tecnologia.ta_contextos.all():
        key = f"contexto_{normalize_key(rel.contexto.nome)}"
        vector[key] = 1

    if tecnologia.subtipo:
        key = f"subtipo_{normalize_key(tecnologia.subtipo)}"
        vector[key] = 1

    return vector

def build_usuario_feature_vector(usuario):
    vector = {}

    for rel in usuario.usuario_deficiencias.all():
        key = f"def_{normalize_key(rel.deficiencia.nome)}"
        vector[key] = 1

    for rel in usuario.usuario_incapacidades.all():
        key = f"inc_{normalize_key(rel.incapacidade.nome)}"
        vector[key] = 1

    for rel in usuario.usuario_plataformas.all():
        key = f"plataforma_{normalize_key(rel.plataforma.nome)}"
        vector[key] = 1

    for rel in usuario.usuario_preferencias.all():
        key = f"pref_{normalize_key(rel.preferencia.chave)}"
        vector[key] = 1

    if hasattr(usuario, "perfil") and usuario.perfil.contexto_principal:
        key = f"contexto_{normalize_key(usuario.perfil.contexto_principal)}"
        vector[key] = 1

    return vector

def recomendar_tas_para_usuario(usuario):
    try:
        u_vector = UsuarioFeatureVector.objects.get(usuario=usuario).vector
    except UsuarioFeatureVector.DoesNotExist:
        u_vector = {}

    resultados = []

    for ta_vector in TAFeatureVector.objects.select_related("tecnologia").all():
        score = cosine_similarity(u_vector, ta_vector.vector)

        matches = list(
            set(u_vector.keys()) & set(ta_vector.vector.keys())
        )

        resultados.append({
            "tecnologia": ta_vector.tecnologia,
            "score": round(score, 4),
            "matches": matches
        })

    resultados.sort(key=lambda x: x["score"], reverse=True)
    return resultados