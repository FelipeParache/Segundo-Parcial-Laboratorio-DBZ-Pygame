# pylint: disable=no-member
# pylint: disable=line-too-long
# pylint: disable=invalid-name
# pylint: disable=import-error
# pylint: disable=consider-using-dict-items
# pylint: disable=non-ascii-name
# pylint: disable=no-name-in-module
import random
import pygame
from clases.clase_enemigo import Enemigo

class Boss(Enemigo):
    '''clase boss'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, animaciones:list, velocidad:int, potencia_salto:int, vidas:int, ki:int, daño_ki:int, daño_golpe:int, aporte_puntos:int) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, velocidad, potencia_salto, vidas, ki, daño_ki, daño_golpe, aporte_puntos)
        self.tiempo_cambio_plataforma = 0
        self.intervalo_cambio_plataforma = 100
        self.teletransportar = False

    def cambiar_posicion_random(self, lista_plataformas:list):
        nueva_plataforma = random.choice(lista_plataformas)
        self.set_superficie_apoyo(nueva_plataforma)
        self.lados["main"].bottom = nueva_plataforma.lados["main"].top + 5
        self.teletransportar = True

    def verificar_colision_piso(self, lista_plataformas:list):
        if not self.teletransportar:
            nueva_plataforma = random.choice(lista_plataformas)
            self.set_superficie_apoyo(nueva_plataforma)
            self.lados["main"].bottom = nueva_plataforma.lados["main"].top + 5
            self.teletransportar = True

    def lanzar_ki(self, velocidad:int, cadencia:int):
        '''lanza el ki un poco mas rapido que lo normal'''
        velocidad = velocidad * 1.5
        return super().lanzar_ki(velocidad, cadencia)

    def actualizar(self, pantalla:pygame.Surface, lista_plataformas:list, jugador):
        super().actualizar(pantalla, lista_plataformas, jugador)

        if self.tiempo_cambio_plataforma >= self.intervalo_cambio_plataforma:
            self.cambiar_posicion_random(lista_plataformas)
            self.tiempo_cambio_plataforma = 0
        else:
            self.tiempo_cambio_plataforma += 1
