# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
# pylint: disable=invalid-name
# pylint: disable=non-ascii-module-import
# pylint: disable=no-member
'''main'''
import sys
import pygame
from clases.clase_juego import Juego
from herramientas.imagenes import dibujar_rectangulos
from herramientas.datos_juego import WIDTH, HEIGHT, TAMAÑO_PANTALLA, FPS, goku
from herramientas.modo import get_modo
from UI.GUI_pantalla_final import FormFinal
from UI.GUI_form_inicio import FormInicio

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

FUENTE = pygame.font.SysFont("Avenir Next", 30)

# timer para el juego
TIEMPO_EVENTO = pygame.USEREVENT + 0
pygame.time.set_timer(TIEMPO_EVENTO, 1000)

juego = None
form_inicio = FormInicio(PANTALLA, 50, 25, WIDTH-100, HEIGHT-50, "dbz_pygame/recursos/ui/wallpaper.png")
form_final = None

def dibujar_borde_rectangulos_juego(pantalla, juego_param):
    '''dibuja los rectangulos de los objetos del juego'''
    if get_modo():
        for plataforma in juego_param.niveles[juego_param.nivel_actual].plataformas:
            dibujar_rectangulos(pantalla, plataforma.lados, "green")

        for enemigo in juego_param.niveles[juego_param.nivel_actual].enemigos:
            dibujar_rectangulos(pantalla, enemigo.lados, "blue")
            for bola in enemigo.bolas_de_ki:
                dibujar_rectangulos(pantalla, bola.lados, "magenta")

        dibujar_rectangulos(pantalla, juego_param.jugador.lados, "red")

        for item in juego_param.niveles[juego_param.nivel_actual].items:
            dibujar_rectangulos(pantalla, item.lados, "yellow")

        for trampa in juego_param.niveles[juego_param.nivel_actual].trampas:
            dibujar_rectangulos(pantalla, trampa.lados, "cyan")

def tiempo_en_segundos(eventos_juego, juego_param):
    '''cuenta el tiempo en segundos del juego'''

    for evento in eventos_juego:
        if evento.type == TIEMPO_EVENTO:
            juego_param.niveles[juego_param.nivel_actual].set_tiempo(-1)
            juego_param.actualizar(PANTALLA, FUENTE, eventos_juego)

while True:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    keys = pygame.key.get_pressed()
    goku.definir_accion(keys)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    if juego is not None and juego.jugando is False:
        form_inicio.flag_jugar = juego.jugando

    if form_inicio.flag_jugar is False:
        form_final = None
        PANTALLA.fill("black")
        form_inicio.update(eventos)
        juego = None
    elif juego is not None and juego.estado_juego is not None:
        PANTALLA.fill("black")
        if form_final is None:
            form_final = FormFinal(PANTALLA, 50, 25, WIDTH-100, HEIGHT-50, "dbz_pygame/recursos/ui/wallpaper.png", juego.estado_juego, juego.jugador.get_puntos())
        form_final.update(eventos)

        if form_final.estado_juego == "again":
            juego = None
            form_inicio.flag_jugar = False
            form_inicio = FormInicio(PANTALLA, 50, 25, WIDTH-100, HEIGHT-50, "dbz_pygame/recursos/ui/wallpaper.png")
    else:
        if juego is None:
            juego = Juego(PANTALLA, goku, form_inicio.nivel, "dbz_pygame/jugadores.bdd", form_inicio.usuario_jugador)

            if form_inicio.nivel == 0:
                goku.set_puntos(0)

            juego.reiniciar_juego()
            juego.mostrar_form_nivel()

        juego.manejar_eventos_juego(eventos)
        tiempo_en_segundos(eventos, juego)
        juego.actualizar(PANTALLA, FUENTE, eventos)
        dibujar_borde_rectangulos_juego(PANTALLA, juego)

    pygame.display.flip()
