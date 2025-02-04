# Gerador de Pares

def gerador_pares():
    for num in range(1, 50):
        if num % 2 == 0:
            yield num

# Usando o gerador para exibir o numeros pares

for par in gerador_pares():
    print(par)

print("==================================================")

# Soma de Quadrados com Expressão Geradora

# oma e quadrado com expressão geradora

soma_quadrados = sum(x**2 for x in range (1, 11))

# Printando o resultado

print(soma_quadrados)

print("==================================================")

# Gerador de Sequência Infinita

def gerador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Exibindo os primeiros 10 números da sequência de Fibonacci
fibonacci = gerador_fibonacci()
for _ in range(10):
    print(next(fibonacci))

print("==================================================")

# Gerador Personalizado de Números Primos

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gerador_primos(start, end):
    for num in range(start, end + 1):
        if eh_primo(num):
            yield num

# Testando o gerador imprimindo os números primos no intervalo de 10 a 50
for primo in gerador_primos(10, 50):
    print(primo)

print("==================================================")

# Gerador Infinito com Condição de Parada

def gerador_fibonacci_limite(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a, b = b, a + b

# Testando o gerador com limite de 10.000
for num in gerador_fibonacci_limite(10000):
    print(num)
