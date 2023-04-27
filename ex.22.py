user = []
passoword = []

for x in range (5):
    user.append(input("Digite o usuario: "))
    passoword.append(input("Digite uma senha: "))
print(input("Digite o nome do usuário: "))
u=input("Usuario para login")
s=input("Senha do login")

for y in range(5):
    if user [y]==u and passoword[y]==s:
        print("Login efetuado com sucesso!!")

