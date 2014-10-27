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
    #terminar funcion para obtener el siguiente numero primo
    while isPrimo(n) == False:
        n+=1

    return n

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def isFibonnaci(n):
    print ""


x = 2678771517965668302371062622650004526403512029263834018609375970925877627812340306232995947039239645318986682293882867062967863214230785108996144393674643700983641943706057746355268651265592785469488545538261618745895485316849691889791385986519265728642799119421635541915107457913156096709301417017344



for i in xrange(1,999):
    print 2**i
exit()

for i in xrange(3,10):
    print "n: ",i," es fibonnaci: ",isFibonnaci()
exit()


