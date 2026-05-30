import pygame


class MotorAudio:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self.sonidos = {}

    def cargar(self, nombre, ruta):
        self.sonidos[nombre] = pygame.mixer.Sound(ruta)

    def reproducir(self, nombre, loop=False, pan=0.0):
        sonido = self.sonidos.get(nombre)
        if not sonido:
            return
        canal = pygame.mixer.find_channel()
        if canal:
            volumen_izq = min(1.0, 1.0 - pan) if pan > 0 else 1.0
            volumen_der = min(1.0, 1.0 + pan) if pan < 0 else 1.0
            canal.set_volume(volumen_izq, volumen_der)
            canal.play(sonido, loops=-1 if loop else 0)

    def detener_todo(self):
        pygame.mixer.stop()
