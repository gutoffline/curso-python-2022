idade = int(input("Informe sua idade: "))
if idade >= 18:
    print("Parabéns, você pode iniciar suas aulas de direção")
else:
    print("Você ainda não pode inicar conosco.")
    print("Volte em", 18-idade,"anos")