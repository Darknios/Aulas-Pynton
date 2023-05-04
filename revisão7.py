while True:
    base = float(input("Informe o valor da base: "))
    altura = float(input("Informe o valor da altura: "))
    A = (base * altura)/2
    print("O valor da base e da altura de um triangulo é:",A)
    resposta = input("Você gostaria de repitir o programa novamente? s/n")
    if resposta == "n":
        break