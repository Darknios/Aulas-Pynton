class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo


    def andar(self, andar):
        self.andar=andar
        if self.andar==False:
            print(self.nome,"está andando",self.andar)
            self.andar = True
        else:
            print(self.nome,"não pode andar, pois já está andando")

    def paredeandar(self):
        if self.paredeandar==True:
            print(self.nome,"parou de andar")
            self.paredeandar=False
        else:
            print(self.nome,"está parado falando")

p1 = Pessoa("Sanderson", 70, 23)
p1.paredeandar()
p1.andar("na rua")
