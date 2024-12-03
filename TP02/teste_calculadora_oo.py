from calculadora_oo import Calculadora


def teste():
    calc = Calculadora()

    print(f'{2} + {1} = {calc.soma(2, 1)}')
    print(f'{2} - {1} = {calc.subtracao(2, 1)}')
    print(f'{2} * {1} = {calc.multiplicacao(2, 1)}')
    print(f'{2} / {1} = {calc.divisao(2, 1)}')

    print('Teste de memória')

    print(f'{calc.soma(2, 1)} + {2} = {calc.soma(2)}')
    print(f'{calc.subtracao(2, 1)} - {2} = {calc.subtracao(2)}')
    print(f'{calc.multiplicacao(2, 1)} * {2} = {calc.multiplicacao(2)}')
    print(f'{calc.divisao(2, 1)} / {2} = {calc.divisao(2)}')


teste()
