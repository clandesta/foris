import time
import math
def fibonnacci(n):
    t0 = time.time()
    fibonacciAnterior = 1
    fibonacciActual = 0
    k = 0
    while k <= n-1:
        sumaFibonacci = fibonacciAnterior+fibonacciActual
        fibonacciAnterior = fibonacciActual
        fibonacciActual = sumaFibonacci
        k+=1
    print "Tiempo de busqueda fib ",n, " = ",time.time()-t0
    return fibonacciActual


def findFib(i):
    t0 = time.time()
    print ((1/math.sqrt(5))*pow(((1+math.sqrt(5))/(2)),i)-(1/math.sqrt(5))*pow(((1-math.sqrt(5))/(2)),i))
    print "Tiempo de busqueda findFib ",i, " = ",time.time()-t0

def divisores(n):
    t0 = time.time()
    cnt = 0
    i=1
    while i <= n:
        if n % i == 0:
            cnt+=1
        i+=1
    print "Tiempo de busqueda divisores ",i-1, " = ",time.time()-t0
    return cnt

def getPrimo(n):
    i = 1
    cnt=0
    while n >= i:
        if n % i == 0:
            cnt+=1
        if cnt >2:
            return -99
        i+=1 
    return n

i = 1
t0 = time.time()
while i < 15000:
    primo = getPrimo(i)
    if(primo!=-99):
        print "Primo: %d" % (primo)
    i+=1
print "Tiempo de busqueda de primos ",i-1, " = ",time.time()-t0
exit()

print fibonnacci(500000)
print "divisores : %d" % (divisores(500000))



init = 1
cntDiv=0
t0 = time.time()
while cntDiv <= 1000:
    print fibonnacci(50000)
    exit()
    fib = fibonnacci(init)
    cntDiv = divisores(fib)
    print "fibonnacci n: ",fib,", cantidad de divisores: ",cntDiv
    init+=1

print "Se demoro ",time.time()-t0," en encontrar el primer fibonnaci con 1000 divisores"