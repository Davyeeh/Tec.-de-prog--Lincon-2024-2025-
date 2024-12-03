class Calculadora:
    def __init__(self) -> None:
        self.__acumulador = 0.0

    def soma(self, operando_a,  operando_b=None):
        self.__acumulador
        if operando_b is None:
            operando_b = self.__acumulador
        self.__acumulador = operando_a + operando_b
        return self.__acumulador

    def subtracao(self, operando_a,  operando_b=None):
        self.__acumulador
        if operando_b is None:
            operando_b = self.__acumulador
        self.__acumulador = operando_a - operando_b
        return self.__acumulador

    def multiplicacao(self, operando_a,  operando_b=None):
        self.__acumulador
        if operando_b is None:
            operando_b = self.__acumulador
        self.__acumulador = operando_a * operando_b
        return self.__acumulador

    def divisao(self, operando_a,  operando_b=None):
        self.__acumulador
        if operando_b is None:
            operando_b = self.__acumulador
        self.__acumulador = operando_a / operando_b
        return self.__acumulador
