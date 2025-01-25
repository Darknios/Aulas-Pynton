while True:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite um segundo número: "))
    
    # Opções de operação
    while True:
        print("\nEscolha uma das opções:")
        print("1 - Soma")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Encerra programa ou realizar uma nova operação")
        
        escolha = float(input("Digite a opção que você deseja: "))
        
        if escolha == 1:
            soma = numero1 + numero2
            print("A soma dos valores é: ", soma)
            
        elif escolha == 2:
            sub = numero1 - numero2
            print("A subtração dos valores é: ", sub)
            
        elif escolha == 3:
            mult = numero1 * numero2
            print("A multiplicação dos valores é: ", mult)
        
        elif escolha == 4:
            if numero2 != 0:
                div = numero1 / numero2
                print("A Divisão dos valores é: ", div)
            else:
                print("Erro! Não é possível dividir por zero.")
            
        elif escolha == 5:
            print("Encerra programa ou realizar novamente.")
            break
        
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

    # Pergunta ao usuário se quer realizar outra operação
    continuar = input("\nDeseja realizar outro cálculo? (s para sim, qualquer outra tecla para encerrar): ").lower()
    if continuar != 's':
        print("Encerrando o programa.")
        break
