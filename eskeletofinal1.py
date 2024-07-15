class Onda:
    def __init__(self, frecuencia, amplitud):
        self.frecuencia = frecuencia
        self.amplitud = amplitud

    def velocidad_propagacion(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    def mostrar_informacion(self):
        print(f"Frecuencia: {self.frecuencia} Hz")
        print(f"Amplitud: {self.amplitud}")


class OndaElectromagnetica(Onda):
    def __init__(self, frecuencia, amplitud, longitud_onda):
        super().__init__(frecuencia, amplitud)
        self.longitud_onda = longitud_onda

    def velocidad_propagacion(self):
        try:
            return self.frecuencia * self.longitud_onda
        except ZeroDivisionError:
            return "Error: División por cero al calcular la velocidad de propagación."

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Longitud de Onda: {self.longitud_onda} m")
        print(f"Velocidad de Propagación: {self.velocidad_propagacion()} m/s")

    def __add__(self, otra_onda):
        if isinstance(otra_onda, OndaElectromagnetica):
            nueva_frecuencia = (self.frecuencia + otra_onda.frecuencia) / 2
            nueva_amplitud = self.amplitud + otra_onda.amplitud
            nueva_longitud_onda = (self.longitud_onda + otra_onda.longitud_onda) / 2
            return OndaElectromagnetica(nueva_frecuencia, nueva_amplitud, nueva_longitud_onda)
        else:
            raise TypeError("Solo se pueden sumar dos ondas electromagnéticas")


class OndaSonora(Onda):
    def velocidad_propagacion(self):
        return 343

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Velocidad de Propagación: {self.velocidad_propagacion()} m/s")


def guardar_onda_en_archivo(onda, nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Frecuencia: {onda.frecuencia} Hz\n")
            archivo.write(f"Amplitud: {onda.amplitud}\n")
            if isinstance(onda, OndaElectromagnetica):
                archivo.write(f"Longitud de Onda: {onda.longitud_onda} m\n")
            archivo.write(f"Velocidad de Propagación: {onda.velocidad_propagacion()} m/s\n")
    except Exception as e:
        print(f"Error al guardar la información en el archivo: {e}")


def cargar_onda_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = archivo.readlines()
            frecuencia = float(datos[0].split(":")[1].strip().split()[0])
            amplitud = float(datos[1].split(":")[1].strip().split()[0])
            if len(datos) == 4:  # OndaElectromagnetica
                longitud_onda = float(datos[2].split(":")[1].strip().split()[0])
                onda = OndaElectromagnetica(frecuencia, amplitud, longitud_onda)
            else:  # OndaSonora
                onda = OndaSonora(frecuencia, amplitud)
            return onda
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print(f"Error al leer la información del archivo: {e}")
        return None


# Ejemplo de uso visual y detallado
def ejemplo_uso():
    print("Creando dos ondas electromagnéticas:")
    onda_em1 = OndaElectromagnetica(5e14, 1.0, 6e-7)
    onda_em2 = OndaElectromagnetica(6e14, 0.5, 5e-7)
    
    print("\nInformación de la primera onda electromagnética:")
    onda_em1.mostrar_informacion()
    
    print("\nInformación de la segunda onda electromagnética:")
    onda_em2.mostrar_informacion()
    
    print("\nSumando las dos ondas electromagnéticas:")
    onda_em_suma = onda_em1 + onda_em2
    
    print("\nInformación de la onda resultante de la suma:")
    onda_em_suma.mostrar_informacion()
    
    print("\nGuardando la información de la onda resultante en un archivo llamado 'onda_em_suma.txt':")
    guardar_onda_en_archivo(onda_em_suma, 'onda_em_suma.txt')
    
    print("\nCargando la onda desde el archivo 'onda_em_suma.txt' y mostrando su información:")
    onda_cargada = cargar_onda_desde_archivo('onda_em_suma.txt')
    if onda_cargada:
        print("\nInformación de la onda cargada desde el archivo:")
        onda_cargada.mostrar_informacion()
    else:
        print("\nNo se pudo cargar la onda desde el archivo.")

ejemplo_uso()
