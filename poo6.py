class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f' O {self.nome} foi comer...')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f' O {self.nome} foi miando...')


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Latir(self):
        print(f' O {self.nome} está latino...')


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f' O {self.nome} está pulando...')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugi(self):
        print(f' O {self.nome} está mugindo...')


pet = Gato("Gato", "Laranja")
pet.miar()
pet.comer()

pet2 = Cachorro("Cachorro", "preto")
pet2.Latir()
pet2.comer()

pet3 = Coelho("Coelho", "Branco")
pet3.pular()
pet3.comer()

pet4 = Vaca("Vaca", "Marrom")
pet4.mugi()
pet4.comer()