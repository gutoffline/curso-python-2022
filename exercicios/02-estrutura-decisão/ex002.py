#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

n = int(input("Informe um número: "))

if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Número é igual a zero")
