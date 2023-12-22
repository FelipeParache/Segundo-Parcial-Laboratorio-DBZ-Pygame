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
'''modulo clase enemigo'''
import random
import pygame
from clases.clase_personaje import Personaje

class Enemigo(Personaje):
    '''clase enemigo'''
    def __init__(self, tamaño: tuple, posicion_inicial: tuple, animaciones: list, velocidad: int, potencia_salto: int, vidas: int, ki: int, daño_ki: int, daño_golpe:int, aporte_puntos:int) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, velocidad, potencia_salto, vidas, ki, daño_ki, daño_golpe)

        self.set_accion("derecha")
        self.__aporte_puntos = aporte_puntos
        self.quieto = False
        self.contador_quieto = 0
        self.vision = pygame.Rect(0,0,200,20)

    def get_aporte_puntos(self):
        '''getter aporte puntos'''
        return self.__aporte_puntos

    def moverse(self):
        '''hago que el enemigo rebote de lado a lado en la plataforma en la que se encuentra'''
        if self.get_vidas() > 0:
            if self.quieto is False and random.randint(1, 100) == 1:
                self.quieto = True
                self.contador_quieto = 20

            if self.quieto is False:
                if self.get_superficie_apoyo() is not None:
                    if self.get_accion() == "derecha" and self.lados['right'].x >= self.get_superficie_apoyo().lados['right'].x:
                        self.set_accion("izquierda")
                    elif self.get_accion() == "izquierda" and self.lados['left'].x <= self.get_superficie_apoyo().lados['left'].x:
                        self.set_accion("derecha")
            else:
                self.contador_quieto -= 1
                self.set_accion("quieto")
                if self.contador_quieto <= 0:
                    self.quieto = False

    def definir_accion_ataque(self, jugador, pantalla):
        '''animo el enemigo para que ataque al jugador'''
        if self.get_accion() == "izquierda":
            self.vision.center = (self.lados['main'].centerx - 200, self.lados['main'].centery)
            # pygame.draw.rect(pantalla, "red", self.vision)
        elif self.get_accion() == "derecha":
            self.vision.center = (self.lados['main'].centerx + 200, self.lados['main'].centery)
            # pygame.draw.rect(pantalla, "red", self.vision)
        else:
            self.set_accion(self.get_ultima_accion())

        for goku in jugador:
            if self.vision.colliderect(goku.lados['main']):
                self.set_accion("lanza_ki")
                self.lanzar_ki(velocidad=8, cadencia=20)

            if self.lados['main'].colliderect(goku.lados['main']):
                self.set_golpeando(True)
                self.set_accion("golpea")
            else:
                self.set_golpeando(False)

    def actualizar(self, pantalla:pygame.Surface, lista_plataformas:list, jugador:"Personaje"):
        '''actualiza el enemigo en pantalla'''
        self.moverse()
        super().actualizar(pantalla, lista_plataformas)
        self.definir_accion_ataque(jugador, pantalla)
