from classes import *
import unittest

class TesteAnimais(unittest.TestCase):
    def testeCriarAnimais(self):
        # Cria animais
        animal1 = Animal("Pé de Pano", "cavalo")
        animal2 = Animal("Trovão", "cavalo")

        self.assertEqual({'nome': "Pé de Pano", 'especie': "cavalo"}, {'nome': animal1.nome, 'especie': animal1.especie})
        self.assertEqual({'nome': "Trovão", 'especie': "cavalo"}, {'nome': animal2.nome, 'especie': animal2.especie})

    def testeAlimentarAnimais(self):
        # Cria animais
        animal1 = Animal("Pé de Pano", "cavalo")
        animal2 = Animal("Trovão", "cavalo")

        # Alimenta um animal
        animal1.alimentar()

        self.assertEqual(animal1.nivelFelicidade, 1)
        self.assertEqual(animal2.nivelFelicidade, 0)


class TesteRecinto(unittest.TestCase):
    def testeCriarRecinto(self):
        # Cria um zoologico
        zoologico = Zoologico('Meu Zoologico')

        # Cria um recinto
        recinto = zoologico.criarRecinto('Recinto de Cavalos', 'cavalo')

        self.assertEqual({'nome': "Recinto de Cavalos", 'especie': "cavalo", 'zoologico': zoologico}, {'nome': recinto.nome, 'especie': recinto.especie, 'zoologico': recinto.zoologico})

    def testeAdicionarAnimais(self):
        # Cria um zoologico
        zoologico = Zoologico('Meu Zoologico')

        # Cria um recinto
        recinto = zoologico.criarRecinto('Recinto de Cavalos', 'cavalo')

        # Cria animais
        animal1 = Animal("Pé de Pano", "cavalo")
        animal2 = Animal("Trovão", "cavalo")
        animal3 = Animal("Nemo", "peixe")

        # Adiciona animais ao recinto
        recinto.adicionarAnimal([animal1, animal2])

        self.assertEqual(recinto.obterAnimais(), [animal1, animal2])

        # Teste para adicionar um animal com espécie diferente do recinto
        with self.assertRaises(ValueError):
            recinto.adicionarAnimal(animal3)

    def testeCuidarRecinto(self):
        # Cria um zoologico
        zoologico = Zoologico('Meu Zoologico')

        # Cria um recinto
        recinto = zoologico.criarRecinto('Recinto de Cavalos', 'cavalo')

        # Cuida de um recinto
        recinto.cuidarRecinto()

        self.assertEqual(recinto.bemCuidado, True)

    def testeRemoverAnimal(self):
        # Cria um zoologico
        zoologico = Zoologico('Meu Zoologico')

        # Cria um recinto
        recinto = zoologico.criarRecinto('Recinto de Cavalos', 'cavalo')

        # Cria animais
        animal1 = Animal("Pé de Pano", "cavalo")
        animal2 = Animal("Trovão", "cavalo")

        # Adiciona animais ao recinto
        recinto.adicionarAnimal([animal1, animal2])

        # Remove um animal do recinto
        recinto.removerAnimal(animal2)

        self.assertEqual(recinto.obterAnimais(), [animal1])


class TesteZoologico(unittest.TestCase):
    def testeReceberVisitante(self):
        # Cria um zoologico
        zoologico = Zoologico('Meu Zoologico')

        # Receber 8 visitantes
        zoologico.receberVisitante(8)

        self.assertEqual(zoologico.visitantes, 8)

    def testeAtrairVisitantes(self):
        # Cria um zoologico
        zoologico = Zoologico('Meu Zoologico')

        # Cria um recinto
        recinto = zoologico.criarRecinto('Recinto de Cavalos', 'cavalo')

        # Cria animais
        animal1 = Animal("Pé de Pano", "cavalo")
        animal2 = Animal("Trovão", "cavalo")

        # Adiciona animais ao recinto
        recinto.adicionarAnimal([animal1, animal2])

        # Para um animal ficar feliz, ele precisa chegar ao 3 nível de felicidade. 
        # Quando um animal fica feliz, atrai um visitante.
        animal1.alimentar()
        animal1.alimentar()
        animal1.alimentar()

        animal2.alimentar()
        animal2.alimentar()
        animal2.alimentar()

        # Ao cuidar de um recinto, atrai um visitante.
        recinto.cuidarRecinto()

        self.assertEqual(zoologico.visitantes, 3)
