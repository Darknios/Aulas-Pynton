vetor = []

for x in range (5):
    vetor.append(int(input("Digite um número: ")))

for i in range(5):
    print(vetor[i], end="")
print()
for j in range(5):
    print(vetor[4-j], end="")
