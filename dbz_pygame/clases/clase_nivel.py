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
'''modulo nivel'''
import random
import pygame
from clases.clase_enemigo import Enemigo
from clases.clase_boss import Boss
from clases.clase_item import Item
from clases.clase_objeto import Objeto
from herramientas.imagenes import animaciones_cell, animaciones_freezer, animaciones_ultimate
from herramientas.datos_juego import HEIGHT

class Nivel():
    '''clase nivel'''
    def __init__(self, fondo:str, plataformas:list, enemigos:list, items:list, trampas:list, tiempo:int, enemigos_requeridos:int, max_enemigos:int, nivel_numero:int, temporizador:int, tipo_enemigo:str, img_enemigo:str) -> None:
        self.fondo = fondo
        self.__tiempo = tiempo
        self.enemigos = enemigos
        self.items = items
        self.max_enemigos = max_enemigos
        self.trampas = trampas
        self.plataformas = plataformas
        self.nivel_numero = nivel_numero
        self.enemigos_requeridos = enemigos_requeridos
        self.enemigos_muertos = 0
        self.temporizador = temporizador
        self.tipo_enemigo = tipo_enemigo
        self.img_enemigo = img_enemigo
        self.cantidad_items_generados = 0
        self.cantidad_maxima_items = 7

    def get_tiempo(self):
        '''getter tiempo'''
        return self.__tiempo

    def set_tiempo(self, tiempo:int):
        '''setter tiempo'''
        if type(tiempo) == int:
            self.__tiempo += tiempo
        else:
            raise TypeError("El tiempo actual debe ser tipo 'int'")

    def enemigo_segun_nivel(self) -> Enemigo:
        '''enemigo segun nivel'''
        lista_pos_x = [random.randint(0, 1200) for _ in range(5)]

        if self.nivel_numero == 1:
            for rand in lista_pos_x:
                return Enemigo(tamaño = (110,100),
                               posicion_inicial= (rand,0),
                               animaciones= animaciones_cell,
                               velocidad= 3,
                               potencia_salto= -15,
                               vidas= 500,
                               ki= 1000,
                               daño_ki= -300,
                               daño_golpe= -10,
                               aporte_puntos= 200)

        elif self.nivel_numero == 2:
            for rand in lista_pos_x:
                return Enemigo(tamaño = (120,110),
                               posicion_inicial= (rand,0),
                               animaciones= animaciones_freezer,
                               velocidad= 5,
                               potencia_salto= -15,
                               vidas= 1000,
                               ki= 1000,
                               daño_ki= -500,
                               daño_golpe= -50,
                               aporte_puntos= 500)

        return Boss(tamaño = (120,150),
                    posicion_inicial= (700,HEIGHT-300),
                    animaciones= animaciones_ultimate,
                    velocidad= 5,
                    potencia_salto= -15,
                    vidas= 5000,
                    ki= 1000,
                    daño_ki= -1000,
                    daño_golpe= -100,
                    aporte_puntos= 2000)

    def generar_enemigos(self):
        '''genera los enemigos'''
        enemigo = self.enemigo_segun_nivel()
        if self.__tiempo % self.temporizador == 0:
            if len(self.enemigos) < self.max_enemigos:
                self.enemigos.append(enemigo)

    def generar_esferas(self, lista_plataformas:list):
        if self.cantidad_items_generados < self.cantidad_maxima_items:
            tipo_esfera = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete"]
            for numero in tipo_esfera:
                plataforma_seleccionada = random.choice(lista_plataformas)
                x_plataforma = plataforma_seleccionada.lados['top'].x
                y_plataforma = plataforma_seleccionada.lados['top'].y
                posicion_x = random.randint(x_plataforma, x_plataforma + plataforma_seleccionada.lados['main'].width - 30)
                posicion_y = random.randint(y_plataforma - 50, y_plataforma - 50)

                esfera = Item(tamaño= (30,30),
                                  posicion_inicial= (posicion_x, posicion_y),
                                  cambio_vida= 0,
                                  cambio_ki= 0,
                                  aporte_puntos= 500,
                                  path_sonido= "dbz_pygame/recursos/efectos_de_sonido/colision_esfera.wav",
                                  path= f"dbz_pygame/recursos/esferas/{numero}.png")
                self.items.append(esfera)
                self.cantidad_items_generados += 1

    def generar_items(self, lista_plataformas:list):
        '''genera los items'''
        plataforma_seleccionada = random.choice(lista_plataformas)
        x_plataforma = plataforma_seleccionada.lados['top'].x
        y_plataforma = plataforma_seleccionada.lados['top'].y
        posicion_x = random.randint(x_plataforma, x_plataforma + plataforma_seleccionada.lados['main'].width - 30)
        posicion_y = random.randint(y_plataforma - 50, y_plataforma - 50)

        if self.nivel_numero != 3:
            tipo = random.choice(["semilla", "capsula_ki"]) # Elije aleatoriamente el tipo de item
            if self.__tiempo % 5 == 0 and self.cantidad_items_generados < self.cantidad_maxima_items:
                if tipo == "semilla":
                    semilla = Item(tamaño= (30,30),
                                   posicion_inicial= (posicion_x,posicion_y),
                                   cambio_vida= 1000,
                                   cambio_ki= 0,
                                   aporte_puntos= 0,
                                   path_sonido= "dbz_pygame/recursos/efectos_de_sonido/colision_item.wav",
                                   path= "dbz_pygame/recursos/power_ups/semilla_vida.png")
                    self.items.append(semilla)
                else:
                    capsula_ki = Item(tamaño= (30,30),
                                      posicion_inicial= (posicion_x,posicion_y),
                                      cambio_vida= 0,
                                      cambio_ki= 5,
                                      aporte_puntos= 0,
                                      path_sonido= "dbz_pygame/recursos/efectos_de_sonido/colision_item.wav",
                                      path= "dbz_pygame/recursos/power_ups/capsula_ki.png")
                    self.items.append(capsula_ki)
                self.cantidad_items_generados += 1
        else:
            self.generar_esferas(lista_plataformas)

    def actualizar_plataformas(self, pantalla:pygame.Surface):
        '''actualiza las plataformas en pantalla'''
        for plataforma in self.plataformas:
            if type(plataforma) == Objeto:
                plataforma.actualizar(pantalla)

    def actualizar_enemigos(self, pantalla, jugador):
        '''actualiza los enemigos en pantalla'''
        lista_jugador = [jugador]

        for enemigo in self.enemigos:
            enemigo.actualizar(pantalla, self.plataformas, lista_jugador)

            if self.nivel_numero != 3:
                if enemigo.get_vidas() <= 0:
                    jugador.set_puntos(enemigo.get_aporte_puntos())
                    self.enemigos.remove(enemigo)
                    self.enemigos_muertos += 1
            else:
                if enemigo.get_vidas() < 999:
                    jugador.set_puntos(enemigo.get_aporte_puntos())
                    self.enemigos.remove(enemigo)
                    self.enemigos_muertos += 1

    def actualizar_items(self, pantalla:pygame.Surface):
        '''actualiza los items en pantalla'''
        for item in self.items:
            if type(item) == Item:
                item.actualizar(pantalla)

    def actualizar_trampas(self, pantalla:pygame.Surface):
        '''actualiza las trampas en pantalla'''
        for trampa in self.trampas:
            if type(trampa) == Item:
                trampa.actualizar(pantalla)

    def resetear_enemigos_nivel(self):
        '''resetea los enemigos al terminar el nivel'''
        self.enemigos.clear()
        enemigos = []
        for enemigo in self.enemigos:
            enemigos.append(enemigo)
        self.enemigos = enemigos
        self.enemigos_muertos = 0

    def resetear_items_nivel(self):
        '''resetea los items al terminar el nivel'''
        self.items.clear()
        items = []
        for item in self.items:
            items.append(item)
        self.items = items

    def resetear_nivel(self):
        '''resetea el nivel'''
        self.resetear_enemigos_nivel()
        self.resetear_items_nivel()

    def actualizar(self, pantalla:pygame.Surface, jugador):
        '''actualiza en pantalla el nivel'''
        pantalla.blit(self.fondo, (0,0))
        self.actualizar_plataformas(pantalla)
        jugador.actualizar(pantalla, self.plataformas, self.enemigos, self.items, self.trampas)
        self.actualizar_enemigos(pantalla, jugador)
        self.actualizar_items(pantalla)
        self.actualizar_trampas(pantalla)
        self.generar_enemigos()
        self.generar_items(self.plataformas)
