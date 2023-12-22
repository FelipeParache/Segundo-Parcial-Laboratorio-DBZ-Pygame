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
'''nivel dos'''
import pygame
from clases.clase_objeto import Objeto
from clases.clase_nivel import Nivel
from clases.clase_item import Item
from herramientas.datos_juego import TAMAÑO_PANTALLA, WIDTH, HEIGHT

fondo = pygame.image.load("dbz_pygame/recursos/nivel_dos/fondo_dos.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

piso = Objeto((WIDTH,50), (0,HEIGHT-50), "dbz_pygame/recursos/nivel_dos/piso.png")

# las dos de abajo
plataforma_uno = Objeto((200,30), (0,650), "dbz_pygame/recursos/nivel_dos/plataforma.png")
plataforma_dos = Objeto((200,30), (1200,650), "dbz_pygame/recursos/nivel_dos/plataforma.png")
plataforma_tres = Objeto((150,30), (600,650), "dbz_pygame/recursos/nivel_dos/plataforma.png")

# las del medio
plataforma_cuatro = Objeto((250,30), (200,500), "dbz_pygame/recursos/nivel_dos/plataforma.png")
plataforma_cinco = Objeto((250,30), (950,500), "dbz_pygame/recursos/nivel_dos/plataforma.png")

# las dos del medio arriba
plataforma_seis = Objeto((200,30), (100,350), "dbz_pygame/recursos/nivel_dos/plataforma.png")
plataforma_siete = Objeto((200,30), (1100,350), "dbz_pygame/recursos/nivel_dos/plataforma.png")
plataforma_ocho = Objeto((150,30), (600,350), "dbz_pygame/recursos/nivel_dos/plataforma.png")

plataforma_nueve = Objeto((200,30), (300,200), "dbz_pygame/recursos/nivel_dos/plataforma.png")
plataforma_diez = Objeto((200,30), (900,200), "dbz_pygame/recursos/nivel_dos/plataforma.png")

# piso
trampa_uno = Item((55,50), (piso.lados['main'].x+200, piso.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")
trampa_dos = Item((55,50), (piso.lados['main'].x+piso.lados['main'].width-250, piso.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma tres
trampa_tres = Item((55,50), (plataforma_tres.lados['main'].x, plataforma_tres.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cuatro
trampa_cuatro = Item((55,50), (plataforma_cuatro.lados['main'].x+plataforma_cuatro.lados['main'].width-55, plataforma_cuatro.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# pltaforma cinco
trampa_cinco = Item((55,50), (plataforma_cinco.lados['main'].x, plataforma_cinco.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cuatro
trampa_seis = Item((55,50), (plataforma_seis.lados['main'].x+plataforma_seis.lados['main'].width-55, plataforma_seis.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma cinco
trampa_siete = Item((55,50), (plataforma_siete.lados['main'].x, plataforma_siete.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# plataforma seis
trampa_ocho = Item((55,50), (plataforma_ocho.lados['main'].x+plataforma_ocho.lados['main'].width-55, plataforma_ocho.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# platafroma siete
trampa_nueve = Item((55,50), (plataforma_nueve.lados['main'].x+plataforma_nueve.lados['main'].width-55, plataforma_nueve.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

# platafroma ocho
trampa_diez = Item((55,50), (plataforma_diez.lados['main'].x, plataforma_diez.lados['top'].y-50), -10, 0, -10, "dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav", True, "dbz_pygame/recursos/trampa.png")

plataformas = [piso, plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro, plataforma_cinco, plataforma_seis, plataforma_siete, plataforma_ocho, plataforma_nueve, plataforma_diez]
enemigos = []
items = []
trampas = [trampa_uno, trampa_dos, trampa_tres, trampa_cuatro, trampa_cinco, trampa_seis, trampa_siete, trampa_ocho, trampa_nueve, trampa_diez]

img_enemigo = "dbz_pygame/recursos/freezer/cabeza_freezer.png"

nivel_dos = Nivel(fondo, plataformas, enemigos, items, trampas, 120, 10, 3, 2, 5, "FREEZER", img_enemigo)
