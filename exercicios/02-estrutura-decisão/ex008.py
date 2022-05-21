#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

produto1 = float(input("Informe o preço do produto 1: "))
produto2 = float(input("Informe o preço do produto 2: "))
produto3 = float(input("Informe o preço do produto 3: "))

if produto1 < produto2 and produto1 < produto3:
    print("Compre o produto 1.")
    print(produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("Compre o produto 2.")
    print(produto2)
else:
    print("Compre o produto 3.")
    print(produto3)