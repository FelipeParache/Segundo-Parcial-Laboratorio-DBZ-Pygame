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
# pylint: disable=non-ascii-module-import
# pylint: disable=invalid-name
'''nivel uno'''
import pygame
from clases.clase_objeto import Objeto
from clases.clase_nivel import Nivel
from clases.clase_item import Item
from herramientas.datos_juego import TAMAÑO_PANTALLA, WIDTH, HEIGHT

fondo = pygame.image.load("dbz_pygame/recursos/nivel_tres/fondo_tres.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

piso = Objeto((WIDTH,50), (0,HEIGHT-50), "dbz_pygame/recursos/nivel_tres/piso.png")

# las cuatro de abajo
plataforma_uno = Objeto((200,30), (0,600), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_dos = Objeto((200,30), (400,600), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_tres = Objeto((200,30), (800,600), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_cuatro = Objeto((200,30), (1200,600), "dbz_pygame/recursos/nivel_tres/plataforma.png")

# las tres del medio
plataforma_cinco = Objeto((250,30), (200,450), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_seis = Objeto((250,30), (600,450), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_siete = Objeto((200,30), (1000,450), "dbz_pygame/recursos/nivel_tres/plataforma.png")

# las cuatro de arriba
plataforma_ocho = Objeto((200,30), (0,300), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_nueve = Objeto((200,30), (400,300), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_diez = Objeto((200,30), (800,300), "dbz_pygame/recursos/nivel_tres/plataforma.png")
plataforma_once = Objeto((200,30), (1200,300), "dbz_pygame/recursos/nivel_tres/plataforma.png")

# plataforma uno
trampa_uno = Item((55,50), (plataforma_uno.lados['main'].x+50, plataforma_uno.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma dos
trampa_dos = Item((55,50), (plataforma_dos.lados['main'].x+50, plataforma_dos.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma tres
trampa_tres = Item((55,50), (plataforma_tres.lados['main'].x+50, plataforma_tres.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cuatro
trampa_cuatro = Item((55,50), (plataforma_cuatro.lados['main'].x+50, plataforma_cuatro.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cinco
trampa_cinco = Item((55,50), (plataforma_cinco.lados['main'].x+50, plataforma_cinco.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma seis
trampa_seis = Item((55,50), (plataforma_seis.lados['main'].x+50, plataforma_seis.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma siete
trampa_siete = Item((55,50), (plataforma_siete.lados['main'].x+50, plataforma_siete.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma ocho
trampa_ocho = Item((55,50), (plataforma_ocho.lados['main'].x+50, plataforma_ocho.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma nueve
trampa_nueve = Item((55,50), (plataforma_nueve.lados['main'].x+50, plataforma_nueve.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma diez
trampa_diez = Item((55,50), (plataforma_diez.lados['main'].x+50, plataforma_diez.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma once
trampa_once = Item((55,50), (plataforma_once.lados['main'].x+50, plataforma_once.lados['top'].y-48), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

enemigos = []
plataformas = [piso, plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro, plataforma_cinco, plataforma_seis, plataforma_siete, plataforma_ocho, plataforma_nueve, plataforma_diez, plataforma_once]
items = []
trampas = [trampa_uno, trampa_dos, trampa_tres, trampa_cuatro, trampa_cinco, trampa_seis, trampa_siete, trampa_ocho, trampa_nueve, trampa_diez, trampa_once]

img_enemigo = "dbz_pygame/recursos/ultimate_cell/cabeza_ultimate_cell.png"

nivel_tres = Nivel(fondo, plataformas, enemigos, items, trampas, 120, 1, 1, 3, 5, "ULTIMATE CELL", img_enemigo)
