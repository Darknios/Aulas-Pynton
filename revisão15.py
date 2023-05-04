inicio = int(input("Informe o horario do inicio do jogo: "))
fim = int(input("Informe o horario do fim dp jogo: "))
tempo = (inicio - fim)
if inicio<fim:
    print(tempo,"Horas")
else:
    print(24-inicio+fim,"Horas")