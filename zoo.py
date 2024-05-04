from animal import Animal
from recinto import Recinto

class Zoo:
    def __init__(self):
        self.animais = []
        self.recintos = []

    def criar_animal(self, nome, especie, felicidade=50):
        animal = Animal(nome, especie, felicidade)
        self.animais.append(animal)
        return animal

    def criar_recinto(self, especie, cuidados):
        recinto = Recinto(especie, cuidados)
        self.recintos.append(recinto)
        return recinto

    def alimentar_animais(self):
        for animal in self.animais:
            animal.alimentar()

    def receber_visitantes(self):
        felicidade_total = sum(animal.felicidade for animal in self.animais)
        cuidados_recintos = sum(10 for recinto in self.recintos if recinto.cuidados == "bem cuidados")
        visitantes = felicidade_total + cuidados_recintos
        return visitantes
    
    def receber_visitantes_felizes(self):
        visitantes_felizes = sum(1 for animal in self.animais if animal.felicidade >= 80)
        return visitantes_felizes
