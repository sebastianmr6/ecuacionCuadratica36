import math
class ecuacionCuadratica():
    a = int(input("Ingrese valor A= "))
    b = int(input("Ingrese valor B= "))
    c = int(input("Ingrese valor C= "))
    if a == 0:
        print ("error, división por 0")
    elif b ** 2 - 4 * a * c < 0:
        print ("no tiene solución en los reales")
    else:
        x1 = (- b + math.sqrt( b**2 - 4 * a * c ))/( 2 * a )
        x2 = (- b - math.sqrt( b**2 - 4 * a * c ))/( 2 * a )
        print (" el valor de x1 es = " + str(x1))
        print (" el valor de x1 es = " + str(x1))
