class Pedido:
    def __init__(self,cliente, pizza, tamaño, ingredientes, precio):
        self.cliente = cliente
        self.tamaño = tamaño
        self.pizza = pizza
        self.ingredientes = ingredientes
        self.precio = precio