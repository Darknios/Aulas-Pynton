pin="12345"
tentativas=1
senha=input("Digite sua senha: 1")
while senha!=pin:
    tentativas = tentativas +1
    print("Senha incorreta, digite novamente: ")
    senha=input()
if tentativas>2 and senha!=pin:
    print("senha bloqueada")

else:
    print("Acesso liberado")




