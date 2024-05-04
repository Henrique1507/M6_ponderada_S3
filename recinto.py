class Recinto:
    def __init__(self, especie, cuidados):
        self.especie = especie
        self.cuidados = cuidados  # bem ou mal cuidados
        self.animais = []

    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
        else:
            raise ValueError("Espécie do animal não coincide com a do recinto.")

    def remover_animal(self, animal):
        self.animais.remove(animal)
