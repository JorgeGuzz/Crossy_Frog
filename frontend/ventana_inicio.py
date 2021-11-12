from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_INICIO)


class VentanaInicio(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_enviar_nombre = pyqtSignal(str)

    senal_ventana_rankings = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.boton_partida_nueva.clicked.connect(self.enviar_login)
        self.boton_rankings.clicked.connect(self.ver_rankings)

    def enviar_login(self):
        nombre = self.form_nombre.text()
        self.senal_enviar_nombre.emit(nombre)

    def pop_up_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText("Nombre de Usuario invalido")
        msg.setWindowTitle("Error 115")
        msg.exec()

    def ver_rankings(self):
        try:
            with open('puntajes.txt'):
                pass
        except FileNotFoundError:
            return self.pop_up_no_rankings()
        self.senal_ventana_rankings.emit()
        self.ocultar()

    def pop_up_no_rankings(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText("No hay rankings registrados todavía")
        msg.setWindowTitle("Error 404")
        msg.exec()

    def mostrar(self):
        self.form_nombre.setText('Ingresa tu nombre de usuario!')
        self.show()

    def ocultar(self):
        self.hide()
