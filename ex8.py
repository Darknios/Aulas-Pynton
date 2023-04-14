novamente = "s"
while novamente == "s":
    nota1 = float(input("Informe uma nota: "))
    while nota1 <0 or nota1 >10:
        nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    while nota2 <0 or nota2 >10:
        nota2 = float(input("Informe a segunda nota: "))
    media = (nota2+nota1)/2
    print("a sua média é:", media)
    novamente = str(input("Você Deseja realizar novamente o calculo? s ou n? "))
print("Processor finalizado")

