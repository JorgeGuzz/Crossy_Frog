import sys
from PyQt5.QtWidgets import QApplication
from backend.logica_post_nivel import LogicaPostNivel
from backend.logica_rankings import LogicaRankings
from frontend.ventana_post_nivel import VentanaPostNivel
from frontend.ventana_rankings import VentanaRankings
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    ventana_inicio = VentanaInicio()
    logica_inicio = LogicaInicio()

    ventana_juego = VentanaJuego()
    logica_juego = LogicaJuego()

    ventana_post_nivel = VentanaPostNivel()
    logica_post_nivel = LogicaPostNivel()

    ventana_rankings = VentanaRankings()
    logica_rankings = LogicaRankings()

    ventana_inicio.senal_enviar_nombre.connect(logica_inicio.comprobar_nombre)
    ventana_inicio.senal_ventana_rankings.connect(
        logica_rankings.iniciar_ventana)

    logica_inicio.senal_arrojar_error.connect(ventana_inicio.pop_up_error)
    logica_inicio.senal_ocultar.connect(ventana_inicio.ocultar)
    logica_inicio.senal_abrir_juego.connect(ventana_juego.mostrar_ventana)

    ventana_juego.senal_iniciar_juego.connect(logica_juego.iniciar_juego)
    ventana_juego.senal_tecla_caminar.connect(logica_juego.moverse)
    ventana_juego.senal_tecla_saltar.connect(logica_juego.saltar)
    ventana_juego.senal_alternar_pausa.connect(logica_juego.alternar_pausa)
    ventana_juego.senal_ventana_inicial.connect(ventana_inicio.mostrar)
    ventana_juego.senal_detener_juego.connect(logica_juego.detener_juego)
    ventana_juego.senal_enviar_datos.connect(logica_juego.recibir_datos)
    ventana_juego.senal_saltar_nivel.connect(logica_juego.meta_alcanzada)
    ventana_juego.senal_vidas_trampa.connect(logica_juego.vidas_trampa)
    ventana_juego.senal_nivel_completado.connect(
        logica_post_nivel.nivel_completado)
    ventana_juego.senal_derrota.connect(logica_post_nivel.nivel_fallado)
    ventana_juego.senal_animacion_froggy.connect(logica_juego.animacion_froggy)

    logica_juego.senal_moverse.connect(ventana_juego.mover_froggy)
    logica_juego.senal_saltar.connect(ventana_juego.saltar)
    logica_juego.senal_choca.connect(ventana_juego.choca)
    logica_juego.senal_perder_vida.connect(ventana_juego.perder_vida)
    logica_juego.senal_meta.connect(ventana_juego.nivel_completado)
    logica_juego.senal_derrota.connect(ventana_juego.derrota)
    logica_juego.senal_actualizar_sprite_froggy.connect(
        ventana_juego.actualizar_sprite)
    logica_juego.senal_spawnear_autos.connect(ventana_juego.spawnear_autos)
    logica_juego.senal_borrar_autos.connect(ventana_juego.borrar_autos)
    logica_juego.senal_actualizar_autos.connect(ventana_juego.actualizar_autos)
    logica_juego.senal_spawnear_objeto.connect(ventana_juego.spawnear_objeto)
    logica_juego.senal_borrar_objeto.connect(ventana_juego.borrar_objeto)
    logica_juego.senal_spawnear_troncos.connect(ventana_juego.spawnear_troncos)
    logica_juego.senal_borrar_troncos.connect(ventana_juego.borrar_troncos)
    logica_juego.senal_actualizar_troncos.connect(
        ventana_juego.actualizar_troncos)
    logica_juego.senal_trasladar_froggy_x.connect(
        ventana_juego.trasladar_froggy_x)
    logica_juego.senal_actualizar_sprite_froggy_direccion.connect(
        ventana_juego.actualizar_sprite_froggy_direccion)
    logica_juego.senal_actualizar.connect(ventana_juego.actualizar)

    logica_post_nivel.senal_enviar_datos.connect(
        ventana_post_nivel.actualizar_labels)
    logica_post_nivel.senal_nivel_completado.connect(
        ventana_post_nivel.nivel_completado)
    logica_post_nivel.senal_nivel_fallado.connect(
        ventana_post_nivel.nivel_fallado)

    ventana_post_nivel.senal_ventana_inicial.connect(ventana_inicio.mostrar)
    ventana_post_nivel.senal_ventana_juego.connect(
        ventana_juego.mostrar_ventana)

    ventana_rankings.senal_ventana_inicial.connect(ventana_inicio.mostrar)

    logica_rankings.senal_abrir.connect(ventana_rankings.mostrar)
    logica_rankings.senal_enviar_ranking.connect(
        ventana_rankings.actualizar_ranking)

    ventana_inicio.mostrar()
    app.exec()
