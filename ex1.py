file = open("string1.txt","r")

linea = file.readline()
#print linea,len(linea)
#linea = list(linea)
cadenaMayor = ""

def busquedaPalindromo(posicionAnterior, posicionActual,cadena):
    print posicionAnterior
    print posicionActual
    print "cadena anterior ",cadena[posicionAnterior]
    print "cadena siguiente ",cadena[posicionActual]

    if cadena[posicionAnterior]==cadena[posicionActual]:
        print "Palindromo: ",cadena[posicionAnterior:posicionActual+1]
        aux = busquedaPalindromo(posicionAnterior-1,posicionActual+1,cadena)
    else:
        if cadena[posicionAnterior+1]==cadena[posicionActual-1]:
            aux = cadena[posicionAnterior+1:posicionActual]
        else:
            aux = cadena[posicionAnterior:posicionActual+1]
        print "Cadena retorno: ",aux
    
    return aux

for x in xrange(0,len(linea)):
    if x >0 and x < len(linea)-1:
        aux = busquedaPalindromo(x-1,x,linea)

        if len(aux) > len(cadenaMayor):
            print aux
            cadenaMayor=aux

file.close()
print cadenaMayor


#def buscar(linea, x, cadenaMayor):
#    pivotMenor = x
#    pivotMayor = x*2
#           print "cadena de entrada: ",linea[0:pivotMayor]," ",x
#    cnt = 1 
#    while(cnt > 0 and cnt < pivotMayor):
#               print "comparacion: ",linea[x-cnt],"=",linea[x+cnt]
#        if linea[x-cnt] == linea[x+cnt]:
#            aux = linea[x-cnt:x+cnt+1]
#            print "Match: ",aux
#            if len(aux)>len(cadenaMayor):
#                cadenaMayor=aux
#            print "cadenaMayor: ",cadenaMayor
#        else:
#            return cadenaMayor
#        cnt+=1



