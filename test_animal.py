import unittest
from animal import Animal

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("Leão", "Felino")

    def test_alimentar(self):
        self.animal.alimentar()
        self.assertEqual(self.animal.felicidade, 60)

    def test_diminuir_felicidade(self):
        self.animal.diminuir_felicidade()
        self.assertEqual(self.animal.felicidade, 45)

if __name__ == '__main__':
    unittest.main()
