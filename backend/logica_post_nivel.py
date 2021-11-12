from PyQt5.QtCore import QObject, pyqtSignal


class LogicaPostNivel(QObject):

    senal_enviar_datos = pyqtSignal(dict)
    senal_nivel_completado = pyqtSignal()
    senal_nivel_fallado = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.completado = True

    def nivel_completado(self, dic):
        self.completado = True
        self.recibir_datos(dic)

        self.senal_nivel_completado.emit()

    def nivel_fallado(self, dic):
        self.completado = False
        self.recibir_datos(dic)
        nombre = dic['usuario']
        puntaje = dic['puntaje_total']

        with open("puntajes.txt", 'a+', encoding="utf-8") as archivo:
            archivo.write(f'{nombre},{puntaje}\n')

        self.senal_nivel_fallado.emit()

    def recibir_datos(self, dic):
        self.dic = dic
        self.puntaje_total = dic['puntaje_total']
        self.puntaje_nivel = dic['puntaje_nivel']
        self.vidas = dic['vidas']
        self.tiempo = dic['tiempo']
        self.monedas = dic['monedas']
        self.nivel = dic['nivel']

        self.senal_enviar_datos.emit(dic)
