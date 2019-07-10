#A partir de um vetor de números inteiros, calcule o produto dos elementos do vetor

def multiplicarVetor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] * multiplicarVetor(lista[1:])

a = [1,23,4,5,68,4]

print(multiplicarVetor(a))
