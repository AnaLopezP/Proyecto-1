class Matriz():
    def __init__(self, elementos: list):
        self.elementos = elementos
        
        
class Traspuesta(Matriz):
    def __init__(self, elementos: list):
        super().__init__(elementos)
        
    def traspuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))]) 
    #es una buena opcion para elementos pequeños, pero si es grande peta. tendría que ser recursivo
    
class Imprimir(Matriz):
    def __init__(self, elementos: list):
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
        self.matriz = Matriz(self.elementos)
        self.traspuesta = Traspuesta(self.matriz)
        self.imprimir = Imprimir(self.matriz)
        
    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Ingrese el elemento ")))
            self.elementos.append(fila)    
    
    def lanzar(self):
        print("La matriz es: ")
        self.imprimir()
        print("La matriz traspuesta es: ")
        traspuesta_resultado = self.traspuesta.calcular_traspuesta()
        imprimir_traspuesta = Imprimir(traspuesta_resultado)
        imprimir_traspuesta.imprimir()
        
        
            
class Main():
    def __init__(self):
        self.lanzador = Lanzador()
        self.lanzador.lanzar()
        
if __name__ == "__main__":
    Main()
