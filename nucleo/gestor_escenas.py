class Escena:
    def iniciar(self, motor):
        pass

    def actualizar(self, motor, entrada):
        pass

    def cerrar(self):
        pass


class GestorEscenas:
    def __init__(self):
        self.escenas = {}

    def agregar(self, nombre, escena):
        self.escenas[nombre] = escena

    def iniciar(self, nombre, motor):
        escena = self.escenas.get(nombre)
        if escena:
            escena.iniciar(motor)
            while True:
                entrada = motor.entrada
                entrada.actualizar()
                escena.actualizar(motor, entrada)
