import random

class Cliente:
    def __init__(self, id, h_llegada):
        self.id = id
        self.h_llegada = h_llegada
        self.tiempo_atencion = None

class Cola:
    def __init__(self):
        self.clientes = []

    def encolar(self, x):
        self.clientes.append(x)

    def desencolar(self):
        return self.clientes.pop(0)

    def es_vacia(self):
        return len(self.clientes) == 0

def simular(minutos):
    cola = Cola()
    cantidad_clientes = minutos  # Almacena la cantidad original de clientes en la cola

    for minuto in range(minutos):
        h_llegada = random.randint(1, 3)
        cliente = Cliente(id=minuto, h_llegada=h_llegada)
        cola.encolar(cliente)

    tiempo_esperaTotal = 0  # Mover esta línea fuera del bucle while

    while not cola.es_vacia():
        cliente = cola.desencolar()
        cliente.tiempo_atencion = minutos
        tiempo_espera = cliente.tiempo_atencion - cliente.h_llegada
        print(f"Cliente {cliente.id} esperó {tiempo_espera} minutos")

        tiempo_esperaTotal += tiempo_espera

    tiempo_esperaPromedio = tiempo_esperaTotal / cantidad_clientes

    print(f'El tiempo de espera promedio es de {tiempo_esperaPromedio} minutos')

# Llamada a la función simular con 60 minutos
simular(60)

