#gestiona los clientes y los pedidos (controlador) 
#hay que trabajar con hilos.
#clientes y pedidios aleatorios, se guardan en un fichero csv, que es la base de datos
from Autenticador import Autenticador
from  Usuario import Usuario
import csv
import config

class DataBaseManager:
