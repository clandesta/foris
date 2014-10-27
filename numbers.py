def decomposeDecimal(number):
    base = 10
    largo = len(str(number))
    digitos = {}

    exp=largo-1

    print "INIT"
   
    while exp>=0:
        print "Base: ",base, " Largo: ",largo," exp: ",exp, "number : ",number
        largo -=1
        digitos[largo] = number/(base**exp)
        aux = digitos[largo]*(base**exp)
        print "aux ",aux
        number -=aux
        print "number ",number
        
        exp -= 1
        print"-----------------------------------"
        pass
    return digitos

number = 3216548761321356848
lista = decomposeDecimal(number)
print "number: ",number
for x in xrange(0, len(lista)):
    print "digito pow(10,",x,"): ",lista[x]
    