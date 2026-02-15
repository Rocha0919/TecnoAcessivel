GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('Outro', 'Outro'),
    ('NaoInformado', 'Não informado'),
]

LEVEL_CHOICES = [
    ('baixo', 'Baixo'),
    ('medio', 'Médio'),
    ('alto', 'Alto'),
]

DISABILITY_DEGREE_CHOICES = [
    ('leve', 'Leve'),
    ('moderado', 'Moderado'),
    ('severo', 'Severo'),
]

ASSISTIVE_TECH_TYPE_CHOICES = [
    ('hardware', 'Hardware'),
    ('software', 'Software'),
    ('servico', 'Serviço'),
]

LICENSE_CHOICES = [
    ('gratuito', 'Gratuito'),
    ('freemium', 'Freemium'),
    ('pago', 'Pago'),
    ('open-source', 'Código aberto'),
]

COMPLEXITY_LEVEL_CHOICES = [
    ('baixo', 'Baixo'),
    ('medio', 'Médio'),
    ('alto', 'Alto'),
]

FEEDBACK_TYPE_CHOICES = [
    ('avaliacao', 'Avaliação'),
    ('usou', 'Usou'),
    ('nao_usou', 'Não usou'),
    ('recomendacao_aceita', 'Recomendação aceita'),
    ('rejeitada', 'Rejeitada'),
]

RECOMMENDATION_METHOD_CHOICES = [
    ('content-based', 'Baseado em conteúdo'),
    ('hybrid', 'Híbrido'),
    ('collaborative', 'Colaborativo'),
]