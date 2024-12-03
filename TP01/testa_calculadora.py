import calculadora as calc


def teste():
    resultado_soma = calc.soma(10, 5)
    print(f"{resultado_soma}")

    resultado_subtracao = calc.subtracao(10, 5)
    print(f"{resultado_subtracao}")

    resultado_multiplicacao = calc.multiplicacao(10, 5)
    print(f"{resultado_multiplicacao}")

    resultado_divisao = calc.divisao(10, 5)
    print(f"{resultado_divisao}")

    resultado_divisao_zero = calc.divisao(10, 0)
    print(f"{resultado_divisao_zero}")

    # Teste de memória

    resultado_memoria_1 = calc.soma(10, 5)
    print(f"{resultado_memoria_1}")

    resultado_memoria_2 = calc.subtracao(5)
    print(f"{resultado_memoria_2}")

    resultado_memoria_3 = calc.multiplicacao(2)
    print(
        f"{resultado_memoria_3}")

    resultado_memoria_4 = calc.divisao(4)
    print(f"{resultado_memoria_4}")

    resultado_memoria_5 = calc.divisao(0)
    print(f"{resultado_memoria_5}")


teste()
