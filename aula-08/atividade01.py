import os
#lista
frutas = ["maçã","laranja","morango","banana","melão", "melancia", "bacate"]

# print(len(frutas))
#print(frutas[6])
# alterando um item da lista
frutas[6] = "abacate"

# inserir item na lista
frutas.append("tomate")
frutas.insert(1,"pêra")
frutas.sort() #ordena em ordem alfabética
print(frutas)

#remover item da lista
frutas.remove("tomate")
# frutas.remove(frutas[8])

#adicionar tomate e uva
frutas.extend(["tomate","uva"])

#limpar a lista
frutas.clear()
os.system("cls")
contador = 0
while contador < len(frutas):
    print(frutas[contador])
    contador += 1
