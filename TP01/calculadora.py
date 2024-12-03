acumulador = 0.0


def soma(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a + operando_b
    return acumulador


def subtracao(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a - operando_b
    return acumulador


def multiplicacao(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a * operando_b
    return acumulador


def divisao(operando_a, operando_b=None):
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    if operando_b == 0:
        return "Erro: Divisão por zero!"
    acumulador = operando_a / operando_b
    return acumulador
