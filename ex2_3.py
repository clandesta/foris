import time

def fibonnacci(n):
    fibonacciAnterior = 1
    fibonacciActual = 0
    k = 0
    while k <= n-1:
        sumaFibonacci = fibonacciAnterior+fibonacciActual
        fibonacciAnterior = fibonacciActual
        fibonacciActual = sumaFibonacci
        k+=1
    return fibonacciActual


def divisores(n):
    primo = 1
    listPrimos = {}
    
    resultado = False
    cnt=1
    while resultado != True:
        
        cociente = n // primo
        resto = n % primo
        if resto == 0 and primo == 1:
            listPrimos[primo]= cnt
            primo = nextPrimo(primo+1)
            cnt=1
        else:
            if resto != 0:
                primo = nextPrimo(primo+1) 
                cnt=1
            else:

                if resto == 0:
                    listPrimos[primo]=cnt
                    n=cociente
                    cnt+=1   
        if cociente == 1 and resto == 0:
            resultado = True

    suma = 1
    if len(listPrimos) == 1:
        return 1
    else:
        del listPrimos[1]

    for item in listPrimos:
        suma*= (listPrimos.get(item)+1)
    
    return suma
 
def isPrimo(n):
    cnt=0
    i = 1
    while i <=n+1:
        if n % i == 0:
            cnt+=1
        i+=1
        if cnt >= 2:
            return False

    if cnt <= 2:
        return True
    else:
        return False

def Primo2(n):


def nextPrimo(n):
    while isPrimo(n) == False:
        n+=1
    return n

find = False
i=1
t0 = time.time()
while find != True:
    fib = fibonnacci(i)
    cntDiv = divisores(fib)
    print "N: ",i, " Fibonnaci: ",fib, ", Cantidad divisores: ",cntDiv
    if cntDiv >= 100:
        print "El primer numero de fibonacci en tenser 100 divisores es %d" % (fib)
        find = True
    else:
        i+=1

print "Se demoro ",time.time()-t0," en encontrar el primer fibonnaci con 100 divisores"