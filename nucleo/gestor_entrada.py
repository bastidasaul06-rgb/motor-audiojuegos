import pygame


class GestorEntrada:
    def __init__(self):
        pygame.init()
        self._teclas = {}

    def actualizar(self):
        self._teclas = {}
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                self._teclas[evento.key] = True
            elif evento.type == pygame.QUIT:
                self._teclas[pygame.K_ESCAPE] = True

    def presiono(self, tecla):
        return self._teclas.get(tecla, False)

    def esperar_tecla(self):
        while True:
            self.actualizar()
            for tecla in self._teclas:
                return tecla
