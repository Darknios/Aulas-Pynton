def primo(numero):
    cont_p = 0
    if numero !=1:
        for x in range(1,numero,+1):
            if numero%x == 0:
                   cont_p+=1
        if cont_p >2:
            print("O número não é primo")
        else:
            print("O número é primo!")
    else:
        print('O número não é primo!')

n=int(input('Digite aqui: '))
print(primo(n))