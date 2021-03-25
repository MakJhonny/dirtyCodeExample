def multiplicar_matrices(m1, m2):
    
    ingresar_datos(m1, m2)
    return [ [sum([m1[i][k]*[fila[j] for fila in m2][k] for k in range(len(m1[i]))]) for j in range(len(m2[0]))] for i in range(len(m1))]

def leer_argumentos(xi, yi, mi):
    print('Ingrese fila por fila la matriz')
    for i in range(xi):
        mi += [[int(x) for x in input().split()]]
        if(len(mi[0]) > yi):
            print("Muchos argumentos en la fila")
            exit()

def comparar_dimensiones(y1, x2):
    if(y1 != x2):
        print("Las dimensiones de las matrices no son compatibles para multiplicarse")
        exit()

def ingresar_datos(m1,m2):
    x1, y1 = tuple([int(x) for x in input("ingrese dimensiones de la primera matriz de forma -> x y: ").split()])
    leer_argumentos(x1,y1,m1)
    x2, y2 = tuple([int(x) for x in input("ingrese dimensiones de la segunda matriz de forma -> x y: ").split()])
    comparar_dimensiones(y1, x2)
    leer_argumentos(x2,y2,m2)




            
    
m1 = []
m2 = []
m3 = multiplicar_matrices(m1,m2)
print("La matriz resultante es: ",m3)