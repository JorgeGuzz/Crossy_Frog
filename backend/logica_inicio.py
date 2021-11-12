from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_arrojar_error = pyqtSignal()
    senal_abrir_juego = pyqtSignal(dict)
    senal_ocultar = pyqtSignal()

    def __init__(self):
        super().__init__()

    def comprobar_nombre(self, nombre):
        alfanumerico = nombre.isalnum()
        largo = len(nombre)

        if largo >= p.MIN_CARACTERES and largo <= p.MAX_CARACTERES and alfanumerico:
            datos = {
                'usuario': nombre,
                'vidas': p.VIDAS_INICIO,
                'tiempo': p.DURACION_RONDA_INICIAL,
                'duracion_nivel': p.DURACION_RONDA_INICIAL,
                'monedas': 0,
                'nivel': 1,
                'puntaje_nivel': 0,
                'puntaje_total': 0,
                'velocidad_autos': p.VELOCIDAD_AUTOS,
                'velocidad_troncos': p.VELOCIDAD_TRONCOS,
                'ponderador_troncos': 1
            }
            self.senal_ocultar.emit()
            self.senal_abrir_juego.emit(datos)
        else:
            self.senal_arrojar_error.emit()
