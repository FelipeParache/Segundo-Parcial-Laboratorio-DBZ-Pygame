# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
# pylint: disable=no-name-in-module
'''modulo clase proyectil'''
import pygame
from clases.clase_item import Item

class Proyectil(Item):
    '''clase proyectil'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, cambio_vida:int, cambio_ki:int, aporte_puntos:int, velocidad:int, path_sonido="", es_trampa=False, path="") -> None:
        super().__init__(tamaño, posicion_inicial, cambio_vida, cambio_ki, aporte_puntos, path_sonido, es_trampa, path)
        self.velocidad = velocidad

    def verificar_colision_pantalla(self, pantalla:pygame.Surface) -> bool:
        '''verifico si el proyectil sale de pantalla'''
        if self.lados['right'].x >= pantalla.get_width():
            return True
        elif self.lados['left'].x <= 10:
            return True
        return False

    def mover(self):
        '''muevo el proyectil'''
        for lado in self.lados:
            self.lados[lado].x += self.velocidad

    def actualizar(self, pantalla:pygame.Surface):
        '''actualizo en pantalla'''
        self.mover()
        self.verificar_colision_pantalla(pantalla)
        super().actualizar(pantalla)
