# construa uma estrutura que permita inseir nome e telefone de um cliente, exiba na tela essas informações com um código sequencial(1 ,2 ,3...) e pergunte se deseja cadastrar um novo cliente

novo = "s"
codigo = 1
while novo.lower() == "s":
    nome = input("Informe o nome do cliente: ")
    telefone = input("Informe o telefone do cliente: ")
    print("NOVO CLIENTE CADASTRADO")
    print("CÓDIGO: ", codigo)
    print("NOME: ", nome)
    print("TELEFONE: ", telefone)
    codigo += 1
    novo = input("Deseja incluir outro cliente? [S]im [N]ão: ")

print("PROGRAMA FINALIZADO")
