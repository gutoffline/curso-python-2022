#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 
#import os
from os import system

def mensagem():
    system("cls")
    print("PROGRAMA DE COMPARAÇÃO DE PREÇOS")
    print("================================")

mercado1 = input("Informe o nome do primeiro mercado: ")
produto1 = float(input("Informe o preço do produto 1: "))

mercado2 = input("Informe o nome do segundo mercado: ")
produto2 = float(input("Informe o preço do produto 2: "))

mercado3 = input("Informe o nome do terceiro mercado: ")
produto3 = float(input("Informe o preço do produto 3: "))

if produto1 < produto2 and produto1 < produto3:
    mensagem()
    print("Compre no mercado", mercado1, "pelo preço ", produto1)
elif produto2 < produto1 and produto2 < produto3:
    mensagem()
    print("Compre no mercado", mercado2, "pelo preço ", produto2)
elif produto3 < produto1 and produto3 < produto2:
    mensagem()
    print("Compre no mercado", mercado3, "pelo preço ", produto3)
else:
    mensagem()
    print("Os preços estão iguais, compre em qualquer lugar.")