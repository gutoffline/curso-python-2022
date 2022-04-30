# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Informe o valor do salário por hora: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
salario = valor_hora * horas_trabalhadas
print('O valor do salário mensal é', salario)