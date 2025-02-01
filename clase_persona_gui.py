"""
Este programa utiliza Tkinter para crear una interfaz gráfica
que permite cargar los datos de una persona (nombre, edad, y DNI).

tkinter es la biblioteca/libreria estándar de Python para crear interfaces
gráficas de usuario (GUIs).

"""


import tkinter as tk #se importa la  biblioteca tkinter y se le pone el alias tk
                     #el alias es solo para comodidad al momento de escribrir codigo
                     #que involucre a la libreria tkinter
                     #tkinter es una que contiene varias clases y funciones
                     #que puedes usar para crear y gestionar elementos de la interfaz gráfica,
                     #como ventanas, botones, etiquetas, etc
                     #tkinter no es una única clase, se puede entender que proporciona varias clases
                     #que encapsulan el comportamiento y las propiedades necesarias para construir GUIs.
                     #Por ejemplo, dentro de tkinter, hay clases como Tk (para la ventana principal),
                     #Label (para etiquetas de texto), Button (para botones), entre otras.


class Persona:
    #Las lineas abajo corresponden al constructor de la clase.
    #Inicializa los atributos nombre, edad, y dni
    #con valores predeterminados ("" para texto y 0 para números).
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    #Setters y Getters:
    #Métodos para asignar (set) y obtener (get)
    #los valores de los atributos. Por ejemplo:
    #setNombre: Establece el nombre de la persona.
    #getNombre: Devuelve el nombre de la persona.
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    
    def setEdad(self, edad): #Establece si la edad es un valor positivo.
                             #Si no lo es, muestra un mensaje de error.
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un valor positivo.")
    def getEdad(self):
        return self.edad
    
    def setDNI(self, dni): #Establece si el DNI tiene 7 caracteres
                           #o menos. Si es mayor,
                           #muestra un mensaje de error.

        if len(dni) <= 7: #La función len() en Python es
                          #una de las funciones integradas
                          #más utilizadas.
                          #Sirve para obtener la longitud
                          #o el número de elementos de un objeto
                          #como una lista, cadena, tupla, diccionario,
                          #conjunto, entre otros.
            self.dni = dni
        else:
            print("El DNI debe tener al menos 7 dígitos.") 
    def getDNI(self):
        return self.dni
    
    def mostrar(self): #Imprime en consola los datos de la persona.
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def esMayorDeEdad(self): #Devuelve True si la persona tiene 18 años
                             #o más; de lo contrario, devuelve False.
        if self.edad >= 18:
            return True
        else:
            return False

"""
Clase InterfazCargaPersonas:
Esta clase utiliza Tkinter para crear la interfaz gráfica
que permite cargar los datos de una persona.

"""

class InterfazCargaPersonas: #la clase InterfazCargaPersonas y su constructor
    def __init__(self):
        self.ventana = tk.Tk() #crea una ventana principal(comando tk.Tk()) y se guarda en "ventana"
        #tk.Tk() es la forma que tenemos de usar los componentes de la libreria tkinter
        #debido a la manera en la que importamos esta libreria
        #esta linea de instancia un objeto de la clase Tk() y la guarda en un atributo
        #de la clase InterfazCargaPersona llamado ventana
        #se esta creando la ventana que permite el ingreso de los datos personales

        self.ventana.title("Carga de Personas") #establece su título a "Carga de Personas".
        #Crea una etiqueta y un campo de entrada para el nombre, y los empaqueta en la ventana.
        self.label_nombre = tk.Label(self.ventana, text="Nombre:")#es un atributo mas de la clase
        self.label_nombre.pack()#se empaqueta la etiqueta en la ventana
        self.entry_nombre = tk.Entry(self.ventana)#se crea un campo para nombre
        self.entry_nombre.pack()#se empaqueta el campo en la ventana
        
        self.label_edad = tk.Label(self.ventana, text="Edad:")
        self.label_edad.pack()
        self.entry_edad = tk.Entry(self.ventana)
        self.entry_edad.pack()
        
        self.label_dni = tk.Label(self.ventana, text="DNI:")
        self.label_dni.pack()
        self.entry_dni = tk.Entry(self.ventana)
        self.entry_dni.pack()
        
        #Crea un botón con el texto "Cargar" que, al ser presionado, llama al método cargar_persona  de la clase InterfazCargaPersonas.
        #Empaqueta el botón en la ventana.
        self.boton_cargar = tk.Button(self.ventana, text="Cargar", command=self.cargar_persona)
        self.boton_cargar.pack()

        #Inicia el bucle(instruccion o conjunto de instrucciones que se repiten) principal de eventos de Tkinter,
        #lo que hace que la ventana esté operativa.
        self.ventana.mainloop()
    
    def cargar_persona(self):#un metodo de la clase InterfazCargaPersonas
                             #Define el método cargar_persona, que se ejecuta cuando el botón "Cargar" es presionado.
                             #Este método obtiene los valores ingresados en los campos de entrada (get())
                             #crea un objeto Persona y le asigna los valores obtenidos.
                             #Luego, llama al método mostrar de la clase Persona para imprimir los datos en la consola.
        nombre = self.entry_nombre.get()
        edad = int(self.entry_edad.get())
        dni = self.entry_dni.get()
        
        persona = Persona()
        persona.setNombre(nombre)
        persona.setEdad(edad)
        persona.setDNI(dni)
        
        persona.mostrar()

#Crea una instancia de la clase InterfazCargaPersonas, lo que inicia la interfaz gráfica.
interfaz = InterfazCargaPersonas()
