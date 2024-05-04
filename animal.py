class Animal:
    def __init__(self, nome, especie, felicidade=50):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade

    def alimentar(self):
        self.felicidade += 10

    def diminuir_felicidade(self):
        self.felicidade -= 5
