# motor-audiojuegos

Motor de audiojuegos en Python. Todo sonido, nada de gráficos.

Reproduce sonidos con panning estéreo para crear la ilusión de posición espacial, ideal para juegos accesibles a usuarios ciegos.

## Requisitos

```
pip install -r requerimientos.txt
```

## Estructura

```
motor-audiojuegos/
├── nucleo/
│   ├── motor_audio.py     → Carga y reproduce sonidos con paneo estéreo
│   ├── gestor_escenas.py  → Ciclo de escenas (menú, juego, fin)
│   ├── gestor_entrada.py  → Captura de teclado
│   └── utilidades.py      → Rutas y helpers
├── recursos/
│   ├── sonidos/           → Coloca aquí tus archivos .wav
│   └── config/
├── requerimientos.txt
└── README.md
```

## Uso básico

```python
from nucleo import MotorAudio, GestorEntrada, Escena, GestorEscenas

class MiEscena(Escena):
    def iniciar(self, motor):
        motor.audio.cargar("disparo", "ruta/al/sonido.wav")
        motor.audio.reproducir("disparo", pan=-0.5)

    def actualizar(self, motor, entrada):
        if entrada.presiono(32):
            print("disparaste")

motor = MotorAudio()
entrada = GestorEntrada()
gestor = GestorEscenas()
gestor.agregar("menu", MiEscena())
gestor.iniciar("menu", motor)
```

## Licencia

GPL-3.0
