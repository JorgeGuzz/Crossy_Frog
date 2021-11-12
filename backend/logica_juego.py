import parametros as p
import random
import time
from collections import deque
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, QRect
from PyQt5.QtGui import QPixmap
from backend.entidades import Auto, Froggy, Objeto, Tronco


class LogicaJuego(QObject):

    senal_moverse = pyqtSignal(tuple, str)
    senal_saltar = pyqtSignal(tuple)
    senal_choca = pyqtSignal(str)
    senal_meta = pyqtSignal(dict)
    senal_trasladar_froggy_x = pyqtSignal(int)
    senal_actualizar_sprite_froggy_direccion = pyqtSignal(str)
    senal_derrota = pyqtSignal(dict)
    senal_actualizar = pyqtSignal(dict)
    senal_actualizar_sprite_froggy = pyqtSignal(QPixmap)
    senal_perder_vida = pyqtSignal()
    senal_spawnear_autos = pyqtSignal(Auto, int)
    senal_borrar_autos = pyqtSignal(int)
    senal_actualizar_autos = pyqtSignal(Auto, int, int)
    senal_spawnear_troncos = pyqtSignal(Tronco, int)
    senal_borrar_troncos = pyqtSignal(int)
    senal_actualizar_troncos = pyqtSignal(Tronco, int, int)
    senal_borrar_objeto = pyqtSignal(int)
    senal_spawnear_objeto = pyqtSignal(Objeto)

    def __init__(self):
        super().__init__()
        self.instanciar_timers()
        self.pausa = False
        self.thread = QThread()
        self.objetos = []
        self.carreteras = [[deque(), 'l'], [deque(), 'l'], [deque(), 'l'],
                           [deque(), 'l'], [deque(), 'l'], [deque(), 'l']]
        self.troncos = [deque(), deque(), deque()]
        self.posy_carreteras = p.CARRETERAS_Y
        self.posx_carreteras = p.CARRETERAS_X
        self.orden_troncos = p.TRONCOS_ORDEN
        self.posy_troncos = p.TRONCOS_Y
        self.posx_troncos = p.TRONCOS_X
        self.bordes_mapa = (p.BORDE_INFERIOR, p.BORDE_SUPERIOR,
                            p.BORDE_IZQUIERDO, p.BORDE_DERECHO)
        self.bordes_rio = (p.BORDE_IZQUIERDO_RIO, p.BORDE_DERECHO_RIO)
        self.meta = p.META

    def recibir_datos(self, dic):
        self.dic = dic

    def instanciar_timers(self):
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_tick)
        self.timer_autos = QTimer()
        self.timer_autos.setInterval(p.TIEMPO_AUTOS)
        self.timer_autos.timeout.connect(self.timer_autos_tick)
        self.timer_troncos = QTimer()
        self.timer_troncos.setInterval(p.TIEMPO_TRONCOS)
        self.timer_troncos.timeout.connect(self.timer_troncos_tick)
        self.timer_objetos = QTimer()
        self.timer_objetos.setInterval(p.TIEMPO_OBJETO)
        self.timer_objetos.timeout.connect(self.timer_objetos_tick)

    def timer_tick(self):
        if self.pausa:
            return
        if self.meta.intersects(self.froggy.hitbox):
            self.meta_alcanzada()
            self.froggy.hitbox = QRect(0, 0, 0, 0)
            self.detener_juego()
        self.froggy.tronco_bool = False
        self.dic['tiempo'] -= 1
        self.avanzar_autos()
        self.avanzar_troncos()
        self.verificar_colision_autos()
        self.verificar_colision_objetos()
        self.comprobar_choque_borde_rio(self.froggy.hitbox)
        self.comprobar_caida_rio(self.froggy.hitbox)
        if self.dic['tiempo'] == 0:
            self.derrota()
        self.actualizar()

    def timer_autos_tick(self):
        if self.pausa:
            return
        for i in range(len(self.carreteras)):
            sentido = self.carreteras[i][1]
            y = self.posy_carreteras[str(i)]
            x = self.posx_carreteras[sentido]
            auto = Auto(x, y, sentido, self.dic['velocidad_autos'])
            self.carreteras[i][0].append(auto)
            self.senal_spawnear_autos.emit(auto, i)

    def timer_troncos_tick(self):
        if self.pausa:
            return
        for i in range(len(self.troncos)):
            sentido = self.orden_troncos[self.direccion_troncos_1][i]
            y = self.posy_troncos[str(i)]
            x = self.posx_troncos[sentido]
            tronco = Tronco(x, y, sentido, round(
                self.dic['velocidad_troncos'] * self.dic['ponderador_troncos']))
            self.troncos[i].append(tronco)
            self.senal_spawnear_troncos.emit(tronco, i)

    def timer_objetos_tick(self):
        if self.pausa:
            return
        posibles_x = [x * 50 for x in range(32)]
        x = random.choice(posibles_x)
        posibles_y = [
            y * 50 for y in range(6, 10)] + [y * 50 for y in range(13, 18)]
        y = random.choice(posibles_y)
        tipo = random.choice(['vida', 'moneda', 'calavera', 'reloj'])
        hitbox = QRect(x, y, p.OBJETOS_ANCHO, p.OBJETOS_ALTO)

        for objeto in self.objetos:
            if objeto.hitbox.intersects(hitbox):
                return self.timer_objetos_tick()
        objeto = Objeto(hitbox, tipo)
        self.objetos.append(objeto)
        self.senal_spawnear_objeto.emit(objeto)

    def iniciar_juego(self):
        self.froggy = Froggy()
        self.froggy.direccion = 'D'
        self.sortear_direcciones()
        self.timer.start()
        self.timer_autos.start()
        self.timer_objetos.start()
        self.timer_troncos.start()
        self.timer_autos_tick()
        self.timer_troncos_tick()

    def detener_juego(self):
        self.timer.stop()
        self.timer_autos.stop()
        self.timer_objetos.stop()
        self.timer_troncos.stop()
        self.limpiar_entidades()

    def actualizar(self):
        self.senal_actualizar.emit(self.dic)

    def saltar(self):
        if self.pausa:
            return
        if self.thread.isRunning():
            return
        if self.froggy.direccion in 'LR' and self.froggy.tronco_bool:
            return
        self.froggy.tronco_bool = False
        x = self.froggy.x
        y = self.froggy.y
        dx = 0
        dy = 0
        if self.froggy.direccion == "R":
            dx += self.froggy.distancia_salto
        elif self.froggy.direccion == "L":
            dx -= self.froggy.distancia_salto
        elif self.froggy.direccion == "U":
            dy -= self.froggy.distancia_salto
        elif self.froggy.direccion == "D":
            dy += self.froggy.distancia_salto
        movimiento = (dx, dy)
        hitbox = QRect(x + dx, y + dy, self.froggy.ancho, self.froggy.alto)

        for hilera in self.troncos:
            for tronco in hilera:
                if tronco.hitbox.intersects(hitbox):
                    self.froggy.tronco_bool = True
                    self.froggy.tronco = tronco
        for borde in self.bordes_mapa:
            if hitbox.intersects(borde):
                self.senal_choca.emit(self.froggy.direccion)
                return
        self.froggy.x, self.froggy.y = x + dx, y + dy
        self.froggy.actualizar_hitbox()
        self.senal_saltar.emit(movimiento)
        self.verificar_colision_autos()
        self.verificar_colision_objetos()
        self.comprobar_caida_rio(self.froggy.hitbox)

    def moverse(self, direccion):
        if self.pausa:
            return
        if self.thread.isRunning():
            return
        self.froggy.direccion = direccion
        x = self.froggy.x
        y = self.froggy.y
        dx = 0
        dy = 0
        if self.froggy.direccion == "R":
            dx += self.froggy.velocidad
        elif self.froggy.direccion == "L":
            dx -= self.froggy.velocidad
        elif self.froggy.direccion == "U":
            dy -= self.froggy.velocidad
        elif self.froggy.direccion == "D":
            dy += self.froggy.velocidad
        movimiento = (dx, dy)
        hitbox = QRect(x + dx, y + dy, self.froggy.ancho, self.froggy.alto)
        if self.comprobar_choque_borde_rio(hitbox):
            return
        for borde in self.bordes_mapa:
            if hitbox.intersects(borde):
                self.senal_choca.emit(self.froggy.direccion)
                return
        for hilera in self.troncos:
            for tronco in hilera:
                if tronco.colisiona(hitbox):
                    self.senal_choca.emit(self.froggy.direccion)
                    if not self.froggy.tronco_bool:
                        return
        if self.froggy.tronco_bool:
            if not hitbox.intersects(self.froggy.tronco.hitbox):
                self.senal_actualizar_sprite_froggy_direccion.emit(
                    self.froggy.direccion)
                return
        if self.comprobar_caida_rio(hitbox):
            return
        self.froggy.x, self.froggy.y = x + dx, y + dy
        self.froggy.actualizar_hitbox()

        if self.verificar_colision_autos():
            return
        self.senal_moverse.emit(movimiento, direccion)
        self.verificar_colision_objetos()

    def animacion_froggy(self, sprites):
        if self.thread.isRunning():
            return
        self.thread = ThreadAnimacion(sprites)
        self.thread.start()
        self.thread.senal_actualizar_sprite.connect(self.actualizar_sprite)

    def actualizar_sprite(self, sprite_froggy):
        self.senal_actualizar_sprite_froggy.emit(sprite_froggy)

    def meta_alcanzada(self):
        self.dic['puntaje_nivel'] = (
            (self.dic['vidas'] * 100) + (self.dic['tiempo'] * 50)) * self.dic['nivel']
        self.dic['puntaje_total'] += self.dic['puntaje_nivel']
        self.dic['velocidad_autos'] = round(
            self.dic['velocidad_autos'] * (2 / (1 + p.PONDERADOR_DIFICULTAD)))
        self.dic['velocidad_troncos'] = round(
            self.dic['velocidad_troncos'] * (2 / (1 + p.PONDERADOR_DIFICULTAD)))
        self.dic['ponderador_troncos'] = 1
        self.senal_meta.emit(self.dic)
        self.detener_juego()

    def alternar_pausa(self, pausa):
        self.pausa = pausa

    def avanzar_autos(self):
        indice_carretera = 0
        for carretera in self.carreteras:
            indice_auto = 0
            lista = []
            for auto in carretera[0]:
                auto.avanzar()
                auto.actualizar_hitbox()
                self.senal_actualizar_autos.emit(
                    auto, indice_carretera, indice_auto)
                lista.append(auto.x >= 1600 and auto.sentido == 'r')
                lista.append(auto.x <= -100 and auto.sentido == 'l')
                indice_auto += 1
            if any(lista):
                carretera[0].popleft()
                self.senal_borrar_autos.emit(indice_carretera)
            indice_carretera += 1

    def avanzar_troncos(self):
        indice_hilera = 0
        for hilera in self.troncos:
            indice_tronco = 0
            lista = []
            for tronco in hilera:
                if tronco.hitbox.intersects(self.froggy.hitbox):
                    self.froggy.sobre_tronco(tronco)
                    self.senal_trasladar_froggy_x.emit(
                        tronco.dx[str(tronco.sentido)])
                    self.froggy.tronco_bool = True
                    self.froggy.tronco = tronco
                tronco.avanzar()
                self.senal_actualizar_troncos.emit(
                    tronco, indice_hilera, indice_tronco)
                lista.append(tronco.x >= 1600 and tronco.sentido == 'r')
                lista.append(tronco.x <= -100 and tronco.sentido == 'l')
                indice_tronco += 1
            if any(lista):
                hilera.popleft()
                self.senal_borrar_troncos.emit(indice_hilera)
            indice_hilera += 1

    def sortear_direcciones(self):
        for carretera in self.carreteras:
            carretera[1] = random.choice(['l', 'r'])
        self.direccion_troncos_1 = random.choice(['l', 'r'])

    def limpiar_entidades(self):
        self.carreteras = [[deque(), 'l'], [deque(), 'l'], [deque(), 'l'],
                           [deque(), 'l'], [deque(), 'l'], [deque(), 'l']]
        self.objetos = []
        self.troncos = [deque(), deque(), deque()]

    def verificar_colision_autos(self):
        for carretera in self.carreteras:
            for auto in carretera[0]:
                if auto.atropella(self.froggy.hitbox):
                    self.perder_vida()
                    return True

    def verificar_colision_objetos(self):
        indice = 0
        for objeto in self.objetos:
            if objeto.recoge(self.froggy.hitbox):
                self.dic = objeto.dar_efecto(self.dic)
                self.senal_borrar_objeto.emit(indice)
                self.objetos.pop(indice)
                self.actualizar()
                return self.verificar_colision_objetos()
            indice += 1

    def perder_vida(self):
        self.dic['vidas'] -= 1
        self.froggy.respawnear()
        self.senal_perder_vida.emit()
        self.actualizar()
        if self.dic['vidas'] == 0:
            self.derrota()

    def derrota(self):
        self.dic['puntaje_nivel'] = (
            (self.dic['vidas'] * 100) + (self.dic['tiempo'] * 50)) * self.dic['nivel']
        self.dic['puntaje_total'] += self.dic['puntaje_nivel']
        self.detener_juego()
        self.senal_derrota.emit(self.dic)

    def vidas_trampa(self):
        self.dic['vidas'] += p.VIDAS_TRAMPA
        self.actualizar()

    def comprobar_choque_borde_rio(self, froggy_hitbox):
        for borde_rio in self.bordes_rio:
            if froggy_hitbox.intersects(borde_rio):
                self.perder_vida()
                return True

    def comprobar_caida_rio(self, froggy_hitbox):
        if not self.froggy.tronco_bool:
            for hitbox_rio in p.RIO:
                if froggy_hitbox.intersects(hitbox_rio):
                    self.perder_vida()
                    return True


class ThreadAnimacion(QThread):
    senal_actualizar_sprite = pyqtSignal(QPixmap)

    def __init__(self, sprites):
        super().__init__()
        self.sprites = sprites

    def run(self):
        for i in range(5):
            time.sleep(0.02)
            self.senal_actualizar_sprite.emit(self.sprites[i])
