

def fib(n,tabla):
    nFib=0
    if(n== 0  or n==1):
        return 1
    if(n>len(tabla)):
        print n
        nfib = tabla[n-1]+tabla[n-2]
        tabla[n]=nFib
    return tabla[n]

tabla = []

for x in xrange(1,10):
    numeroFib = fib(x,tabla)
    print numeroFib
    tabla[x]=numeroFib
print tabla
