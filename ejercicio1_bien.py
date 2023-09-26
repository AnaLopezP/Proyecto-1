class Matriz():
    def __init__(self, elementos, list):
        self.elementos = elementos
        
        
class Traspuesta(Matriz):
    def __init__(self, elementos, list):
        super().__init__(elementos)
        
    def traspuesta(self):
        return Matriz( [[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))]) #es una buena opcion para elementos pequeños, pero si es grande peta. tendría que ser recursivo
    
class Imprimir(Matriz):
    def __init__(self, elementos, list):
        super().__init__(elementos)
        
    def imprimir(self):
        for fila in self.elementos:
            print(fila)
            