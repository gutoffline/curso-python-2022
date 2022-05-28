"""
contador = 1
while contador <= 5:
    print("Contando", contador)
    #contador = contador + 1 #incremento
    contador += 1

print(contador)
print("Laço terminou")


aulas = 1 
while aulas <= 9:
    print("CURSO PYTHON - AULA ", aulas)

    if aulas == 1:
        print("Introdução ao Python")
    elif aulas == 2:
        print("Operadores e variáveis")
    elif aulas == 3:
        print("Estrutura de decisão")
    elif aulas == 4:
        print("Exercícios")
    elif aulas == 5:
        print("Validações")
    elif aulas == 6:
        print("Funções")
    elif aulas == 7:
        print("Funções e estrutura de repetição")
    elif aulas == 8:
        print("Salvando arquivo e lendo sites")
    elif aulas == 9:
        print("Classes e exercícios")
    aulas += 1

"""
imposto = int(input("Informe o valor do imposto entre 0 e 100: "))

while imposto < 0 or imposto > 100:
    print("Valor inválido")
    imposto = int(input("Informe o valor do imposto entre 0 e 100: "))

print("Imposto: ", imposto)