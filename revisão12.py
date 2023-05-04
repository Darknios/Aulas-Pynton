while True:
    pergunta = input("Qual das opções você deseja: 1-Triangulo, 2-Retângulo, 3-encerrar: ")
    if pergunta == "3":
        break
    base = float(input("Informe o valor da base: "))
    altura = float(input("Informe o valor da altura: "))
    if pergunta == "1":
        A = (base * altura)/2
        print("O valor da área de um triangulo é:",A)
    elif pergunta == "2":
        A = (base * altura)
        print("O valor da área de um retangulo é:", A)
