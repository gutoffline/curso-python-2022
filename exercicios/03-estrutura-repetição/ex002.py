#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
# Imprime os numeros um abaixo do outro
for i in range(1, 21):
    print(i)

# Imprime os numeros um ao lado do outro
numeros = ""
for i in range(1, 21):
    numeros += str(i)
print(numeros)