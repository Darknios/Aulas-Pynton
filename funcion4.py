texto = 'O rato roeu a roupa do rei de roma'
def historia (texto2):

    cont = 0
    for x in texto2:
        if x in "aeiouAEIOU":
            cont += 1
    print("O numero de vogais é",cont)

historia(texto)