eleitores = int(input("Informe o numero de eleitores: "))
votos_em_branco = int(input("Informe o numero de votos em branco"))
nulos = int(input("Informe o numero de nulos"))
válidos = int(input("Informe o numero de válidos"))

pvotos_em_branco=(votos_em_branco/eleitores)*100
pnulos = (nulos/eleitores)*100
pvalidos = (válidos/eleitores)*100
print("Total de eleitores",eleitores)
print("Percentual de votos branco",votos_em_branco,"%")
print("Percentual de votos nulos",nulos,"%")
print("Percentual de votos válidos",válidos,"%")




























