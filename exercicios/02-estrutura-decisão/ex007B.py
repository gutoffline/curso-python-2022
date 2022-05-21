#Faça um Programa que leia três números e mostre o maior e o menor deles. 

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print("Maior: ", maior)
print("Menor: ", menor)