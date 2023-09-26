class Matriz():
    def __init__(self, elementos, list):
        self.elementos = elementos
        
        
class Traspuesta(Matriz):
    def __init__(self, elementos, list):
        super().__init__(elementos)
        
    def traspuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))]) 
    #es una buena opcion para elementos pequeños, pero si es grande peta. tendría que ser recursivo
    
class Imprimir(Matriz):
    def __init__(self, elementos, list):
        super().__init__(elementos)
        
    def imprimir(self):
        for fila in self.elementos:
            print(fila)
            
            
class Lanzador(Imprimir, Traspuesta):
    #creame una funcion que me permita llamar a la funcion imprimir y traspuesta y recoja los datos con un imput de los elementos de la matriz
    
    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input("numero de filas: "))
        self.cantidad_columnas = int(input("numero de columnas: "))
        self.crear_matriz()
        super().__init__(self.elementos)
        
    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Ingrese el elemento ")))
            self.elementos.append(fila)    
    
    def lanzar(self):
        self.imprimir()
        print("La matriz traspuesta es: ")
        self.traspuesta.imprimir()
        
            
            
#hay que hacer una clase lanzador que haga esta weá. bueno lo hace el miguel ohara
m = Imprimir([1, 2], [3, 4])
m.imprimir()

t = Traspuesta(m.elementos)
print(t.traspuesta().elementos)
