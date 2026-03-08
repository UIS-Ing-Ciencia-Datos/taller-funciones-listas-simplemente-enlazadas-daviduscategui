# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# Clase Lista simplemente enlazada
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Lista vacía
    def vacio(self):
        if self.cabeza == None:
            print("Está vacía")
        else:
            print("Lista no vacía")

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    #Agregar antes de un elemento X
    def agregarAn(self,data,x):
        nuevo_nodo=Nodo(data)
        if self.cabeza is None:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            nodoesp=self.cabeza
            while nodoesp.siguiente is not None and nodoesp.siguiente.data!=x:
                nodoesp=nodoesp.siguiente
            nuevo_nodo.siguiente = nodoesp.siguiente
            nodoesp.siguiente = nuevo_nodo

    #Agregar despues de un elemento X
    def agregarDes(self,data,x):
        nuevo_nodo=Nodo(data)
        if self.cabeza is None:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            nodoesp=self.cabeza 
            while nodoesp.siguiente is not None and nodoesp.data!=x:
                nodoesp=nodoesp.siguiente 
            nuevo_nodo.siguiente=nodoesp.siguiente 
            nodoesp.siguiente=nuevo_nodo           
        
	#Agregar al final
    def agregarFin(self,data):
        nuevo_nodo=Nodo(data)
        if self.cabeza is None:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        else:
            nodoesp=self.cabeza
            while nodoesp.siguiente is not None:
                nodoesp=nodoesp.siguiente
            nodoesp.siguiente=nuevo_nodo
            return

    #Eliminar el primero
    def eliminarPrim(self):
        if self.cabeza is None:
            print("No hay nada que eliminar")
        eliminado=self.cabeza          
        self.cabeza=self.cabeza.siguiente  
        eliminado.siguiente=None

    #Eliminar el ultimo
    def eliminarUlt(self):
        nodoesp=self.cabeza
        if self.cabeza is None:
            print("No hay nada que eliminar")
        elif self.cabeza.siguiente is None:
            self.cabeza=None
        else:
            while nodoesp.siguiente.siguiente is not None:
                nodoesp=nodoesp.siguiente
            nodoesp.siguiente=None

    # Contador
    def contador(self):
        contador = 0
        nodoesp = self.cabeza
        while nodoesp != None:
            contador += 1
            nodoesp = nodoesp.siguiente
        return contador

    # Buscar elemento
    def buscador(self, valor):
        nodoesp = self.cabeza
        while nodoesp != None:
            if nodoesp.data == valor:
                return True
            nodoesp = nodoesp.siguiente
        return False

lista = ListaSE()
lista.agregarInicio(10)
lista.agregarInicio(20)
lista.agregarFin(50)
lista.agregarAn(80,20)
lista.eliminarPrim()
cont=lista.contador()
print(cont)
