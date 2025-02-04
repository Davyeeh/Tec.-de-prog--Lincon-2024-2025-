from functools import reduce

# Produto de uma lista

# Lita de números
numeros = [1,2,3,4,5]

# Usano reduce e lambda pra calcular o produto de uma lista

produto = reduce(lambda x, y: x * y, numeros)

#Printando resultados
print(numeros)
print(produto)

print("==================================================")

# Maior número

# Lista numérica
numeros = [1, 10, 20, 500, 36]

# Usano reduce co lamba pra saber o maior numero de uma lista
maior_numero = reduce(lambda x, y: x if x > y else y, numeros)

# Printando resultao

print(numeros)
print(maior_numero)



print("==================================================")

# Contrução de um icionário

# Lista de tuplas
lista_tuplas = [("a", 1), ("b", 2), ("a", 3)]

# Usano reduce() junto á lamba ára criar umicionário somando os valores

resultado = reduce(lambda acc, curr: {**acc, curr[0]: acc.get(curr[0], 0) + curr[1]}, lista_tuplas, {})

# Printatno o rsultado
print(lista_tuplas)
print(resultado)