def multiplicar_matrices(m1, m2):
    muchos_argumentos = False
    x1, y1 = tuple([int(x) for x in input("ingrese dimensiones de la primera matriz de forma -> x y: ").split()])
    print('Ingrese fila por fila la primera matriz')
    for i in range(x1):
        m1 += [[int(x) for x in input().split()]]
        if(len(m1[0]) > y1):
            print("Muchos argumentos en la fila")
            exit()
    
    x2, y2 = tuple([int(x) for x in input("ingrese dimensiones de la segunda matriz de forma -> x y: ").split()])
    if(y1 != x2):
        print("Las dimensiones de las matrices no son compatibles para multiplicarse")
        exit()
    print('Ingrese fila por fila la segunda matriz')
    for i in range(x2):
        m2 += [[int(x) for x in input().split()]]
        if(len(m2[0]) > y2):
            print("Muchos argumentos en la fila")
            exit()
    return [ [sum([m1[i][k]*[fila[j] for fila in m2][k] for k in range(len(m1[i]))]) for j in range(len(m2[0]))] for i in range(len(m1))]
            
    
m1 = []
m2 = []
m3 = multiplicar_matrices(m1,m2)
print("La matriz resultante es: ",m3)