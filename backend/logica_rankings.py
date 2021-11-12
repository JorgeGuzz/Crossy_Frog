from PyQt5.QtCore import QObject, pyqtSignal


class LogicaRankings(QObject):

    senal_enviar_ranking = pyqtSignal(list)
    senal_abrir = pyqtSignal()

    def __init__(self):
        super().__init__()

    def iniciar_ventana(self):
        ranking = []
        with open("puntajes.txt", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip().split(",")
                linea[1] = int(linea[1])
                ranking.append(linea)
        ranking.sort(key=lambda x: x[1], reverse=True)

        ranking = ranking[:5]

        self.senal_enviar_ranking.emit(ranking)
        self.senal_abrir.emit()
