class Correo_electronico:
    
    emisor: str
    receptor: str
    mensaje: str

    def __init__(self, emisor: str, receptor: str, mensaje: str) -> None:
        self.emisor=emisor
        self.receptor=receptor
        self.mensaje=mensaje

    def __str__(self) -> str:
       return  f"***Correo Electronico***\nDe: {self.emisor}\nPara: {self.receptor}\nMensaje: {self.mensaje}"
        

c1=Correo_electronico("guillermopuertas@correo.com","estebantrabajos@correo.com","Hola")
print(c1)

