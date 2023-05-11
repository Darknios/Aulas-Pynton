from funciona7 import *

while True:
    produto = input("Digite um nome do produto: ")
    preco = input("Digite o preço do produto: ")
    listaadd(produto, preco)
    resp = input("Deseja continuar: ")
    if resp!="S":
        break
print(lista_produto)
print(lista_preco)