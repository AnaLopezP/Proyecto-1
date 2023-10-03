'''Estás creando un sistema de gestión de pedidos de pizza en línea utilizando Python. Este sistema consta de varios componentes que interactúan entre sí. Los componentes principales son:

DataBaseManager: Esta clase es responsable de manejar la conexión con la base de datos y realizar operaciones CRUD.

Authenticator: Esta clase se utiliza para manejar la autenticación de usuarios, posiblemente utilizando un servicio externo o una base de datos local.

OrderManager: Esta clase se encarga de la gestión de los pedidos, incluyendo la creación, actualización, y eliminación de los pedidos de los usuarios.

PaymentProcessor: Esta clase es responsable de manejar las transacciones de pago, utilizando un servicio de procesamiento de pagos externo.'''
#cada movida de estas aqui arriba es una clase distinta. 
#DataBaseManager tiene que tener: get, put, delete, y otro que no me acuerdo
#aythenticator: nombre, apellidos, telefono, email, pagos. Esto es la base del modelo. Dos métodos, log in y register. Tiene que apuntar al DataBaseManager
#ordenManager: 
#paymentProcessor
#hay que hacer al menos 4 apis por lo siguiente. 
'''Estos componentes no deben crearse ni gestionarse dentro de cada clase que los utiliza, 
sino que deben ser creados en algún lugar centralizado y "inyectados" en las clases que los necesitan.
'''
#habría que hacer uml (recomendación) con clases, atributos, métodos, y con que inyectan y heredan.

'''Tu tarea es implementar este sistema utilizando el concepto de inyección de dependencias. 
Debes definir cada clase y sus dependencias, luego inyectar las dependencias a través de los constructores 
de las clases. Por ejemplo, la clase OrderManager debería recibir instancias de DataBaseManager,
Authenticator, y PaymentProcessor a través de su constructor.
'''
#Ejemplo: A depende de B, entonces A tiene en su constructor B

'''Al implementar este sistema, considera los siguientes aspectos:

Desacoplamiento de las clases: Las clases no deben crear sus propias dependencias. 
En lugar de eso, deben recibir las dependencias ya creadas. Esto promueve un código más limpio y modular.

Pruebas: La inyección de dependencias debe facilitar las pruebas de las clases.
Deberías poder crear "mocks" o "stubs" de las dependencias para probar las clases de manera aislada.

Reutilización de código: Si varias clases necesitan la misma dependencia, 
no debes crear una nueva instancia para cada una. En lugar de eso, crea una instancia de la dependencia y 
pásala a todas las clases que la necesiten.'''

'''Estás creando un sistema de gestión de pedidos de pizza en línea utilizando Python. Este sistema consta de varios componentes que interactúan entre sí. Los componentes principales son:

DataBaseManager: Esta clase es responsable de manejar la conexión con la base de datos y realizar operaciones CRUD.

Authenticator: Esta clase se utiliza para manejar la autenticación de usuarios, posiblemente utilizando un servicio externo o una base de datos local.

OrderManager: Esta clase se encarga de la gestión de los pedidos, incluyendo la creación, actualización, y eliminación de los pedidos de los usuarios.

PaymentProcessor: Esta clase es responsable de manejar las transacciones de pago, utilizando un servicio de procesamiento de pagos externo.

Estos componentes no deben crearse ni gestionarse dentro de cada clase que los utiliza, sino que deben ser creados en algún lugar centralizado y "inyectados" en las clases que los necesitan.

Tu tarea es implementar este sistema utilizando el concepto de inyección de dependencias. Debes definir cada clase y sus dependencias, luego inyectar las dependencias a través de los constructores de las clases. Por ejemplo, la clase OrderManager debería recibir instancias de DataBaseManager, Authenticator, y PaymentProcessor a través de su constructor.

Al implementar este sistema, considera los siguientes aspectos:

Desacoplamiento de las clases: Las clases no deben crear sus propias dependencias. En lugar de eso, deben recibir las dependencias ya creadas. Esto promueve un código más limpio y modular.

Pruebas: La inyección de dependencias debe facilitar las pruebas de las clases. Deberías poder crear "mocks" o "stubs" de las dependencias para probar las clases de manera aislada.

Reutilización de código: Si varias clases necesitan la misma dependencia, no debes crear una nueva instancia para cada una. En lugar de eso, crea una instancia de la dependencia y pásala a todas las clases que la necesiten.

Para concluir, debes demostrar cómo crearías las instancias de las dependencias y cómo las inyectarías en las clases que las necesitan. Asegúrate de que tu implementación sea robusta, fácil de entender y fácil de mantener.

Aquí está cómo se podrían ver nuestras clases:'''


class DataBaseManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string

class Authenticator:
    def __init__(self, user_database):
        self.user_database = user_database

class PaymentProcessor:
    def __init__(self, api_key):
        self.api_key = api_key

class OrderManager:
    def __init__(self, database_manager, authenticator, payment_processor):
        self.database_manager = database_manager
        self.authenticator = authenticator
        self.payment_processor = payment_processor

#Ahora, en lugar de crear las instancias de las dependencias dentro de la OrderManager, puedes crearlas en algún lugar centralizado y pasarlas como argumentos al constructor de la OrderManager.


# Crear instancias de nuestras dependencias
database_manager = DataBaseManager("my-database-connection-string")
authenticator = Authenticator(database_manager)
payment_processor = PaymentProcessor("my-payment-api-key")

# Crear una instancia de OrderManager, pasando nuestras dependencias
order_manager = OrderManager(database_manager, authenticator, payment_processor)