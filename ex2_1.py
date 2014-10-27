import math
def fib(n):
    i = 1
    j = 0
    print n
    for k in xrange(0,n-1):
        t = i+j
        i = j
        j = t
    return j




def divisoresPrimos(n):
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
def divisores(n):
    fin = False
    cnt = 0
    while fin != True:
        if n // 2 == 0 :
            print "nugger"


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

def matFib(n):
    if n <= 0:
        return 0
    i = n-1
    mat = {'a':1,'b':0,'c':0,'d':1}
    while  i > 0:
        if i % 2 != 0:
            print "impar ",i
            mat['a']= (mat['d'] * mat['b']) + (mat['c'] * mat['a'])
            mat['b']=(mat['d']*(mat['b']+mat['a'])+(mat['c']*mat['b']))
        mat['c'] = (mat['c']**2) + (mat['d']**2)
        mat['d'] = mat['d'] * ((2* mat['c'])+mat['d'])
        i = i/2
        print mat
    return mat['a']+mat['b']

def fibIndex(n):
    if n < 1:
        return 1
    index = math.log(n * math.sqrt(5) + 1.0/2.0, math.pi)
    return index
#for i in xrange(0,10):
#print "Print fib 100: ",matFib(2)


print fibIndex(2)