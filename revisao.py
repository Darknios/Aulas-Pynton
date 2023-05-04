nota1=float(input("informe uma nota: "))
nota2=float(input("Informe uma segunda nota: "))
media=(nota1+nota2)/2

if media >=7:
    print("Aluno está aprovado")
elif media >=4:
    print("Aluno está de recuperação")
else:
    print("Aluno está aprovado")
    print("A sua média é: ", media)
novamente = "s"
while novamente == "s":


   novamente =str(input("Você deseja realizar novamente o calculo?"))
   if novamente == "s":
       continue
print("Processor finalizado")
