# Faça um Programa que peça dois números e imprima a soma. 
# \n --> quebra de linha
# \t --> tabulação
n1 = input("Informe \tum número \n")
n2 = input("Informe outro número ")

#variáveis
# um espaço reservado na memória que você da um nome e guarda um valor. Quando precisar utilizar aquele valor guardado, você recupera através do nome da variável.
# utilize nomes significativos para variáveis, sendo JurosCompostos um nome melhor que jc

# Tipos de variáveis
# Python define automaticamente o tipo da variável de acordo com o conteúdo da variável
# Principais tipos
# - str --> string --> texto "Guto" "10" "10+10"
# - int --> integer --> número inteiro 10 
# - float --> ponto flutuante, casas decimais 10.7 
# - bool --> boolean --> booleano True ou False

# type()  --> comando para verificar o tipo da variável
# print(type(n1))

# toda entrada do teclado, mesmo digitando número, chega como STRING (texto), para a conta ser realizada, precisamos converter de string para algum tipo numérico
# str --> int --> int()
# str --> float --> float()
n1 = float(n1)
n2 = float(n2)

print(n1 + n2)