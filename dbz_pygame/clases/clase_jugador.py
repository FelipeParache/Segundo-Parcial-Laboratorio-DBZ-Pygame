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
'''modulo clase jugador'''
import pygame
from clases.clase_personaje import Personaje

class Jugador(Personaje):
    '''clase jugador'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, animaciones:list, velocidad:int, potencia_salto:int, vidas:int, ki:int, daño_ki:int, daño_golpe:int) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, velocidad, potencia_salto, vidas, ki, daño_ki, daño_golpe)
        self.vidas_iniciales = vidas
        self.__puntos = 0
        self.sonido_colision_item = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/colision_item.wav")
        self.sonido_colision_proyectil = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/proyectil_final.wav")
        self.sonido_colision_golpe = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/golpe.wav")
        self.sonido_colision_trampa = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/colision_trampa.wav")
        self.volumen = 5

    def get_puntos(self):
        '''getter puntos'''
        return self.__puntos

    def set_puntos(self, puntos:int):
        '''setter puntos'''
        if type(puntos) == int:
            self.__puntos += puntos
        else:
            raise TypeError("Los puntos deben ser 'int'")

    def verificar_colision_items(self, items:list):
        '''verifico la colision del jugador con un item'''
        for item in items:
            if self.lados['main'].colliderect(item.lados['main']):
                if item.es_trampa is False:
                    sonido = pygame.mixer.Sound(item.path_sonido)
                    sonido.set_volume(self.volumen)
                    sonido.play()
                    self.set_vida(item.get_cambio_vida())
                    self.set_ki(item.get_cambio_ki())

                items.remove(item)
                del item

    def verificar_colision_trampas(self, trampas:list):
        '''verificar colision con las trampas'''
        for item in trampas:
            if self.lados['right'].colliderect(item.lados['main']) or self.lados['left'].colliderect(item.lados['main']):
                self.set_vida(item.get_cambio_vida())
                self.set_puntos(item.get_aporte_puntos())
                self.sonido_colision_trampa.set_volume(self.volumen)
                self.sonido_colision_trampa.play()
                self.set_atacado(True)
                self.set_accion("atacado")

    def verificar_jugador_atacado_golpe(self, enemigos:list):
        '''verifico la colision con el enemigo'''
        for enemigo in enemigos:
            if enemigo.get_golpeando():
                if enemigo.golpe_rect.colliderect(self.lados['main']):
                    self.sonido_colision_golpe.set_volume(self.volumen)
                    self.sonido_colision_golpe.play()
                    self.set_atacado(True)
                    self.set_accion("atacado")
                    self.set_vida(enemigo.get_daño_golpe())

    def verificar_jugador_atacado_ki(self, enemigos:list):
        '''verifico si el jugador recibe una bola de ki'''
        for enemigo in enemigos:
            for bola_de_ki in enemigo.bolas_de_ki:
                if bola_de_ki.lados['main'].colliderect(self.lados['main']):
                    self.sonido_colision_proyectil.set_volume(self.volumen)
                    self.sonido_colision_proyectil.play()
                    self.set_atacado(True)
                    self.set_accion("atacado")
                    self.set_vida(enemigo.get_daño_ki())
                    enemigo.bolas_de_ki.remove(bola_de_ki)
                    del bola_de_ki

    def verificar_enemigo_atacado_golpe(self, enemigos:list):
        '''verifico la colision con el enemigo'''
        for enemigo in enemigos:
            if self.get_golpeando():
                if self.golpe_rect.colliderect(enemigo.lados['main']):
                    self.sonido_colision_golpe.set_volume(self.volumen)
                    self.sonido_colision_golpe.play()
                    enemigo.set_atacado(True)
                    enemigo.set_accion("atacado")
                    enemigo.set_vida(self.get_daño_golpe())

    def verificar_enemigo_atacado_ki(self, enemigos:list):
        '''verifico si el enemigo recibe una bola de ki'''
        for enemigo in enemigos:
            for bola_de_ki in self.bolas_de_ki:
                if bola_de_ki.lados['main'].colliderect(enemigo.lados['main']):
                    self.sonido_colision_proyectil.set_volume(self.volumen)
                    self.sonido_colision_proyectil.play()
                    enemigo.set_atacado(True)
                    enemigo.set_accion("atacado")
                    enemigo.set_vida(self.get_daño_ki())
                    self.bolas_de_ki.remove(bola_de_ki)
                    del bola_de_ki

    def definir_accion(self, teclas):
        '''defino la acccion del jugador segun los eventos de las teclas'''
        if teclas[pygame.K_RIGHT]:
            self.set_accion("derecha")
        elif teclas[pygame.K_LEFT]:
            self.set_accion("izquierda")
        elif teclas[pygame.K_UP]:
            self.set_accion("salta")
        elif teclas[pygame.K_SPACE]:
            self.set_accion("lanza_ki")
        elif teclas[pygame.K_a]:
            self.set_golpeando(True)
            self.set_accion("golpea")
        else:
            if self.get_accion() != "atacado":
                self.set_golpeando(False)
                self.set_accion("quieto")

    def actualizar(self, pantalla:pygame.Surface, lista_plataformas:list, enemigos:list, items:list, trampas:list):
        '''actualizo en pantalla'''
        super().actualizar(pantalla, lista_plataformas)
        self.verificar_colision_items(items)
        self.verificar_colision_trampas(trampas)
        self.verificar_enemigo_atacado_ki(enemigos)
        self.verificar_enemigo_atacado_golpe(enemigos)
        self.verificar_jugador_atacado_ki(enemigos)
        self.verificar_jugador_atacado_golpe(enemigos)
        self.verificar_colision_trampas(trampas)
