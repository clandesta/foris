def fib(n):
    i = 1
    j = 0
    print n
    for k in xrange(0,n-1):
        t = i+j
        i = j
        j = t
    return j

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
    for i in xrange(1,n+1):
        if n % i == 0:
            cnt+=1

    if cnt <= 2:
        return True
    else:
        return False

def nextPrimo(n):
    while isPrimo(n) == False:
        n+=1
    return n


#for i in xrange(1000,2000):
potX = 999
x = 2**potX
nf = 1
while fib(nf) != x:
    if fib(nf) > x:
        print "fib mayor n:",nf
        potX+=1
        x = 2 **potX
    else:
        print "Fib menor n: ",nf
        nf+=1
    
    if fib(nf) == x:
        print "n fib",nf," 2 elevado a:",potX
        exit()
    
