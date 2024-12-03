import matematica as mat
from matematica.estatistica import media


def teste():
    a = 10
    b = 5
    c = [20, 108, 49, 5, 83, 62]

    # Teste aritimética
    resultado_soma = mat.soma(a, b)
    resultado_sub = mat.sub(a, b)

    # Teste geometria
    resultado_area_circulo = mat.area_circulo(a)
    resultado_area_retangulo = mat.area_retangulo(a, b)

    # Teste do subpacote de estatistica (média)
    media_lista = media.calcular_media_simples(c)

    print(f'{a} + {b} = {resultado_soma}')
    print(f'{a} - {b} = {resultado_sub}')
    print(f'A área do circulo de raio {a} é {resultado_area_circulo}')
    print(f'A área do retângulo de base {a} e altura {b} é {resultado_area_retangulo}')
    print(f'A média simples da lista {c} é {media_lista}')


teste()
