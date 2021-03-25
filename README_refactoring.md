# dirtyCodeExample
Refactorización

Línea 1: El nombre del método definido es **multiplicar_matrices** por lo que el método solo debería hacer eso, cumpliendo con el pricipio de Single Responsability. 

Code Smell: 

Refactoring: Abstraer las lecturas por teclado en otro método. El metodo se llama ingresar_datos()

Línea 2: la variable muchos_argumentos = False nunca es utilizada. 

Code Smell:

Refactoring: Eliminar esa variable

Líneas 4-9 y 16-20: Existe código duplicado que puede ser parte de un método nuevoç 

Code Smell: 

Refactoring: Creación de un nuevo método llamado **leer_aegumentos()** que recibe x, y y la matriz m 





