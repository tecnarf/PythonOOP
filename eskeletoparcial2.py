# Clase base Habitacion
class Habitacion:
    def __init__(self, numero, capacidad, precio):
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio

    def descripcion(self):
        print(f"Habitación {self.numero}: Capacidad para {self.capacidad} personas, Precio por noche: ${self.precio}")

# Clase Estandar que hereda de Habitacion
class Estandar(Habitacion):
    def __init__(self, numero, capacidad, precio, tiene_tv):
        super().__init__(numero, capacidad, precio)
        self.tiene_tv = tiene_tv

    def descripcion(self):
        tv = "sí" if self.tiene_tv else "no"
        print(f"Habitación Estándar {self.numero}: Capacidad para {self.capacidad} personas, Precio por noche: ${self.precio}, TV: {tv}")

# Clase Suite que hereda de Habitacion
class Suite(Habitacion):
    def __init__(self, numero, capacidad, precio, tiene_jacuzzi):
        super().__init__(numero, capacidad, precio)
        self.tiene_jacuzzi = tiene_jacuzzi

    def descripcion(self):
        jacuzzi = "sí" if self.tiene_jacuzzi else "no"
        print(f"Habitación Suite {self.numero}: Capacidad para {self.capacidad} personas, Precio por noche: ${self.precio}, Jacuzzi: {jacuzzi}")

# Clase Familiar que hereda de Habitacion
class Familiar(Habitacion):
    def __init__(self, numero, capacidad, precio, numero_de_camas):
        super().__init__(numero, capacidad, precio)
        self.numero_de_camas = numero_de_camas

    def descripcion(self):
        print(f"Habitación Familiar {self.numero}: Capacidad para {self.capacidad} personas, Precio por noche: ${self.precio}, Número de camas: {self.numero_de_camas}")

# Lista de habitaciones
habitaciones = [
    Estandar(101, 2, 100000, True),
    Estandar(102, 2, 100000, False),
    Suite(201, 4, 200000, True),
    Familiar(301, 6, 150000, 3)
]

# Usar polimorfismo para describir cada habitación
for habitacion in habitaciones:
    habitacion.descripcion()

# Función para guardar habitaciones en un archivo
def guardar_reservas(habitaciones, nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as file:
            for habitacion in habitaciones:
                if isinstance(habitacion, Estandar):
                    tipo = "Estandar"
                    detalles = f"{habitacion.numero},{habitacion.capacidad},{habitacion.precio},{habitacion.tiene_tv}"
                elif isinstance(habitacion, Suite):
                    tipo = "Suite"
                    detalles = f"{habitacion.numero},{habitacion.capacidad},{habitacion.precio},{habitacion.tiene_jacuzzi}"
                elif isinstance(habitacion, Familiar):
                    tipo = "Familiar"
                    detalles = f"{habitacion.numero},{habitacion.capacidad},{habitacion.precio},{habitacion.numero_de_camas}"
                file.write(f"{tipo},{detalles}\n")
        print("Reservas guardadas exitosamente.")
        file.close()
        print("")
    except IOError as e:
        print(f"Error al guardar las reservas: {e}")

# Función para cargar habitaciones desde un archivo
def cargar_reservas(nombre_archivo):
    habitaciones = []
    try:
        with open(nombre_archivo, 'r') as file:
            for linea in file:
                datos = linea.strip().split(',')
                tipo = datos[0]
                numero = int(datos[1])
                capacidad = int(datos[2])
                precio = float(datos[3])
                if tipo == "Estandar":
                    tiene_tv = datos[4] == "True"
                    habitaciones.append(Estandar(numero, capacidad, precio, tiene_tv))
                elif tipo == "Suite":
                    tiene_jacuzzi = datos[4] == "True"
                    habitaciones.append(Suite(numero, capacidad, precio, tiene_jacuzzi))
                elif tipo == "Familiar":
                    numero_de_camas = int(datos[4])
                    habitaciones.append(Familiar(numero, capacidad, precio, numero_de_camas))
        print("Reservas cargadas exitosamente.")
        file.close()
    except FileNotFoundError:
        print("Error: El archivo de reservas no se encuentra.")
    except IOError as e:
        print(f"Error al leer el archivo de reservas: {e}")
    except ValueError as e:
        print(f"Error en el formato de los datos: {e}")
    return habitaciones

# Demostración de la funcionalidad de guardar y cargar
guardar_reservas(habitaciones, 'reservas.txt')

habitaciones_cargadas = cargar_reservas('reservas.txt')
for hab in habitaciones_cargadas:
    hab.descripcion()
