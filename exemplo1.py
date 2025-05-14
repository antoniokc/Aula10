# Biblioteca para numeros aleatorios
import random
import os


os.system('cls')
# n = random.randint(1, 5)
# m = random.randint(1, 5)
# print(n, m)

# lst_numeros = [random.randint(1, 10) for i in range(5)]
# print(lst_numeros)


# Exemplo 02 - Função
def gerar_numeros(i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num


ini = int(input("infome o primeiro numero: "))
fin = int(input("infome o ultimo numero: "))
qtd = int(input("Quantos números? "))

numeros = gerar_numeros(ini, fin, qtd)
print(numeros)
