import random
total_numeros = 6
numeros_sorteados = []
for i in range(total_numeros):
    numero = (random.randint(1,60))
    while numero in numeros_sorteados:
        numero = (random.randint(1, 60))
    ##print(numero)
    numeros_sorteados.append(numero)
print()
print('Os números sorteados foram: ')
print(numeros_sorteados)
numeros = (numeros_sorteados)
numeros.sort()
print()
print('Números ordenados: ')
print(numeros)