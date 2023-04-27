lista_a = []
lista_b = []
a = 0
for x in range (10):
    lista_a.append(float(input("Informe um número: ")))
x=int(input("Digite o multiplicado: "))

for y in range (10):
    lista_b.append(lista_a[y]*x)
print(lista_b)