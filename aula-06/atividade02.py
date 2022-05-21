from os import system
from datetime import date

def somar(n1,n2):
    total = float(n1) + float(n2)
    print(total)

def subtrair(n1, n2):
    total = float(n1) - float(n2)
    print(total)

def dividir(n1, n2):
    total = float(n1) / float(n2)
    print(total)

def multiplicar(n1, n2):
    total = float(n1) * float(n2)
    print(total)

def menu():
    system("cls")
    print("ESCOLHA A OPERAÇÃO QUE SERÁ EXECUTADA:")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    opcao = int(input("INFORME A OPÇÃO: "))
    return opcao
    
system("cls")
print(date.today())
num1 = input("Informe um número: ")
num2 = input("Informe outro número: ")

operacaoEscolhida = menu()
if operacaoEscolhida == 1:
    somar(num1, num2)
elif operacaoEscolhida == 2:
    subtrair(num1, num2)
elif operacaoEscolhida == 3:
    multiplicar(num1 , num2)
elif operacaoEscolhida == 4:
    dividir(num1, num2)
else:
    print("Operação inválida")