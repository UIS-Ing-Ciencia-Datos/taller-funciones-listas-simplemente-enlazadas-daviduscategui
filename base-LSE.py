# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
			
    #Contador 
		contador=0
		def contador(self):
			if self.cabeza==None:
				return 0
			else:
				nodoesp=self.cabeza
				while nodoesp!=None:
					contador+=1
					nodoesp=nodoesp.siguiente
					return contador

    #Buscar un elemento
		def buscador(self,data):
			cent=input(int("Ingrese el elemento a buscar: "))
			if self.cabeza==None:
				return False
			else:
				nodoesp=self.cabeza
				while nodoesp!=cent:
					nodoesp=nodoesp.siguiente
					if nodoesp==None:
						return False
					
          
lista = ListaSE()
lista.agregarInicio(10)
lista.agregarInicio(20)
cont=lista.contador()
print(cont)
