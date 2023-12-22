# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
# pylint: disable=no-member
# pylint: disable=modified-iterating-list
# pylint: disable=no-name-in-module
'''modulo donde se encuentran los datos principales del juego'''
from clases.clase_jugador import Jugador
from herramientas.imagenes import animaciones_goku

WIDTH = 1400
HEIGHT = 800

FPS = 18

TAMAÑO_PANTALLA = (WIDTH,HEIGHT)

NARANJA = (255, 128, 0)
TRANSPARENTE = (0,0,0,0)

goku = Jugador(tamaño=(100,120), posicion_inicial=(200,HEIGHT-300), animaciones=animaciones_goku, velocidad=7, potencia_salto=-16, vidas=3000, ki=10, daño_ki=-500, daño_golpe=-100)
