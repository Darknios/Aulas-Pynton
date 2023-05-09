while True:
    numero = int (input("Informe um numero: "))
    if numero ==0:
        print("Numero invalido!")
    elif numero >0:
        print("numero positivo!")
    else:
        print("numero negativo!")
    respota = input("Deseja continuar")
    if respota == "não":
        break