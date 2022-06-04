import os
frutas = ["maçã","laranja","morango"]

print(os.name)

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
"""
i = 0
limpar_tela()
while i < len(frutas):
    print(frutas[i])
    i += 1
"""
limpar_tela()
for fruta in frutas:
    print(fruta)

"""
limpar_tela()
for i in range(10,1,-1):
    print(i)
"""