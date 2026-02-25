import math

def cosine_similarity(vec1: dict, vec2: dict) -> float:
    common_keys = set(vec1.keys()) & set(vec2.keys())

    numerator = sum(vec1[k] * vec2[k] for k in common_keys)

    sum1 = sum(v ** 2 for v in vec1.values())
    sum2 = sum(v ** 2 for v in vec2.values())

    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator == 0:
        return 0.0

    return numerator / denominator