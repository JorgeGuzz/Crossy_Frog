import os
from PyQt5.QtCore import QRect

# Parametros Logica Juego
VIDAS_INICIO = 3
TIEMPO_AUTOS = 8000
TIEMPO_TRONCOS = 10000
TIEMPO_OBJETO = 7000
CANTIDAD_MONEDAS = 5

DURACION_RONDA_INICIAL = 200
VELOCIDAD_AUTOS = 50
VELOCIDAD_TRONCOS = 50
PONDERADOR_DIFICULTAD = 0.8

VELOCIDAD_CAMINAR = 50
PIXELES_SALTO = 50

VIDAS_TRAMPA = 3

# Parametros Ventana Inicio
MIN_CARACTERES = 4
MAX_CARACTERES = 12

# Parámetros generales y paths:
RUTA_UI_VENTANA_JUEGO = os.path.join("frontend", "ventana_juego.ui")
RUTA_UI_VENTANA_INICIO = os.path.join("frontend", "ventana_inicio.ui")
RUTA_UI_VENTANA_POST_NIVEL = os.path.join("frontend", "ventana_post_nivel.ui")
RUTA_UI_VENTANA_RANKINGS = os.path.join("frontend", "ventana_rankings.ui")

RUTA_FROGGY_STILL = os.path.join('sprites', 'Personajes', 'Verde', 'still.png')

RUTA_FROGGY_DOWN_1 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'down_1.png')
RUTA_FROGGY_DOWN_2 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'down_2.png')
RUTA_FROGGY_DOWN_3 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'down_3.png')

RUTA_FROGGY_LEFT_1 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'left_1.png')
RUTA_FROGGY_LEFT_2 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'left_2.png')
RUTA_FROGGY_LEFT_3 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'left_3.png')

RUTA_FROGGY_UP_1 = os.path.join('sprites', 'Personajes', 'Verde', 'up_1.png')
RUTA_FROGGY_UP_2 = os.path.join('sprites', 'Personajes', 'Verde', 'up_2.png')
RUTA_FROGGY_UP_3 = os.path.join('sprites', 'Personajes', 'Verde', 'up_3.png')

RUTA_FROGGY_RIGHT_1 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'right_1.png')
RUTA_FROGGY_RIGHT_2 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'right_2.png')
RUTA_FROGGY_RIGHT_3 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'right_3.png')

RUTA_FROGGY_JUMP_1 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'jump_1.png')
RUTA_FROGGY_JUMP_2 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'jump_2.png')
RUTA_FROGGY_JUMP_3 = os.path.join(
    'sprites', 'Personajes', 'Verde', 'jump_3.png')

RUTA_AUTO_LEFT = os.path.join('sprites', 'Mapa', 'autos', 'morado_left.png')
RUTA_AUTO_RIGHT = os.path.join('sprites', 'Mapa', 'autos', 'morado_right.png')

RUTA_TRONCO = os.path.join('sprites', 'Mapa', 'elementos', 'tronco.png')

RUTA_VIDA = os.path.join('sprites', 'Objetos', 'Corazon.png')
RUTA_MONEDA = os.path.join('sprites', 'Objetos', 'Moneda.png')
RUTA_CALAVERA = os.path.join('sprites', 'Objetos', 'Calavera.png')
RUTA_RELOJ = os.path.join('sprites', 'Objetos', 'Reloj.png')

# Bordes del mapa
BORDE_INFERIOR = QRect(0, 901, 1600, 0)
BORDE_SUPERIOR = QRect(0, 249, 1600, 0)
BORDE_IZQUIERDO = QRect(-1, 0, 0, 900)
BORDE_DERECHO = QRect(1601, 0, 0, 900)

BORDE_IZQUIERDO_RIO = QRect(-1, 500, 0, 150)
BORDE_DERECHO_RIO = QRect(1601, 500, 0, 150)

RIO = (QRect(-1, 501, 1600, 0), QRect(-1, 551, 1600, 0), QRect(-1, 601, 1600, 0))

META = QRect(-1, 251, 1700, 0)

# Tamaño froggy y entidades
FROGGY_ANCHO = 50
FROGGY_ALTO = 50

AUTOS_ANCHO = 100
AUTOS_ALTO = 50

TRONCOS_ANCHO = 100
TRONCOS_ALTO = 50

OBJETOS_ANCHO = 30
OBJETOS_ALTO = 30

SPAWN_X = 750
SPAWN_Y = 850

# Valores dependientes de inputs
CARRETERAS_Y = {
    '0': 300,
    '1': 350,
    '2': 400,
    '3': 700,
    '4': 750,
    '5': 800}

CARRETERAS_X = {
    'l': 1600,
    'r': -100}

TRONCOS_ORDEN = {
    'l': {0: 'l', 1: 'r', 2: 'l'},
    'r': {0: 'r', 1: 'l', 2: 'r'}}

TRONCOS_Y = {
    '0': 500,
    '1': 550,
    '2': 600}

TRONCOS_X = {
    'l': 1600,
    'r': -100}
