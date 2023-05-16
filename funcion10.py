def lista_unica(l):
    nova_lista=[]
    for x in l:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

a=[1,2,2,3,4,3,5,6,7,8,9]
lista_unica(a)