#Verifique se uma sequência de números inteiros está ordenada
def ordenacao(lista):
    if len(lista) == 2:
        if lista[0] <= lista[1]:
            return 0
        else:
            return 1
    else:
        return(lista[0] <= lista[1]) and ordenacao(lista[1:len(lista)])

a = [0,3,5,7,3,8,4]
b = [0,1,2,3,4,5,6]

print(ordenacao(b))
