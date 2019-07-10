#Verifique se uma palavra é palíndromo
def palindromo(p):
    if len(p) <= 1:
        return 0
    else:
        return (p[0] == p[len(p)-1]) and palindromo(p[1:len(p) - 1])


p = 'casa'
p2 = 'asa'
print(palindromo(p2))
