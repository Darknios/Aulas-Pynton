quantidade = int(input("Informe os números de alunos: "))
alunos=[]
for x in range(quantidade):
    alunos.append(input("Digite o nome do aluno "))

pesquisa=input("Digite um nome para a pesquisa: ")
for y in range(quantidade):
    if pesquisa== alunos[y]:
        print(y,alunos[y])