class Asignatura:
    nombre = ""
    salon = ""

    def __init__(self, nombre="Nombre Determinado", salon="remoto"):
        self.nombre = nombre
        self.salon = salon

    def __str__(self):
        return(f"{self.nombre} {self.salon}")
