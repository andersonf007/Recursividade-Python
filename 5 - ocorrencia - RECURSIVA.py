#Calcula quantas vezes o caractere X ocorre em uma string
def ocorrencia(s, c):
    if len(s) == 0:
        return 0
    else:
        if s[0] == c:
            return 1 + ocorrencia(s[1:], c)
        else:
            return ocorrencia(s[1:], c)

s = 'luis'
print(ocorrencia(s, 'i'))
