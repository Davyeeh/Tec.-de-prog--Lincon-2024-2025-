# Filtrar números positivos

#lista numérica
numeros =[-10, 15, -20, 25, 0, 30]

# Usando foler() com a função lambaa pra iltrar números poitivos
numeros_positivos= list(filter(lambda x: x > 0, numeros))

# Printando o resultdo
print(numeros)
print(numeros_positivos)

print("------------------------------------------------")

# Filtrar palavras curtas

#Lita de palavras 
palavras = ['Davi', 'Cão', 'Programação', 'Atividades']

# Uasando filter() com a função lambda para filtrar palavras maiores que 5 letras

palavras_curtas = list(filter(lambda x: len(x) > 5, palavras))

#printando o resultado
print(palavras)
print(palavras_curtas)

print("------------------------------------------------")

# Filtragem baseada em multiplas condições

# Çista numérica
numeros = [10, -5, 15 ,3 ,-9, 20, 7, 0, 30, -2]

# Função lamba para fo=iltrar multiplos de 3 ou e 5 e positivos
resultado = list(filter(lambda x: (x % 3 == 0 or x % 5 ==0) and x > 0, numeros))

# Printano o resultado
print(numeros)
print(resultado)
