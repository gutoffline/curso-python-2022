#from operacoes import soma
import operacoes
from menu import exibir_menu

exibir_menu()
opcao = input("Informe uma opção: ")
n1 = float(input("Informe o n1: "))
n2 = float(input("Informe o n2: "))
if opcao == "1":
    operacoes.soma(n1, n2)
elif opcao == "2":
    operacoes.subtrair(n1, n2)
elif opcao == "3":
    operacoes.dividir(n1, n2)
elif opcao == "4":
    operacoes.multiplicar(n1, n2)
else:
    print("Operação inválida")
