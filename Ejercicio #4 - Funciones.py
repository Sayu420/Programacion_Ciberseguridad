#Ejercicio 4 - Funciones

Discriminante = lambda a, b, c : b**2 - 4*a*c

def Una_Solucion (a, b):
    return -b/(2*a)

def Resolver_Cuadratica(X, Y, Z):
    dis = float ( Discriminante(X, Y, Z))
    if (dis < 0):
        print("\nNo existe solucion en los numeros reales para la ecuacion.")
    elif (dis == 0):
        print("\nLa ecuacion tiene solo una solucion.")
        print("X = " + str(Una_Solucion(X, Y)))
    else:
        print("\nLa ecuacion tiene 2 posibles soluciones")
        x1 = float ((-Y + dis**(1/2))/2*X)
        x2 = float ((-Y - dis**(1/2))/2*X)
        print("X1 = " + str(x1))
        print("X2 = " + str(x2))

validar = False
A = 0
print("\nIngrese los coeficientes de la ecuacion cuadratica que desea resolver.")
print("                         Ax^2 + Bx + C = 0\n\n")

while(not validar):    
    try:
        while(A == 0):
            A = float( input("Ingrese el valor de A: "))
            if (A != 0):
                B = float( input("Ingrese el valor de B: "))
                C = float( input("Ingrese el valor de C: "))
                Resolver_Cuadratica(A, B, C)
                validar = True
            else:
                print("\nError: Valor no permitido.")
    except ValueError:
        print ("\nError: Valor ingresado no corresponde a un valor numerico")
        
# Prueba
