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
