# Incluye una subclase DVD que no fue solicitado en el Taller  
# por cuestion de tiempo 

# Clase base Material
class Material:
    def __init__(self, titulo, costo_base):
        # Inicializa el título y el costo base del material
        self.titulo = titulo
        self.costo_base = costo_base
    
    def calcular_costo(self):
        # Método que retorna el costo base del material
        return self.costo_base

    def __str__(self):
        # Método que devuelve una representación en cadena del objeto
        return f"Material: {self.titulo}, Costo Base: {self.costo_base}"

# Subclase Libro que hereda de Material
class Libro(Material):
    def __init__(self, titulo, costo_base, autor):
        # Inicializa el título, costo base y autor del libro
        super().__init__(titulo, costo_base)
        self.autor = autor
    
    def __str__(self):
        # Método que devuelve una representación en cadena del libro
        return f"Libro: {self.titulo}, Autor: {self.autor}, Costo Base: {self.costo_base}"

# Subclase Revista que hereda de Material
class Revista(Material):
    def __init__(self, titulo, costo_base, numero_edicion):
        # Inicializa el título, costo base y número de edición de la revista
        super().__init__(titulo, costo_base)
        self.numero_edicion = numero_edicion
    
    def calcular_costo(self):
        # Método que calcula el costo total de la revista
        return self.costo_base + self.numero_edicion
    
    def __str__(self):
        # Método que devuelve una representación en cadena de la revista
        return f"Revista: {self.titulo}, Edición: {self.numero_edicion}, Costo Base: {self.costo_base}"

# Subclase DVD que hereda de Material
class DVD(Material):
    def __init__(self, titulo, costo_base, duracion):
        # Inicializa el título, costo base y duración del DVD
        super().__init__(titulo, costo_base)
        self.duracion = duracion
    
    def calcular_costo(self):
        # Método que calcula el costo total del DVD
        if self.duracion < 0:
            raise ValueError("La duración no puede ser negativa.")
        return self.costo_base + (0.05 * self.duracion)
    
    def __str__(self):
        # Método que devuelve una representación en cadena del DVD
        return f"DVD: {self.titulo}, Duración: {self.duracion} min, Costo Base: {self.costo_base}"

# Clase Biblioteca que gestiona una colección de materiales
class Biblioteca:
    def __init__(self):
        # Inicializa una lista vacía de materiales
        self.materiales = []
    
    def agregar_material(self, material):
        # Agrega un material a la colección
        self.materiales.append(material)
    
    def mostrar_materiales(self):
        # Muestra la lista de materiales en la biblioteca
        for material in self.materiales:
            print(material)
    
    def calcular_costo_total(self):
        # Calcula el costo total de todos los materiales en la colección
        costo_total = 0
        try:
            costo_total = sum(material.calcular_costo() for material in self.materiales)
        except ZeroDivisionError:
            print("Error: División por cero encontrada en el cálculo de costos.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return costo_total

def main():
    # Crear instancias de cada tipo de material
    libro = Libro("Cien años de soledad", 10, "Gabriel García Márquez")
    revista = Revista("National Geographic", 5, 120)
    dvd = DVD("Inception", 3, 148)
    
    # Crear una instancia de Biblioteca y agregar los materiales
    biblioteca = Biblioteca()
    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(dvd)
    
    # Mostrar la lista de materiales en la biblioteca
    biblioteca.mostrar_materiales()
    
    # Calcular y mostrar el costo total de los materiales
    try:
        costo_total = biblioteca.calcular_costo_total()
        print(f"Costo total de los materiales: {costo_total}")
    except Exception as e:
        print(f"Ocurrió un error al calcular el costo total: {e}")
    
    # Pruebas con datos que provoquen errores
    dvd_invalido = DVD("Error DVD", 3, -148)  # Duración negativa
    biblioteca.agregar_material(dvd_invalido)
    try:
        costo_total = biblioteca.calcular_costo_total()
        print(f"Costo total de los materiales después de agregar DVD inválido: {costo_total}")
    except Exception as e:
        print(f"Ocurrió un error al calcular el costo total después de agregar DVD inválido: {e}")

if __name__ == "__main__":
    main()
