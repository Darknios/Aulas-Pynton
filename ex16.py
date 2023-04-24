quantidade = int(input("Informe os números de alunos: "))
alunos=[]
for x in range (quantidade):
    alunos.append(input("Digite o nome do aluno: "))
    print(x)
for y in range (quantidade):
    print(alunos[y],y)
