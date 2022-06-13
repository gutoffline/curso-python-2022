"""
Crie uma classe que modele uma bola:
    1. Atributos: Cor, circunferência, material
    2. Métodos: trocaCor e mostraCor
""" 
class Bola:
    def trocaCor(self, cor):
        self.cor = cor
    def mostraCor(self):
        print(self.cor)

# Teste da Classe
bola = Bola()
bola.trocaCor("Azul")
bola.mostraCor()