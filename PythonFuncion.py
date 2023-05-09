def somar (n1,n2):
    print(n1+n2)
def sub (n1,n2):
    print(n1-n2)
def mult (n1,n2):
    print(n1*n2)
def div (n1,n2):
    print(n1/n2)
while True:
    peguntar = input("Informe uma das opção 1- Somar, 2-Subtrair, 3-Multiplicar, 4-Dividir, 5-Sair: ")
    if peguntar == "5":
        break
    if peguntar == "1":
        n1 = int(input("Informe um número: "))
        n2 = int(input("Informe outro número: "))
        somar(n1, n2)
    if peguntar == "2":
        n1 = int(input("Informe um número: "))
        n2 = int(input("Informe outro número: "))
        sub(n1, n2)
    if peguntar == "3":
        n1 = int(input("Informe um número: "))
        n2 = int(input("Informe outro número: "))
        mult(n1, n2)
    if peguntar == "4":
        n1 = int(input("Informe um número: "))
        n2 = int(input("Informe outro número: "))
        div(n1, n2)

    encerra = input("Você deseja realizar novamente o programa? s/n: ")
    if encerra == "n":
        break