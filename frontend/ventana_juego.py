from PyQt5 import uic
from PyQt5.QtCore import QRect, Qt, pyqtSignal
from PyQt5.QtGui import QKeySequence, QPixmap
from PyQt5.QtWidgets import QLabel, QShortcut
from collections import deque
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_tecla_caminar = pyqtSignal(str)
    senal_tecla_saltar = pyqtSignal()
    senal_alternar_pausa = pyqtSignal(bool)
    senal_ventana_inicial = pyqtSignal()
    senal_animacion_froggy = pyqtSignal(list)
    senal_enviar_datos = pyqtSignal(dict)
    senal_nivel_completado = pyqtSignal(dict)
    senal_derrota = pyqtSignal(dict)
    senal_detener_juego = pyqtSignal()
    senal_saltar_nivel = pyqtSignal()
    senal_vidas_trampa = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()

        self.froggy = QLabel()
        self.objetos = []
        self.carreteras = [deque(), deque(), deque(),
                           deque(), deque(), deque()]
        self.troncos = [deque(), deque(), deque()]

        self.boton_pausa.clicked.connect(self.pausar)
        self.boton_salir.clicked.connect(self.salir)

        self.cheatcode_nivel = QShortcut(
            QKeySequence(Qt.Key_N, Qt.Key_I, Qt.Key_V), self)
        self.cheatcode_nivel.activated.connect(self.saltar_nivel)

        self.cheatcode_vidas = QShortcut(
            QKeySequence(Qt.Key_V, Qt.Key_I, Qt.Key_D), self)
        self.cheatcode_vidas.activated.connect(self.vidas_trampa)

        self.sprites_u = [QPixmap(p.RUTA_FROGGY_UP_1), QPixmap(p.RUTA_FROGGY_UP_1), QPixmap(
            p.RUTA_FROGGY_UP_2), QPixmap(p.RUTA_FROGGY_UP_3), QPixmap(p.RUTA_FROGGY_UP_3)]
        self.sprites_l = [QPixmap(p.RUTA_FROGGY_LEFT_1), QPixmap(p.RUTA_FROGGY_LEFT_1), QPixmap(
            p.RUTA_FROGGY_LEFT_2), QPixmap(p.RUTA_FROGGY_LEFT_3), QPixmap(p.RUTA_FROGGY_LEFT_3)]
        self.sprites_d = [QPixmap(p.RUTA_FROGGY_DOWN_1), QPixmap(p.RUTA_FROGGY_DOWN_1), QPixmap(
            p.RUTA_FROGGY_DOWN_2), QPixmap(p.RUTA_FROGGY_DOWN_3), QPixmap(p.RUTA_FROGGY_DOWN_3)]
        self.sprites_r = [QPixmap(p.RUTA_FROGGY_RIGHT_1), QPixmap(p.RUTA_FROGGY_RIGHT_1), QPixmap(
            p.RUTA_FROGGY_RIGHT_2), QPixmap(p.RUTA_FROGGY_RIGHT_3), QPixmap(p.RUTA_FROGGY_RIGHT_3)]

    def mostrar_ventana(self, dic):
        self.limpiar_mapa()
        self.spawnear_froggy()
        self.show()
        self.dic = dic
        self.cont_vidas.setText(str(self.dic['vidas']))
        self.cont_tiempo.setText(str(self.dic['tiempo']))
        self.cont_monedas.setText(str(self.dic['monedas']))
        self.cont_nivel.setText(str(self.dic['nivel']))
        self.cont_puntaje.setText('0')
        self.setFocus()
        self.senal_enviar_datos.emit(dic)
        self.senal_iniciar_juego.emit()

    def limpiar_mapa(self):
        self.froggy.clear()
        for carretera in self.carreteras:
            for auto in carretera:
                auto.clear()
        self.carreteras = [deque(), deque(), deque(),
                           deque(), deque(), deque()]
        for objeto in self.objetos:
            objeto.clear()
        self.objetos = []
        for hilera in self.troncos:
            for tronco in hilera:
                tronco.clear()
        self.troncos = [deque(), deque(), deque()]

    def keyPressEvent(self, event):
        tecla = event.text()
        if tecla == 'w':
            self.senal_tecla_caminar.emit('U')
        elif tecla == 'a':
            self.senal_tecla_caminar.emit('L')
        elif tecla == 's':
            self.senal_tecla_caminar.emit('D')
        elif tecla == 'd':
            self.senal_tecla_caminar.emit('R')
        elif tecla == ' ':
            self.senal_tecla_saltar.emit()
        elif tecla == 'p':
            pausa = self.boton_pausa.isChecked()
            self.boton_pausa.setChecked(not pausa)
            self.pausar()

    def init_gui(self):
        self.setWindowTitle("Ventana de Juego")

    def spawnear_froggy(self):
        self.froggy = QLabel('', self)
        self.sprite_froggy = QPixmap(p.RUTA_FROGGY_STILL)
        self.froggy.setPixmap(self.sprite_froggy)
        self.froggy.setScaledContents(True)
        self.froggy.resize(p.FROGGY_ANCHO, p.FROGGY_ALTO)
        self.froggy.move(p.SPAWN_X, p.SPAWN_Y)
        self.froggy.show()
        self.froggy_hitbox = self.froggy.geometry()

    def mover_froggy(self, dxdy, direccion):
        dx = dxdy[0]
        dy = dxdy[1]
        x = self.froggy.x() + dx
        y = self.froggy.y() + dy

        self.froggy_hitbox = QRect(x, y, p.FROGGY_ANCHO, p.FROGGY_ALTO)

        if direccion == 'U':
            sprites = self.sprites_u
        elif direccion == 'L':
            sprites = self.sprites_l
        elif direccion == 'D':
            sprites = self.sprites_d
        elif direccion == 'R':
            sprites = self.sprites_r

        self.x, self.y, self.dx, self.dy = x, y, dx, dy
        self.senal_animacion_froggy.emit(sprites)

    def actualizar_sprite(self, sprite):
        self.froggy.setPixmap(sprite)
        self.froggy.move(self.froggy.x() + self.dx/5,
                         self.froggy.y() + self.dy/5)
        self.froggy.raise_()

    def saltar(self, dxdy):
        dx = dxdy[0]
        dy = dxdy[1]
        x = self.froggy.x() + dx
        y = self.froggy.y() + dy
        self.froggy_hitbox = QRect(x, y, p.FROGGY_ANCHO, p.FROGGY_ALTO)
        self.x, self.y, self.dx, self.dy = x, y, dx, dy
        self.froggy.move(x, y)

    def choca(self, direccion):
        if direccion == 'U':
            sprites = self.sprites_u
        elif direccion == 'L':
            sprites = self.sprites_l
        elif direccion == 'D':
            sprites = self.sprites_d
        elif direccion == 'R':
            sprites = self.sprites_r
        self.froggy.setPixmap(sprites[0])
        self.froggy_hitbox = QRect(
            self.froggy.x(), self.froggy.y(), p.FROGGY_ANCHO, p.FROGGY_ALTO)

    def pausar(self):
        if self.boton_pausa.isChecked() == True:
            self.senal_alternar_pausa.emit(True)
        elif self.boton_pausa.isChecked() == False:
            self.senal_alternar_pausa.emit(False)
        self.setFocus()

    def salir(self):
        self.senal_ventana_inicial.emit()
        self.senal_detener_juego.emit()
        self.close()
        self.limpiar_mapa()
        self.init_gui()

    def nivel_completado(self, dic):
        self.froggy.move(self.froggy.x() +
                         p.VELOCIDAD_CAMINAR, self.froggy.y())
        self.froggy.setPixmap(self.sprites_u[0])
        self.close()
        self.limpiar_mapa()
        self.init_gui()
        self.senal_nivel_completado.emit(dic)

    def saltar_nivel(self):
        self.senal_saltar_nivel.emit()

    def vidas_trampa(self):
        self.senal_vidas_trampa.emit()

    def actualizar(self, dic):
        puntaje = dic['puntaje_nivel']
        vidas = dic['vidas']
        tiempo = dic['tiempo']
        monedas = dic['monedas']
        self.cont_puntaje.setText(str(puntaje))
        self.cont_tiempo.setText(str(tiempo))
        self.cont_monedas.setText(str(monedas))
        self.cont_vidas.setText(str(vidas))

    def spawnear_autos(self, auto, indice):
        if auto.sentido == 'l':
            self.sprite_auto = QPixmap(p.RUTA_AUTO_LEFT)
        elif auto.sentido == 'r':
            self.sprite_auto = QPixmap(p.RUTA_AUTO_RIGHT)
        x = auto.x
        y = auto.y
        self.auto = QLabel('', self)
        self.auto.move(x, y)
        self.auto.resize(p.AUTOS_ANCHO, p.AUTOS_ALTO)
        self.auto.setPixmap(self.sprite_auto)
        self.auto.setScaledContents(True)
        self.auto.show()
        self.carreteras[indice].append(self.auto)

    def borrar_autos(self, indice):
        self.carreteras[indice].popleft().clear()

    def actualizar_autos(self, auto, indice_carretera, indice_auto):
        self.carreteras[indice_carretera][indice_auto].move(auto.x, auto.y)

    def spawnear_troncos(self, tronco, indice):
        self.sprite_tronco = QPixmap(p.RUTA_TRONCO)
        x = tronco.x
        y = tronco.y
        self.tronco = QLabel('', self)
        self.tronco.move(x, y)
        self.tronco.resize(p.TRONCOS_ANCHO, p.TRONCOS_ALTO)
        self.tronco.setPixmap(self.sprite_tronco)
        self.tronco.setScaledContents(True)
        self.tronco.show()
        self.troncos[indice].append(self.tronco)

    def borrar_troncos(self, indice):
        self.troncos[indice].popleft().clear()

    def actualizar_troncos(self, tronco, indice_hilera, indice_tronco):
        self.troncos[indice_hilera][indice_tronco].move(tronco.x, tronco.y)

    def spawnear_objeto(self, objeto):
        if objeto.tipo == 'vida':
            self.sprite_objeto = QPixmap(p.RUTA_VIDA)
        elif objeto.tipo == 'moneda':
            self.sprite_objeto = QPixmap(p.RUTA_MONEDA)
        elif objeto.tipo == 'calavera':
            self.sprite_objeto = QPixmap(p.RUTA_CALAVERA)
        elif objeto.tipo == 'reloj':
            self.sprite_objeto = QPixmap(p.RUTA_RELOJ)
        x = objeto.hitbox.x()
        y = objeto.hitbox.y()
        self.objeto = QLabel('', self)
        self.objeto.move(x + (50 - p.OBJETOS_ANCHO)//2,
                         y + (50 - p.OBJETOS_ALTO)//2)
        self.objeto.resize(p.OBJETOS_ANCHO, p.OBJETOS_ALTO)
        self.objeto.setPixmap(self.sprite_objeto)
        self.objeto.setScaledContents(True)
        self.objeto.show()
        self.objetos.append(self.objeto)

    def borrar_objeto(self, indice):
        self.objetos.pop(indice).clear()

    def derrota(self, dic):
        self.close()
        self.limpiar_mapa()
        self.init_gui()

        self.senal_derrota.emit(dic)

    def perder_vida(self):
        self.froggy.clear()
        self.spawnear_froggy()

    def trasladar_froggy_x(self, dx):
        self.froggy.move(self.froggy.x() + dx, self.froggy.y())
        self.froggy.raise_()

    def actualizar_sprite_froggy_direccion(self, direccion):
        if direccion == 'U':
            sprites = self.sprites_u
        elif direccion == 'L':
            sprites = self.sprites_l
        elif direccion == 'D':
            sprites = self.sprites_d
        elif direccion == 'R':
            sprites = self.sprites_r
        self.froggy.setPixmap(sprites[0])
