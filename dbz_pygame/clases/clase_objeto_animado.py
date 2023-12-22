# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
# pylint: disable=no-name-in-module
'''clase objeto animado'''

import pygame
from herramientas.imagenes import reescalar_imagenes
from clases.clase_objeto import Objeto

class ObjetoAnimado(Objeto):
    '''clase objeto animado'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, animaciones:list, velocidad:int, potencia_salto:int) -> None:
        super().__init__(tamaño, posicion_inicial, "")
        self.contador_pasos = 0
        self.actualizar_tiempo = pygame.time.get_ticks()
        self.animaciones = animaciones
        self.__animacion_actual = animaciones["quieto_derecha"][0]
        self.__accion = "quieto"
        self.__ultima_accion = "derecha" #donde esta mirando
        self.velocidad = velocidad
        self.__salta = False
        self.__superficie_apoyo = None
        self.__desplazamiento_y = 0
        self.gravedad = 1
        self.potencia_salto = potencia_salto
        self.limite_velocidad_caida = potencia_salto * -1
        reescalar_imagenes(self.animaciones, tamaño)

    def get_animacion_actual(self):
        '''getter animacion actual'''
        return self.__animacion_actual

    def get_accion(self):
        '''getter accion'''
        return self.__accion

    def get_ultima_accion(self):
        '''getter ultima_accion'''
        return self.__ultima_accion

    def get_salta(self):
        '''getter salta'''
        return self.__salta

    def get_superficie_apoyo(self):
        '''getter superficie de apoyo'''
        return self.__superficie_apoyo

    def get_desplazamiento_y(self):
        '''getter desplazamiento_y'''
        return self.__desplazamiento_y

    def set_animacion_actual(self, animacion_actual:str):
        '''setter animacion actual'''
        if type(animacion_actual) == str:
            self.__animacion_actual = animacion_actual
        else:
            raise TypeError("La animacion actual debe ser un path 'str'")

    def set_accion(self, accion:str):
        '''setter accion'''
        if type(accion) == str:
            self.__accion = accion
        else:
            raise TypeError("La acción debe ser un 'str'")

    def set_ultima_accion(self, ultima_accion:str):
        '''setter ultima accion'''
        if type(ultima_accion) == str:
            self.__ultima_accion = ultima_accion
        else:
            raise TypeError("La última acción debe ser un s'tr")

    def set_salta(self, salta:bool):
        '''setter salta'''
        if type(salta) == bool:
            self.__salta = salta
        else:
            raise TypeError("La acción debe ser un 'bool'")

    def set_superficie_apoyo(self, superficie_apoyo):
        '''setter superficie de apoyo'''
        self.__superficie_apoyo = superficie_apoyo

    def set_desplazamiento_y(self, desplazamiento_y:int):
        '''setter desplazamiento_y'''
        if type(desplazamiento_y) == int:
            self.__desplazamiento_y = desplazamiento_y
        else:
            raise TypeError("El desplazamiento en el eje y debe ser un 'int'")

    def animar(self, pantalla:pygame.Surface, accion:str):
        '''anima el objeto animado en la pantalla'''
        super().animar(pantalla)
        tiempo = 110 #milisegundos
        imagen_accion = self.animaciones[accion]
        largo = len(imagen_accion)

        if pygame.time.get_ticks() - self.actualizar_tiempo > tiempo:
            self.contador_pasos += 1
            self.actualizar_tiempo = pygame.time.get_ticks()

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(imagen_accion[self.contador_pasos], self.lados['main'])
        # self.contador_pasos += 1

    def mover(self, eje:str):
        '''mueve el objeto animado dependiendo el eje'''
        for lado in self.lados:
            if eje == "x":
                if self.__accion == "izquierda":
                    self.lados[lado].x += self.velocidad * -1
                else:
                    self.lados[lado].x += self.velocidad
            else:
                self.lados[lado].y += self.__desplazamiento_y
