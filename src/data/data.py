class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """

    def invertir_lista(self, lista):
        resultado = []

        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])

        return resultado

    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i

        return -1

    def eliminar_duplicados(self, lista):
        resultado = []

        for elemento in lista:
            repetido = False

            for existente in resultado:
                if elemento == existente and type(elemento) == type(existente):
                    repetido = True
                    break

            if not repetido:
                resultado.append(elemento)

        return resultado

    def merge_ordenado(self, lista1, lista2):
        resultado = lista1 + lista2
        resultado.sort()
        return resultado

    def rotar_lista(self, lista, k):
        if not lista:
            return []

        k = k % len(lista)
        return lista[-k:] + lista[:-k]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        total = n * (n + 1) // 2
        return total - sum(lista)

    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False

        return True

    def implementar_pila(self):
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    def implementar_cola(self):
        cola = []

        def enqueue(elemento):
            cola.append(elemento)

        def dequeue():
            if cola:
                return cola.pop(0)
            return None

        def peek():
            if cola:
                return cola[0]
            return None

        def is_empty():
            return len(cola) == 0

        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }

    def matriz_transpuesta(self, matriz):
        return [list(fila) for fila in zip(*matriz)]