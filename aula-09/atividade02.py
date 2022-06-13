class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    def identificacao(self):
        print("Olá, meu nome é", self.nome, "e tenho", self.idade, "anos. Meu curso atual é", self.curso)

estudante01 = Estudante("Cleiton", 20, "Python I")
estudante02 = Estudante("Roberta", 22, "Excel Avançado")

estudante01.identificacao()
estudante02.identificacao()
