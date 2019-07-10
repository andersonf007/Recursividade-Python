#Inversão de uma string de caracteres
def inverte(s):
    if len(s) == 1:
        return 0
    else:
        return inverte(s[1:len(s)]) + s[0]

print(inverte('casa'))
