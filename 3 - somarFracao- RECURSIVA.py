#Cálculo de 1 + 1/2 + 1/3 + ... 1/n
def somarFracao(f):
    if f == 1:
        return f
    else:
        return somarFracao(f-1)+1/f


print(somarFracao(5))
