class Usuario:
    def __init__(self, nombre, apellido, direccion, telefono, email, password, n_pedido, dinero):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.dinero = dinero
        self.direccion = direccion
        self.telefono = telefono
        self.n_pedido = n_pedido
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Password: {self.password}, Dinero: {self.dinero}, Direccion: {self.direccion}, Telefono: {self.telefono}, Numero de pedido: {self.n_pedido}"
    
    def to_dict(self):
        return {"nombre": self.nombre, "apellido": self.apellido, "direccion": self.direccion, "telefono": self.telefono, "email": self.email, "password": self.password, "dinero": self.dinero, "n_pedido": self.n_pedido}