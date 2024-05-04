import unittest
from zoo import Zoo
from animal import Animal
from recinto import Recinto

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
        self.animal = self.zoo.criar_animal("Leão", "Felino")
        self.recinto = self.zoo.criar_recinto("Felino", "bem cuidados")

    def test_criar_animal(self):
        self.assertEqual(self.animal.nome, "Leão")
        self.assertEqual(self.animal.especie, "Felino")

    def test_criar_recinto(self):
        self.assertEqual(self.recinto.especie, "Felino")
        self.assertEqual(self.recinto.cuidados, "bem cuidados")

    def test_alimentar_animais(self):
        self.zoo.alimentar_animais()
        self.assertEqual(self.animal.felicidade, 60)

    def test_receber_visitantes(self):
        visitantes = self.zoo.receber_visitantes()
        self.assertEqual(visitantes, 60)  # 50 de felicidade do animal + 10 de recinto bem cuidado

if __name__ == '__main__':
    unittest.main()
