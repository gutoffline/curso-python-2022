import os
import socket
import platform

nome_computador = socket.gethostname()
so = platform.system()
ip = socket.gethostbyname(nome_computador)

print(nome_computador, so, ip)

nome = ""
while nome == "":
    nome = input("Informe seu nome: ")

departamento = ""
while departamento == "":
    departamento = input("Informe seu departamento: ")

#ESCREVENDO UM ARQUIVO DE TEXTO - INÍCIO
if os.path.isfile("identificacao.csv"):
    arquivo = open("identificacao.csv","r+")
else:
    arquivo = open("identificacao.csv","w+")

#AQUI PRESERVAR AS INFORMAÇÕES DO ARQUIVO
conteudo_anterior = arquivo.readlines()

arquivo.writelines(nome + ";" + departamento + ";" + nome_computador + ";" + so + ";" + ip + "\n")
arquivo.close()
#ESCREVENDO UM ARQUIVO DE TEXTO - FIM

#LENDO UM ARQUIVO DE TEXTO - INÍCIO
arquivo = open("identificacao.csv","r+")
conteudo = arquivo.readlines()
for linha in conteudo:
    #print(linha)
    colunas = linha.split(";")
    linha_nova = ''
    for coluna in colunas:
        linha_nova += coluna + "\t"
        
    print(linha_nova)
arquivo.close()
#LENDO UM ARQUIVO DE TEXTO - FIM