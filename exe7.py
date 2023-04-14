alunos = int(input("Informe a quantidade de alunos? "))
i = 1
soma = 0
while i <= alunos:
    notas = float(input(f"Informe a nota do {i} aluno ? "))
    i += 1
    soma = soma + notas
media = soma / alunos
print(media)


