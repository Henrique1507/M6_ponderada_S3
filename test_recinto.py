import unittest
from recinto import Recinto
from animal import Animal

class TestRecinto(unittest.TestCase):
    def setUp(self):
        self.recinto = Recinto("Felino", "bem cuidados")
        self.animal = Animal("Tigre", "Felino")

    def test_adicionar_animal(self):
        self.recinto.adicionar_animal(self.animal)
        self.assertIn(self.animal, self.recinto.animais)

    def test_remover_animal(self):
        self.recinto.adicionar_animal(self.animal)
        self.recinto.remover_animal(self.animal)
        self.assertNotIn(self.animal, self.recinto.animais)

if __name__ == '__main__':
    unittest.main()
