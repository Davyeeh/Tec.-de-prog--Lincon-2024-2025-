print('Soma simples')
#Criando a função
soma = lambda a, b: a + b

#Teste
print(soma(3, 5))
print(soma(10, 20))
print(soma(-1, 4))
print(soma(0, 0)) 

print('----------------')
print('Verificação de Paridade')
#Criando a função
verificacao_paridade = lambda num: num%2 ==- 0 # Verifica se um número é par

#Teste
print(verificacao_paridade(0))
print(verificacao_paridade(3))
print(verificacao_paridade(2))
print(verificacao_paridade(-2))

print('----------------')
print('Elevar ao quadrado')

#Criando uma lista para testar a função e criando a função
lista_numerica = [-2, 0, 4, 2, 6]
quadrado = map(lambda x: x^2, lista_numerica) #pode ser tbm x ** 2 para elevação ao quadrado

#Teste
print(list(quadrado))

print('----------------')
print('Composição de Funções')

#Criando as funções
celcius_para_fahrenheit  = lambda celcius: (celcius * 9/5) + 32
arredondar = lambda valor: round(valor)

#Compondo as funções
celcius_para_fahrenheit_arrendondar = lambda celcius: arredondar(celcius_para_fahrenheit(celcius))

#Lista de temeratuas em celcius
temperatura_celcius = [0, 0.6, 20, 32.5, 100]

#Convertendo as temperaturas
temperatura_convertidas = list(map(celcius_para_fahrenheit_arrendondar, temperatura_celcius))

#Teste
print(temperatura_convertidas)


