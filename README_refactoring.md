# dirtyCodeExample
Refactorización

Línea 1: El nombre del método definido es **multiplicar_matrices** por lo que el método solo debería hacer eso, cumpliendo con el pricipio de Single Responsability. 

Code Smell: 

Refactoring: Abstraer las lecturas por teclado en otro método. El metodo se llama ingresar_datos()

Línea 2: la variable muchos_argumentos = False nunca es utilizada. 

Code Smell:

Refactoring: Eliminar esa variable

Líneas 4-9 y 16-20: Existe código duplicado que puede ser parte de un método nuevo.

Code Smell: 

Refactoring: Creación de un nuevo método llamado **leer_argumentos()** que recibe x, y y la matriz m 

Líneas 12-14: Estas tres líneas hacen una comprueban que el número de columnas de la primera matriz sea igual al número de filas de la segunda matriz. El if de la línea 12 no es muy claro y todo el código mencionado puede ser parte de un método con un nombre descriptivo. 

Code Smell:

Refactoring: Creación de un nuevo método llamado **comparar_dimensiones()**

Líneas 24 y 25: Se definen las matrices m1 y m2 como un arreglo vacío y luego se pasan como aurgumento a la función **multiplicar_matrices(m1,m2)**, pero no se camnbian los valores de estas antes. La definición en esas líneas está demás. 

Code Smell:

Refactoring: Se pasan m1 y m2 como argumentos a la función **multiplicar_matrices** inicializándolas como m1=[] y m2=[]
De esta manera, ya no es necesario definirlas antes de llamar a la función. Así la función **multiplicar_matrices()** ya no recibe parámetros.




