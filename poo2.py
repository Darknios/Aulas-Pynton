class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo


    def comer(self, comida):
        self.comida=comida
        self.comendo = True
        print(self.nome,"está Comendo",self.comida)
p1 = Pessoa("Sanderson", 70, 23)
p2 = Pessoa('Messias', 72, 21, comendo=True)
p1.comer("Sopa")
p2.comer("Carne")
