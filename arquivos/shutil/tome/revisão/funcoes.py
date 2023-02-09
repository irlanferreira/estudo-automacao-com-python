def fatorial(n, mostrar=False):
    c = n - 1
    res = n
    while c > 0:
        res *= c
        c-=1
fatorial(3)