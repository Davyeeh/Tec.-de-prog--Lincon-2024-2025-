def calcular_media_simples(numeros):
    if not numeros:
        return None
    soma = sum(numeros)
    tamanho = len(numeros)
    media = soma / tamanho
    return media
