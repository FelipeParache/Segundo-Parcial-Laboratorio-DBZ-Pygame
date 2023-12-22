# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
'''clase objeto'''
import pygame

from herramientas.imagenes import obtener_rectangulos

class Objeto:
    '''clase objeto'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, path="") -> None:
        self.path = path

        if path != "":
            imagen = pygame.image.load(path)
            imagen = pygame.transform.scale(imagen, tamaño)
        else:
            imagen = pygame.Surface(tamaño)
            imagen.set_alpha(0) # Para que el sprite no tenga un rectangulo negro de fondo

        self.superficie = imagen
        self.posicion_inicial = posicion_inicial
        self.tamaño = tamaño
        self.width = tamaño[0]
        self.height = tamaño[1]

        rectangulo = imagen.get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]

        self.lados = obtener_rectangulos(rectangulo)

    def animar(self, pantalla:pygame.Surface):
        '''anima el objeto en la pantalla'''
        pantalla.blit(self.superficie, self.lados['main'])

    def actualizar(self, pantalla:pygame.Surface):
        '''actualiza el objeto en la pantalla'''
        self.animar(pantalla)
