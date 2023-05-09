while True:
    n1 = int(input("Informe um numero: "))
    n2 = int(input("Informe outro numero: "))

    if n1>n2:
        print("O numero é maior:",n2,n1)
    else:
        print("O numero é maior",n1,n2)
        novamente = input("Você deseja realizar o codigo novamente? s/n: ")
        if novamente == "n":
            break
