class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
    def comer(self):
        print(self.nome,"Comendo")
p1 = Pessoa("Sanderson", 70, 23)
p2 = Pessoa('Messias', 72, 21, comendo=True)
print(p1.nome)
print(vars(p1))
print(p2.nome)
print(vars(p2))