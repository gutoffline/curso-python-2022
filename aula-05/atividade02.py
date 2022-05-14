"""
Nome, idade e email

os campos não podem estar em branco
nome ter mais de 3 caracteres
idade ser maior ou igual a 18 anos
email ter mais que 10 caracteres

"""

print("===== CADASTRO DE FUNCIONÁRIOS =====")
nome = input("Nome: ")
idade = input("Idade: ")
email = input("E-mail: ")

#validação nome
if nome == "":
    print("***O campo NOME é obrigatório")
elif len(nome) < 3:
    print("*** O campo NOME deve possuir mais de 3 caracteres.")

#validação da idade
if idade == "":
    print("*** O campo IDADE é obrigatório")
elif idade.isnumeric():
    idade = int(idade)
    if idade < 18:
        print("*** A IDADE deve ser maior que 18")
else:
    print("*** O campo IDADE deve ser número")

#validação do email
if email == "":
    print("*** O campo E-MAIL é obrigatório")
elif len(email) < 10:
    print("*** O e-mail precisa ter ao menos 10 caracteres")
elif email.count("@") != 1:
    print("O campo e-mail precisa ter um @")
