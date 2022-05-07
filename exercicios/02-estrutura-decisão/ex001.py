#Faça um Programa que peça dois números e imprima o maior deles. 
n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

if n1 > n2:
    print("Número 1 é o maior")
else:
    if n1 == n2:
        print("Os números são iguais")
    else:
        print("Número 2 é o maior")

