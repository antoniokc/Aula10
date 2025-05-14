# Criar calculadora

import random
# Biblioteca para limpar o console
import os


os.system('cls')


def somar(x, y):
    soma = x + y
    return soma


def subtrair(x, y):
    subtrai = x - y
    return subtrai


def multiplicar(x, y):
    multiplica = x * y
    return multiplica


def divisao(x, y):
    dividir = x / y
    return dividir


num1 = random.randint(1, 5)
num2 = random.randint(1, 5)


somar1 = somar(num1, num2)
subtrair1 = subtrair(num1, num2)
multiplicar1 = multiplicar(num1, num2)
divisao1 = divisao(num1, num2)

print(f"Os números gerados foram: {num1} e {num2}")

os = int(input(
    """Informe o número da operação desejada:
    \n 1 - soma 
    \n 2 - subtração 
    \n 3 - multiplicação 
    \n 4 - divisão

digite aqui: """
))
print(''*30)

if os == 1:
    print("Resultado da soma: ", somar1)
if os == 2:
    print("Resultado da subtração: ", subtrair1)
if os == 3:
    print("Resultado da multiplicação: ", multiplicar1)
if os == 4:
    print("Resultado da divisão: ", divisao1)
