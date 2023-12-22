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

fondo = pygame.image.load("dbz_pygame/recursos/nivel_uno/fondo_uno.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

piso = Objeto((WIDTH,50), (0,HEIGHT-50), "dbz_pygame/recursos/nivel_uno/piso.png")

# las dos de abajo
plataforma_uno = Objeto((400,30), (100,600), "dbz_pygame/recursos/nivel_uno/plataforma.png")
plataforma_dos = Objeto((400,30), (900,600), "dbz_pygame/recursos/nivel_uno/plataforma.png")

# las dos del medio
plataforma_tres = Objeto((250,30), (350,450), "dbz_pygame/recursos/nivel_uno/plataforma.png")
plataforma_cuatro = Objeto((250,30), (800,450), "dbz_pygame/recursos/nivel_uno/plataforma.png")

# las dos de arriba
plataforma_cinco = Objeto((200,30), (100,300), "dbz_pygame/recursos/nivel_uno/plataforma.png")
plataforma_seis = Objeto((200,30), (900,300), "dbz_pygame/recursos/nivel_uno/plataforma.png")

# plataforma uno
trampa_uno = Item((55,50), (plataforma_uno.lados['main'].x, plataforma_uno.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")
trampa_dos = Item((55,50), (plataforma_uno.lados['main'].x+plataforma_uno.lados['main'].width-55, plataforma_uno.lados['top'].y-50), -0, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma dos
trampa_tres = Item((55,50), (plataforma_dos.lados['main'].x, plataforma_dos.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")
trampa_cuatro = Item((55,50), (plataforma_dos.lados['main'].x+plataforma_dos.lados['main'].width-55, plataforma_dos.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma tres
trampa_cinco = Item((55,50), (plataforma_tres.lados['main'].x+plataforma_tres.lados['main'].width-55, plataforma_tres.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cuatro
trampa_seis = Item((55,50), (plataforma_cuatro.lados['main'].x, plataforma_cuatro.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cinco
trampa_siete = Item((55,50), (plataforma_cinco.lados['main'].x, plataforma_cinco.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma seis
trampa_ocho = Item((55,50), (plataforma_seis.lados['main'].x+plataforma_seis.lados['main'].width-55, plataforma_seis.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

plataformas = [piso, plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro, plataforma_cinco, plataforma_seis]
enemigos = []
items = []
trampas = [trampa_uno, trampa_dos, trampa_tres, trampa_cuatro, trampa_cinco, trampa_seis, trampa_siete, trampa_ocho]

img_enemigo = "dbz_pygame/recursos/cell/cabeza_cell.png"

nivel_uno = Nivel(fondo, plataformas, enemigos, items, trampas, 120, 7, 2, 1, 5, "CELL", img_enemigo)
