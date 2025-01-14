class Dispositivo:
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    def encender(self):
        self.estado = True
        print(f"{self.nombre} ha sido encendido")
    def apagar(self):
        self.estado = False
        print(f"{self.nombre} ha sido apagado")
    def __str__(self):
        return f"{self.nombre} - Estado: {"Encendido" if self.estado else "Apagado"}"

dispositivo_1 = Dispositivo("Acondicionador de Aire", False)
dispositivo_2 = Dispositivo("Televisor", False)
dispositivo_3 = Dispositivo("Radio", True)
print(dispositivo_1.nombre)
print(dispositivo_1.estado)
print(dispositivo_2.nombre)
print(dispositivo_2.estado)
print(dispositivo_3)
#print(dispositivo_3.__str__()) es una alternativa a la linea anterior pero sin uso


        
"""
dispositivo es todo lo que encontramos en un dormitorio

class Lampara(Dispositivo):
class Acondicionador(Dispositivo):
class Termostato(Dispositivo):
class Televisor(Dispositivo):
class Radio(Dispositivo):
class Reloj(Dispositivo):

"""
    
