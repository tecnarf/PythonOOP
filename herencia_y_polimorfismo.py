#Para que haya herencia es necesario que la clase derivada cumpla la relación de es un/a de la clase base.
#La clase `Derivada` heredará TODOS los atributos y métodos de la clase `Base`.

#Definicion de la clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def hablar(self): #metodo polimorfico
        pass

#Definicion de las clases derivadas
class Perro(Animal):
    def __init__(self, nombre, edad, raza):#atributos de la clase base +  atributos propios de la clase derivada
        super().__init__(nombre, edad) #inicializacion de los atributos de la clase base pero que pertenece a la clase derivada
        self.raza=raza #inicializacion del atributo propio de la clase derivada
    def hablar(self):
        return "¡Guau, guau!"

class Gato(Animal):
    def __init__(self, nombre, edad, raza, color):
        super().__init__(nombre, edad)
        self.raza=raza
        self.color=color
    def hablar(self):
        return "Miau"

class Vaca(Animal):
    def __init__(self, nombre, edad, raza, peso):
        super().__init__(nombre, edad)
        self.raza=raza
        self.peso=peso
    def hablar(self):
        return "Muu"

mi_perro=Perro("Paco",2,"Salchicha")
mi_gato=Gato("Timo",4,"Mestizo","Café, negro y blanco")
mi_vaca=Vaca("Lola",4,"Holanda",300)

print("Tengo un perro", mi_perro.raza, "que se llama", mi_perro.nombre)
print("tambien tengo un gato de tres colores", mi_gato.color)
print("y una vaca lechera que se llama", mi_vaca.nombre )


#creamos objetos como elementos de una lista o los guardamos en una lista
animales=[Perro("Perry",8,"Caniche"), Gato("Pascual",4, "Mestizo", "Naranja"), Vaca("Lola",5,"Hereford",300)]

for animal in animales: #simplemente llamamos "animal" al indice de la lista de objetos "animales"
    print(animal.hablar())


