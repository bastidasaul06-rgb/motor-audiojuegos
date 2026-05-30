import os


def ruta_recurso(ruta_relativa):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, ruta_relativa)
