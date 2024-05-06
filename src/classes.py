class Zoologico:
    def __init__(self, nome):
        self.nome = nome
        self.visitantes = 0
        self.recintos = []

    def criarRecinto(self, nome, especie):
        recinto = Recinto(nome, especie, zoologico=self)
        self.recintos.append(recinto)
        return recinto
    
    def receberVisitante(self, quantidade=1):
        self.visitantes += quantidade


class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie.lower()
        self.nivelFelicidade = 0
        self.recinto = None

    def aumentarNivelFelicidade(self):
        if self.nivelFelicidade < 5:
            self.nivelFelicidade += 1
        if self.nivelFelicidade == 3:
            self.recinto.zoologico.receberVisitante()

    def alimentar(self):
        self.aumentarNivelFelicidade()


class Recinto:
    def __init__(self, nome, especie, zoologico):
        self.nome = nome
        self.especie = especie.lower()
        self.animais = []
        self.bemCuidado = False
        self.zoologico = zoologico

    def validaEspecie(self, animal):
        if self.especie == animal.especie:
            return True
        else:
            return False
        
    def adicionarAnimal(self, animal):
        def adicionarAnimalNaLista(animalParaAdicionar):
            if self.validaEspecie(animalParaAdicionar):
                animalParaAdicionar.recinto = self
                self.animais.append(animalParaAdicionar)
            else:
                raise ValueError("Espécie do animal não corresponde à do recinto")

        if isinstance(animal, list):
            for a in animal:
                adicionarAnimalNaLista(a)
        else:
            adicionarAnimalNaLista(animal)

    def removerAnimal(self, animal):
        def removerAnimalDaLista(animalParaRemover):
            if animalParaRemover in self.animais:
                self.animais.remove(animalParaRemover)

        if isinstance(animal, list):
            for a in animal:
                removerAnimalDaLista(a)
        else:
            removerAnimalDaLista(animal)

    def obterAnimais(self):
        return self.animais

    def cuidarRecinto(self):
        self.bemCuidado = True
        self.zoologico.receberVisitante()
