from queue import PriorityQueue


class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, other):
        return self.prioridad < other.prioridad


def asignar_tareas(cola):
    tasks = []
    while not cola.empty():
        tarea = cola.get()
        tasks.append(tarea)

    # Print tasks in reverse order (highest to lowest priority)
    for tarea in reversed(tasks):
        print(f"Asignando tarea '{tarea.nombre}'")


cola = PriorityQueue()
cola.put(Tarea("Refactorizar código base", 3))
cola.put(Tarea("Implementar nueva característica A", 5))
cola.put(Tarea("Corregir error crítico B", 9))
cola.put(Tarea("Actualizar documentación", 2))
cola.put(Tarea("Revisar y aprobar PRs", 4))

asignar_tareas(cola)



#1. Asignación de Prioridad:
#Asigna una prioridad máxima al error de seguridad crítico.
#Esto puede implicar asignar la máxima prioridad posible en la cola de tareas.

#2. La manejaría por orden de Llegada o por duración estimada.

#3. Monitoreo y ajuste Continuo:
#Implementa un sistema de monitoreo continuo para identificar patrones
#y ajustar la implementación según sea necesario.