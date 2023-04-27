A=[]
B=[]
C=[]
n = int(input("Informe um número: "))
soma1 = 0
soma2 = 0
for x in range (n):
    A.append(int(input("Informe o numero para a lista A: ")))
for y in range (n):
    B.append(int(input("Informe o numero para a lista B: ")))
for p in range (n):
    C.append(A[p] + B[p])
    
    print(A)
    print(B)
    print(C)
