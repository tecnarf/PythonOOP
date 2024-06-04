
#Clase: Una clase es una plantilla o modelo que define las propiedades (atributos) y comportamientos (métodos) de un objeto.
#Es la unidad básica de la POO.

#Objeto: Un objeto es una instancia de una clase. Cada objeto tiene sus propios atributos y métodos.

#Atributos: Los atributos son las características o propiedades de un objeto, como su color, tamaño, nombre, etc.

#Métodos: Los métodos son las acciones o comportamientos que un objeto puede realizar, como moverse, imprimir algo, calcular algo, etc.


class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad

    def ladrar(self):
        print("¡Guau, guau!")

    def correr(self):
        print(f"{self.nombre} esta corriendo")

#creamos un objeto de la clase perro y usamos sus metodos
mi_perro=Perro("Paco", "Salchicha", 2)
print("Mi perro se llama ",mi_perro.nombre)
print("es de la raza ", mi_perro.raza)
print("y tiene ", mi_perro.edad, "años")

#usamos los metodos del objeto
mi_perro.ladrar() #salida: ¡Guau, guau!
mi_perro.correr()  #salida: Paco esta corriendo

