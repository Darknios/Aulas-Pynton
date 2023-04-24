c = 1
escolha = 0
while escolha != 6:
    c = c + 1
    numero1 = int(input("Informe um número: "))
    numero2 = int(input("Informe um segundo número: "))
    while True:
        print("Escolha uma das opções: 1-Soma, 2-Subtração, 3-Multiplicacão, 4-Divisão, 5-Escolha novamente uma opcão, 6-Encerrar programa")
        escolha = float(input("Digite a opcão que você quer: "))

        if escolha == 1:
            soma = numero1 + numero2
            print(soma)

        elif escolha == 2:
            sub = numero1 - numero2
            print(sub)

        elif escolha == 3:
            mult = numero1 * numero2
            print(mult)

        elif escolha == 4:
            div = numero1/numero2
            print(div)

        elif escolha == 5:
           break


        elif escolha == 6:
            print("Programa Encerrado")
            break

        print("O resultado escolhido foi: ")