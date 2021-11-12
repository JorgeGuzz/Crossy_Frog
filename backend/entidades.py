from PyQt5.QtCore import QObject, QRect
import parametros as p


class Froggy(QObject):

    def __init__(self):
        super().__init__()
        self.direccion = 'D'
        self.x = p.SPAWN_X
        self.y = p.SPAWN_Y
        self.alto = p.FROGGY_ALTO
        self.ancho = p.FROGGY_ANCHO
        self.velocidad = p.VELOCIDAD_CAMINAR
        self.distancia_salto = p.PIXELES_SALTO
        self.tronco_bool = False
        self.tronco = None
        self.actualizar_hitbox()

    def actualizar_hitbox(self):
        self.hitbox = QRect(self.x, self.y, self.ancho, self.alto)

    def simular_movimiento(self, direccion, hitbox):
        if direccion in 'URDL':
            self.moverse(direccion, hitbox)
            self.direccion = direccion
        elif direccion == 'SALTO':
            self.saltar(hitbox)

    def respawnear(self):
        self.x = p.SPAWN_X
        self.y = p.SPAWN_Y
        self.actualizar_hitbox()

    def sobre_tronco(self, tronco):
        self.x += tronco.dx[str(tronco.sentido)]
        self.actualizar_hitbox()


class Auto(QObject):

    def __init__(self, x_inicial, y_inicial, sentido, velocidad):
        super().__init__()
        self.x = x_inicial
        self.y = y_inicial
        self.sentido = sentido
        self.alto = p.AUTOS_ALTO
        self.ancho = p.AUTOS_ANCHO
        self.velocidad = velocidad
        self.actualizar_hitbox()
        self.dx = {
            'l': -velocidad,
            'r': velocidad
        }

    def actualizar_hitbox(self):
        self.hitbox = QRect(self.x, self.y, self.ancho, self.alto)

    def atropella(self, hitbox_froggy):
        self.actualizar_hitbox()
        return self.hitbox.intersects(hitbox_froggy)

    def avanzar(self):
        self.x += self.dx[str(self.sentido)]
        self.actualizar_hitbox()

    def __repr__(self):
        return f'(x:{self.x}, y:{self.y}, {self.sentido}, v: {self.velocidad})'


class Objeto(QObject):

    def __init__(self, hitbox, tipo):
        super().__init__()
        self.hitbox = hitbox
        self.alto = p.OBJETOS_ALTO
        self.ancho = p.OBJETOS_ANCHO
        self.tipo = tipo

    def recoge(self, hitbox_froggy):
        return self.hitbox.intersects(hitbox_froggy)

    def dar_efecto(self, dic):
        if self.tipo == 'vida':
            dic['vidas'] += 1
        elif self.tipo == 'moneda':
            dic['monedas'] += p.CANTIDAD_MONEDAS
        elif self.tipo == 'calavera':
            dic['ponderador_troncos'] += 0.05
        elif self.tipo == 'reloj':
            dic['tiempo'] += round(dic['tiempo'] / dic['duracion_nivel']) * 10
        return dic


class Tronco(QObject):
    def __init__(self, x_inicial, y_inicial, sentido, velocidad):
        super().__init__()
        self.x = x_inicial
        self.y = y_inicial
        self.sentido = sentido
        self.alto = p.TRONCOS_ALTO
        self.ancho = p.TRONCOS_ANCHO
        self.velocidad = velocidad
        self.actualizar_hitbox()
        self.dx = {
            'l': -velocidad,
            'r': velocidad
        }

    def actualizar_hitbox(self):
        self.hitbox = QRect(self.x, self.y, self.ancho, self.alto)

    def avanzar(self):
        self.x += self.dx[str(self.sentido)]
        self.actualizar_hitbox()

    def colisiona(self, hitbox_froggy):
        self.actualizar_hitbox()
        return self.hitbox.intersects(hitbox_froggy)

    def __repr__(self):
        return f'(x:{self.x}, y:{self.y}, {self.sentido}, v: {self.velocidad})'
