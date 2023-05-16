def quantidade_letras(informacao):
    contador = 0
    contador2=0
    for x in informacao:
        if x !=' ':
            contador = contador+1
        contador2+=1
    contador2-=1
    print(contador,"é a quantidade de letras do nome:",arara)
    for y in range(contador2,-1,-1):
        print(informacao[y], end ='')
    return " "
arara = input('digite o nome aqui: ')
print(quantidade_letras(arara))