#Esqueleto de una aplicacion en python

class Candidato:
    def __init__(self, nombre, partido_politico, edad, sexo, educacion, experiencia_politica, propuestas, electo=False):
        self.nombre = nombre
        self.partido_politico = partido_politico
        self.edad = edad
        self.sexo = sexo
        self.educacion = educacion
        self.experiencia_politica = experiencia_politica
        self.propuestas = propuestas
        self.electo = electo

    def presentar_propuestas(self):
        print(f"Propuestas de {self.nombre}:")
        for propuesta in self.propuestas:
            print("- " + propuesta)

    def cantidad_mujeres(candidatos):
        cont = 0
        for candidato in candidatos:
            if candidato.sexo == "Mujer":
                cont += 1
        return cont

    def candidatos_reelectos(candidatos):
        cont = 0
        for candidato in candidatos:
            if candidato.electo:
                cont += 1
        return cont


class Senador(Candidato):
    def __init__(self, nombre, partido_politico, edad, sexo, educacion, experiencia_politica, propuestas, circunscripcion, comisiones, electo=False):
        super().__init__(nombre, partido_politico, edad, sexo, educacion, experiencia_politica, propuestas, electo)
        self.circunscripcion = circunscripcion
        self.comisiones = comisiones


class Diputado(Candidato):
    def __init__(self, nombre, partido_politico, edad, sexo, educacion, experiencia_politica, propuestas, distrito, proyectos_aprobados, electo=False):
        super().__init__(nombre, partido_politico, edad, sexo, educacion, experiencia_politica, propuestas, electo)
        self.distrito = distrito
        self.proyectos_aprobados = proyectos_aprobados


#Prueba de clases y metodos
candidatos = []

#Candidatos a senadores
senador1 = Senador("Paraguayo Cubas", "Cruzada Nacional", 58, "Hombre", "Licenciatura", "30 años", ["Abolir el parlamento", "Impuesto a la soja"], "Circunscripción 1", ["Comisión 1", "Comisión 2"], True)
candidatos.append(senador1)

senador2 = Senador("Carlos Galaverna", "Partido Colorado", 96, "Hombre", "Maestría", "70 años", ["Aumentar salario de parlamentarios", "Disminuir presupuesto en salud y educacion"], "Circunscripción 2", ["Comisión 3", "Comisión 4"], False)
candidatos.append(senador2)

#Candidatos a diputados
diputado1 = Diputado("Carlos Portillo", "Partido Colorado", 42, "Hombre", "Doctorado", "2 años", ["Clases de ingles obligatorias en instituciones de educacion publicas", "Acreditar todas las carreras universitarias de instituciones privadas"], "Distrito 1", 3, False)
candidatos.append(diputado1)

diputado2 = Diputado("Ruben Rubin", "Encuentro Nacional", 26, "Hombre", "Licenciatura", "20 años", ["Declarar la guerra a Argentina", "Aumentar el presupuesto militar"], "Distrito 2", 5, True)
candidatos.append(diputado2)

#Propuestas de todos los candidatos
for candidato in candidatos:
    candidato.presentar_propuestas()

#Cantidad de mujeres candidatas
cantidad_mujeres = Candidato.cantidad_mujeres(candidatos)
print("Cantidad de mujeres candidatas:", cantidad_mujeres)

# Obtener cantidad de candidatos reelectos
candidatos_reelectos = Candidato.candidatos_reelectos(candidatos)
print("Cantidad de candidatos reelectos:", candidatos_reelectos)