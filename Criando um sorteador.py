import random
total_numeros = 6
numeros_sorteados = []
for i in range(total_numeros):
    numero = (random.randint(1,60))
    while numero in numeros_sorteados:
        numero = (random.randint(1, 60))
    ##print(numero)
    numeros_sorteados.append(numero)
print(numeros_sorteados)
