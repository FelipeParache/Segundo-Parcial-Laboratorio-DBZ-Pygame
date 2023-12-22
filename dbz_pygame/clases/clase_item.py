# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
# pylint: disable=no-name-in-module
'''modulo clase item'''
from clases.clase_objeto import Objeto
import pygame

class Item(Objeto):
    '''clase item'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, cambio_vida:int, cambio_ki:int, aporte_puntos:int, path_sonido="", es_trampa=False, path="") -> None:
        super().__init__(tamaño, posicion_inicial, path)
        self.__cambio_vida = cambio_vida
        self.__cambio_ki = cambio_ki
        self.__aporte_puntos = aporte_puntos
        self.es_trampa = es_trampa

        if path_sonido != "":
            self.path_sonido = pygame.mixer.Sound(path_sonido)

    def get_cambio_vida(self):
        '''getter cambio vida'''
        return self.__cambio_vida

    def get_cambio_ki(self):
        '''getter cambio ki'''
        return self.__cambio_ki

    def get_aporte_puntos(self):
        '''getter cambio ki'''
        return self.__aporte_puntos
