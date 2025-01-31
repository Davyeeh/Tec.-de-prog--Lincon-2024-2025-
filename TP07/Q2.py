import math

print('Converter para Maiúscula')
#Lista de palavras
palavras = ['python', 'lambda', 'map']

#Usando a função map()
maiusculas = map(lambda palavra: palavra.upper(), palavras)

#Teste
print(list(maiusculas))

print('----------')
print('Raiz quadrada')

#Lista numérica
numeros = [1,34,5,-4,10]

#Usando a função map()
quadrado = map(lambda x: math.sqrt(x), numeros)


#Teste
print(list(quadrado))
