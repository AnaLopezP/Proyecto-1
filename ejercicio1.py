'''Ejercicio práctico1 (3Puntos): Creación de una clase en Python que representa una matriz.
Para este ejercicio, deberás crear una clase que representa una matriz. 
Las operaciones que esta clase debe permitir son la creación de una matriz a partir de una lista de listas,
la impresión de la matriz en una forma legible, y el cálculo de la transpuesta de la matriz. Asegúrate de que cada método tenga una única responsabilidad.'''

#operaciones son acciones---> osea las funciones. 
class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos 
        #Este es el constructor, las acciones las hacemos aparte en otra clase (interface)
        #los elementos serán la lista de listas, que añadiré cuando cree la matriz.
    def imprimir(self):
        for fila in self.elementos:
            print(fila)                    #estas funciones tendrían que ir en otra clase (todo)

    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    
#En esta clase están solo las acciones, en otra tiene que estar la estructura (MVC)
#habría que crear otra clase todo para que quien quiera añadir más funciones no se toque la clase todo original que has hecho tú.
#La manera perfecta de hacerlo es haciendo otra clase que sea un lanzador
#creo que la tercera clase hereda de las otras, entonces llamas a esa y te hace todo. 