class Banco:
    def __init__(self,nome,tipo_da_conta,numero_conta):
        self.nome = nome
        self.tipo_da_conta = tipo_da_conta
        self.numero_conta = numero_conta
        self.saldo = 0
        self.status = False
    def conta_ativa(self):
        if self.status == True:
            print("A sua conta já está ativa!")
        else:
            self.status = True
            print("Conta ativa")

    def sacar(self,pegunta):

        if self.status == True:
          if pegunta > self.saldo:
               print("Saldo insuficiene para esse sague!")
          else:
               if self.saldo <=0:
                  self.saldo = self.saldo - pegunta

        else:
            print("Conta desativada!")

    def verificar(self):
        if self.status == True:
            print(self.nome, "vc tem", "R$",self.saldo)
        else:
            print("Sua conta está desativada")

    def depositar(self,deposito):
        if self.status == True:
            print("Você está depositando",deposito)
            self.saldo = self.saldo + deposito

        else:
            print("Sua conta está desativada")

    def desativar(self):
        if self.status == False:
            print("A sua conta está desativada")
        else:
            self.status = False
        print("A sua conta foi desativada")

pessoa = Banco ("Sanderson", "poupança", 81999710140)
pessoa.conta_ativa()
pessoa.sacar(120)
pessoa.verificar()
pessoa.depositar(500)
pessoa.desativar()
