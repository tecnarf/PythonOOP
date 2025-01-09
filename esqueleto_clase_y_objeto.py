#Esqueleto de clase y su instancia(objeto) en Python

class MiClase:
	def __init__(self, atributo1_miclase, atributo2_miclase):
		self.atributo1_miclase=atributo1_miclase
		self.atributo2_miclase=atributo2_miclase
    def metodo1_miclase(self):
        pass
    def metodo2_miclase(self):
        pass
    
#Instancia de la clase
miObjeto1=miClase("valor_atributo1_miclase", "valor_atributo2_miclase")

print(miObjeto1.atributo1_miclase)
print(miObjeto1.atributo2_miclase)

miObjeto1.metodo1_miclase()
miObjeto1.metodo2_miclase()


