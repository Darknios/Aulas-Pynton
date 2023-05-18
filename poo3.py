class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo


    def comer(self, comida):
        self.comida=comida
        if self.comendo==False:
            print(self.nome,"está Comendo",self.comida)
            self.comendo = True
        else:
            print(self.nome,"não pode comer, pois já está comendo")

    def paredecomer(self):
        if self.comendo==True:
            print(self.nome,"parou de comer")
            self.comendo=False
        else:
            print(self.nome,"não está comendo")

p1 = Pessoa("Sanderson", 70, 23)
p2 = Pessoa('Messias', 72, 21, comendo=True)
p1.paredecomer()
p1.comer("Sopa")
p1.paredecomer()
