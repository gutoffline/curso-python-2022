#Faça um Programa que verifique se uma letra digitada é "M" ou "N". Conforme a letra escrever: M - Manhã, N - Noite, Período inválido. 
periodo = input("Informe o período\n(M)Manhã\n(N)Noite\n")
periodo = periodo.upper()

if periodo == "M":
    print("Manhã")
elif periodo == "N":
    print("Noite")
else:
    print("Opção inválida")