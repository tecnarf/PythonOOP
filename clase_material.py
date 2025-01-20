class Material:
    def __init__(self, titulo, costo_base):
        self.titulo=titulo
        self.costo_base=costo_base

    def calcular_costo(self):
        return self.costo_base

    def __str__(self): #funcion especial que puede retornar
                       #todos los atributos de la clase
                       #con solo print(nombre del objeto)
        return f"Material: {self.titulo} - Costo Base: {self.costo_base}"

class Libro(Material):
    def __init__(self, titulo, costo_base, autor):
        super().__init__(titulo, costo_base)
        self.autor=autor

    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - Costo Base: {self.costo_base}"

class Revista(Material):
    def __init__(self, titulo, costo_base, numero_edicion):
        super().__init__(titulo, costo_base)
        self.numero_edicion=numero_edicion

    def calcular_costo(self):#es redefinido la implementacion del metodo
                             #calcular_costo de la superclase Material
        return self.costo_base + self.numero_edicion

    def __str__(self):
        return f"Revista: {self.titulo} - Edicion: {self.numero_edicion} - Costo Base: {self.costo_base}"

class DVD(Material):
    def __init__(self, titulo, costo_base, duracion):
        super().__init__(titulo, costo_base)
        self.duracion=duracion

    def calcular_costo(self):
        if self.duracion < 0:
            raise ValueError("Duracion no valida")
        return self.costo_base + self.duracion

    def __str__(self):
        return f"DVD: {self.titulo} - Duracion: {self.duracion} min - Costo Base: {self.costo_base}"

    
material_1=Material("La Biblia Latinoamerica", 60000)
print(material_1)
print(material_1.calcular_costo())

libro_1=Libro("Fisica Universitaria", 150000, "Sears & Zemansky",)
print(libro_1)
print(libro_1.calcular_costo())

revista_1=Revista("Popular Electronics", 40000, 1)
print(revista_1)
print(revista_1.calcular_costo())

dvd_1=DVD("Cosmos",  15000, 1200)
print(dvd_1)
print(dvd_1.calcular_costo())



































