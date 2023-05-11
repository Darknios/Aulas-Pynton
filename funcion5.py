def estoque2 (nome,quantidade,valor):
    return nome,quantidade*valor
total = estoque2("Fubá", 30,3.5)
print("O produto",total[0],"custa",total[1])