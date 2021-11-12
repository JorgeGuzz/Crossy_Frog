from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POST_NIVEL)


class VentanaPostNivel(window_name, base_class):

    senal_ventana_inicial = pyqtSignal()
    senal_ventana_juego = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_siguiente_nivel.clicked.connect(self.siguiente_nivel)
        self.boton_salir.clicked.connect(self.salir)

    def salir(self):
        self.senal_ventana_inicial.emit()
        self.close()

    def siguiente_nivel(self):
        self.dic['nivel'] += 1
        self.dic['puntaje_nivel'] = 0
        self.dic['duracion_nivel'] = round(self.dic['duracion_nivel'] *
                                           p.PONDERADOR_DIFICULTAD)
        self.dic['tiempo'] = self.dic['duracion_nivel']
        self.dic['ponderacion_troncos'] = 1
        self.senal_ventana_juego.emit(self.dic)
        self.close()

    def nivel_completado(self):
        self.mostrar_ventana()
        self.boton_siguiente_nivel.setEnabled(True)
        self.notificacion_estado.setStyleSheet("background-color: lightgreen")
        self.notificacion_estado.setText('Nivel Completado! :D')

    def nivel_fallado(self):
        self.mostrar_ventana()
        self.boton_siguiente_nivel.setEnabled(False)
        self.notificacion_estado.setStyleSheet("background-color: red")
        self.notificacion_estado.setText('Derrota :c')

    def actualizar_labels(self, dic):
        self.dic = dic
        self.puntaje_total = str(dic['puntaje_total'])
        self.puntaje_nivel = str(dic['puntaje_nivel'])
        self.vidas = str(dic['vidas'])
        self.tiempo = str(dic['tiempo'])
        self.monedas = str(dic['monedas'])
        self.nivel = str(dic['nivel'])

        self.cont_nivel.setText(self.nivel)
        self.cont_puntaje_total.setText(self.puntaje_total)
        self.cont_puntaje_nivel.setText(self.puntaje_nivel)
        self.cont_vidas.setText(self.vidas)
        self.cont_monedas.setText(self.monedas)
        self.cont_tiempo.setText(self.tiempo)

    def mostrar_ventana(self):
        self.show()
