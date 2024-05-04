import unittest
from zoo import Zoo
from animal import Animal
from recinto import Recinto

class TestZooSystem(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
        self.animal1 = Animal("Leão", "Felino", felicidade=70)
        self.animal2 = Animal("Tigre", "Felino", felicidade=30)
        self.recinto1 = Recinto("Felino", "bem cuidados")
        self.recinto2 = Recinto("Felino", "mal cuidados")

    def test_receber_visitantes_felizes(self):
        zoo = Zoo()
        leao = zoo.criar_animal("Leão", "Felino", 90)  # Felicidade 90
        recinto_leao = zoo.criar_recinto("Felino", "bem cuidados")
        recinto_leao.adicionar_animal(leao)
        
        girafa = zoo.criar_animal("Girafa", "Herbívoro", 85)  # Felicidade 85
        recinto_girafa = zoo.criar_recinto("Herbívoro", "bem cuidados")
        recinto_girafa.adicionar_animal(girafa)

        visitantes_felizes = zoo.receber_visitantes_felizes()
        self.assertEqual(visitantes_felizes, 2)  # Dois animais com felicidade acima de 80


if __name__ == '__main__':
    unittest.main()
    