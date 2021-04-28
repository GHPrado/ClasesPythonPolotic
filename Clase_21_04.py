
#EJERCICIO 1
class Rectangulo:

    #Atributo de clase
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    #Calculo area
    def calculo(self):
        area = self.longitud*self.ancho
        return f"el area del rectangulo es {area}"

#EJERCICIO 2
class Vehiculo:
    
    pasajeros = []

    def agregar_pasajero(self,nombre):
        if not self.disponibles():
            return False
        else:
            if nombre in self.pasajeros:
                return False
            else:
                self.pasajeros.append(nombre)
                return True

    def disponibles(self):
        return 50 - len(self.pasajeros)

class Minibus(Vehiculo):
    def __init__(self,capacidad=6):
        self.capacidad=capacidad



class Perro:

    #Atributo de clase
    especie = "Canis lupus familiaris"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Metodo de instancia
    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años"
    
    #Otro metodo de instancia
    def ladrar(self, sonido):
        return f"{self.nombre} dice {sonido}"



