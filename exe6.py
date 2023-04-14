solucao=0
valor1 = int(input("Informe um valor? "))
valor2 = int(input("Informe um segundo valor? "))
while valor2 == 0:
    valor2 = int(input("O valor que escolheu é igual a zero por favor escolhar outro número! "))
else:
    solucao=valor1/valor2
    print(solucao)
