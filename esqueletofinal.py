#Esqueleto de pequeñas aplicaciones de python

class ClaseBase:
    def __init__(self, atributo_base1, atributo_base2):
        self.atributo_base1 = atributo_base1
        self.atributo_base2 = atributo_base2
    
    def metodo_base1(self):
       pass
       
    def metodo_abstracto(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    def mostrar_informacion(self):
        print(f"Atributo_base1: {self.atributo_base1}")
        print(f"Atributo_base2: {self.atributo_base2}")
    
class ClaseDerivada1(ClaseBase):
    def __init__(self, atributo_base1, atributo_base2, atributo1_derivada1):
        super().__init__(atributo_base1, atributo_base2)
        self.atributo1_derivada1 = atributo1_derivada1

    def metodo1_derivada1(self):
        try:
            return self.atributo_base1 * atributo_base2
        except ZeroDivisionError:
            return "Error Division por cero"

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Atributo1_derivada1: {self.atributo_derivada11}")
        print(f"Resultado_metodo1_derivada1: {self.metodo1_derivada1()}")

    def __add__(self, otra_derivada1):
        if isinstance(otra_derivada1, ClaseDerivada1):
            nuevo_atributo_base1= self.atributo_base1 + otra_derivada1.atributo_base1
            nuevo_atributo_base2 = self.atributo_base2 + otra_derivada1.atributo_base2
            nuevo_atributo_derivada1 = self.atributo_derivada1 + otra_derivada1.atributo_derivada1
            return ClaseDerivada1(nuevo_atributo_base1, nuevo_atributo_base2, nuevo_atributo_derivada1)
        else:
            raise TypeError("Solo se pueden sumar dos ondas electromagnéticas")   
            
class ClaseDerivada2(ClaseBase):
    def __init__(self, atributo_base1, atributo_base2, atributo1_derivada2):
        super().__init__(atributo_base1, atributo_base2)
        self.atributo1_derivada2 = atributo1_derivada2
        
    def metodo1_derivada2(self):
        return 343

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"<Resultado de metodo1_derivada2: {self.metodo1_derivada2()}")
 
def guardar_onda_en_archivo(objeto_claseBase, nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Atributo_base1: {objeto_claseBase.atributo_base1}")
            archivo.write(f"Atributo_base2: {objeto_claseBase.atributo_base2}")
            if isinstance(objeto_claseBase, ClaseDerivada1):
                archivo.write(f"Atributo1_derivada1: {objeto_claseBase.atributo1_derivada1}\n")
                archivo.write(f"Resultado_metodo1_derivada1: {objeto_claseBase.metodo1_derivada1()}\n")
    except Exception as e:
        print(f"Error al guardar la información en el archivo: {e}") 
        
def cargar_onda_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = archivo.readlines()
            atributo_base1 = float(datos[0].split(":")[1].strip().split()[0])
            atributo_base2 = float(datos[1].split(":")[1].strip().split()[0])
            if len(datos) == 4: 
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

# Ejemplo de uso 
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
