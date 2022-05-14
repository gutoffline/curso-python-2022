# Faça um Programa que leia três números e mostre o maior deles. 
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1>n2 and n1>n3:
    print("O número 1 é o maior")
elif n2>n1 and n2>n3:
    print("O número 2 é o maior")
else:
    print("O número 3 é o maior")