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
            if elemento not in resultado:
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
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass