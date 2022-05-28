salario = float(input("Informe o salário: "))
imposto = 27

while imposto > 0:
    imposto = input("Informe o valor do imposto ou S para  sair: ")
    if not imposto:
        imposto = 27
    elif imposto.isnumeric():
        imposto = float(imposto)
    elif imposto.upper() == "S":
        break
    else:
        imposto = 27

    if imposto > 0:
        print("IMPOSTO: ", imposto, "%")
        print("SALÁRIO: ", salario - (salario * ( imposto * 0.01)))