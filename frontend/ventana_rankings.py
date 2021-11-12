from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKINGS)


class VentanaRankings(window_name, base_class):

    senal_ventana_inicial = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boton_volver.clicked.connect(self.salir)

    def actualizar_ranking(self, ranking):
        try:
            self.jugador_1.setText(f'1. {ranking[0][0]}')
            self.puntaje_1.setText(f'{ranking[0][1]} ptos.')

            self.jugador_2.setText(f'2. {ranking[1][0]}')
            self.puntaje_2.setText(f'{ranking[1][1]} ptos.')

            self.jugador_3.setText(f'3. {ranking[2][0]}')
            self.puntaje_3.setText(f'{ranking[2][1]} ptos.')

            self.jugador_4.setText(f'4. {ranking[3][0]}')
            self.puntaje_4.setText(f'{ranking[3][1]} ptos.')

            self.jugador_5.setText(f'5. {ranking[4][0]}')
            self.puntaje_5.setText(f'{ranking[4][1]} ptos.')
        except IndexError:
            pass

    def mostrar(self):
        self.show()

    def salir(self):
        self.senal_ventana_inicial.emit()
        self.close()

    def closeEvent(self, event):
        self.senal_ventana_inicial.emit()
        event.accept()
