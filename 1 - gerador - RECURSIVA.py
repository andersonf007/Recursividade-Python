def gerador(f):
    if f == 1 or f == 2:
        return 0
    else:
        return (2*gerador(f-1) + 3*gerador(f-2))

print(gerador(5))
