numeros =[]
limitado = 0
cont = 0
for x in range (10):
    numeros.append(int(input("Informe o número: ")))

num=int(input("Informe o número para pesquisar: "))

for y in range(10):
    if num==numeros[y]:
        cont+=1
print("O número",num,"apareceu",cont,"Vezes")

