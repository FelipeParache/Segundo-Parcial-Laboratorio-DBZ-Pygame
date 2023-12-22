# pylint: disable=non-ascii-name
# pylint: disable=consider-using-dict-items
# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=unidiomatic-typecheck
# pylint: disable=import-error
# pylint: disable=arguments-differ
# pylint: disable=no-name-in-module
'''Modulo class Personaje'''
import pygame
from clases.clase_objeto_animado import ObjetoAnimado
from clases.clase_proyectil import Proyectil

class Personaje(ObjetoAnimado):
    '''clase personaje'''
    def __init__(self, tamaño:tuple, posicion_inicial:tuple, animaciones:list, velocidad:int, potencia_salto:int, vidas:int, ki:int, daño_ki:int, daño_golpe:int) -> None:
        super().__init__(tamaño, posicion_inicial, animaciones, velocidad, potencia_salto)
        pygame.mixer.init()
        self.__vidas = vidas
        self.__ki = ki
        self.__atacado = False
        self.__daño_ki = daño_ki
        self.__daño_golpe = daño_golpe
        self.__golpeando = False
        self.golpe_rect = pygame.Rect(0,0,40,20)
        self.bolas_de_ki = []
        self.img_proyectil = "dbz_pygame/recursos/efectos/proyectil.png"
        self.disparo_cooldown = 0

    def get_vidas(self):
        '''getter vidas'''
        return self.__vidas

    def get_ki(self):
        '''getter ki'''
        return self.__ki

    def get_atacado(self):
        '''getter atacado'''
        return self.__atacado

    def get_daño_ki(self):
        '''getter daño ki'''
        return self.__daño_ki

    def get_daño_golpe(self):
        '''getter daño golpe'''
        return self.__daño_golpe

    def get_golpeando(self):
        '''getter golpeando'''
        return self.__golpeando

    def set_vida(self, vidas:int):
        '''setter vidas'''
        if type(vidas) == int:
            self.__vidas += vidas
        else:
            raise TypeError("La vida actual debe ser un 'int'")

    def set_ki(self, ki:int):
        '''setter ki'''
        if type(ki) == int:
            self.__ki += ki
        else:
            raise TypeError("El ki actual debe ser un 'int'")

    def set_atacado(self, atacado:bool):
        '''setter atacado'''
        if type(atacado) == bool:
            self.__atacado = atacado
        else:
            raise TypeError("El atacado debe ser un 'bool'")

    def set_golpeando(self, golpeando:bool):
        '''setter atacado'''
        if type(golpeando) == bool:
            self.__golpeando = golpeando
        else:
            raise TypeError("El atacado debe ser un 'bool'")

    def verificar_salto(self, pantalla:pygame.Surface):
        '''verifico si salta para animarlo'''
        if self.get_salta():
            if self.get_ultima_accion() == "derecha":
                self.animar(pantalla, "salta_derecha")
            else:
                self.animar(pantalla, "salta_izquierda")
            self.mover("y")

        if self.get_desplazamiento_y() + self.gravedad < self.limite_velocidad_caida:
            caida = self.get_desplazamiento_y() + self.gravedad
            self.set_desplazamiento_y(caida)

    def verificar_colision_piso(self, lista_plataformas:list):
        '''verifico si esta apoyado sobre una plataforma'''
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                if self.get_superficie_apoyo() is None:
                    self.set_superficie_apoyo(plataforma)
                self.lados["main"].bottom = plataforma.lados["main"].top + 5
                self.set_salta(False)
                self.set_desplazamiento_y(0)
                break
            self.set_salta(True)

    def lanzar_ki(self, velocidad:int, cadencia:int):
        '''lanza la bola de ki a la velocidad pasada por parametro'''
        if self.__ki <= 0:
            self.__ki = 0

        if self.disparo_cooldown == 0 and self.get_ki() > 0:
            self.disparo_cooldown = cadencia

            if self.get_ultima_accion() == "izquierda":
                velocidad = velocidad * -1
                bola_de_ki = Proyectil((40,40), (self.lados["main"].x - 40, self.lados["main"].y + 20), 0, 0, 0, velocidad, "dbz_pygame/recursos/efectos_de_sonido/pryectil_inicio.wav", False, "dbz_pygame/recursos/proyectil.png")
            elif self.get_ultima_accion() == "derecha":
                bola_de_ki = Proyectil((40,40), (self.lados["main"].x + 110, self.lados["main"].y + 20), 0, 0, 0, velocidad, "dbz_pygame/recursos/efectos_de_sonido/pryectil_inicio.wav", False, "dbz_pygame/recursos/proyectil.png")

            bola_de_ki.path_sonido.set_volume(1)
            bola_de_ki.path_sonido.play()

            self.bolas_de_ki.append(bola_de_ki)
            self.set_ki(-1)

    def golpear(self, pantalla:pygame.Surface):
        '''ataque cuerpo a cuerpo'''
        if self.__golpeando:
            if self.get_ultima_accion() == "izquierda":
                self.golpe_rect.center = (self.lados['main'].centerx - 55, self.lados['main'].centery)
            elif self.get_ultima_accion() == "derecha":
                self.golpe_rect.center = (self.lados['main'].centerx + 55, self.lados['main'].centery)

            # pygame.draw.rect(pantalla, "red", self.golpe_rect)

    def actualizar_bolas_de_ki(self, pantalla:pygame.Surface):
        '''actualizo la lista de bolas de ki cuando son disparadas'''
        for bola_de_ki in self.bolas_de_ki:
            if type(bola_de_ki) == Proyectil: # verifico el tipo para que me reconozca los metodos
                bola_de_ki.actualizar(pantalla)
                if bola_de_ki.verificar_colision_pantalla(pantalla):
                    self.bolas_de_ki.remove(bola_de_ki)

    def actualizar_animacion(self, pantalla:pygame.Surface):
        '''actualiza las animaciones segun la accion'''
        if self.get_accion() == "derecha":
            if not self.get_salta():
                self.animar(pantalla, "camina_derecha")
            if self.lados['main'].x < pantalla.get_width() - self.width:
                self.set_ultima_accion("derecha")
                self.mover("x")

        elif self.get_accion() == "izquierda":
            if not self.get_salta():
                self.animar(pantalla, "camina_izquierda")
            if self.lados['main'].x > 0:
                self.set_ultima_accion("izquierda")
                self.mover("x")

        elif self.get_accion() == "salta":
            if not self.get_salta():
                self.set_salta(True)
                self.set_desplazamiento_y(self.potencia_salto)
                self.mover("y")

        elif self.get_accion() == "quieto":
            if not self.get_salta():
                if self.get_ultima_accion() == "derecha":
                    self.animar(pantalla, "quieto_derecha")
                else:
                    self.animar(pantalla, "quieto_izquierda")

        elif self.get_accion() == "atacado":
            if self.get_atacado() is True:
                if self.get_ultima_accion() == "derecha":
                    self.animar(pantalla, "atacado_derecha")
                else:
                    self.animar(pantalla, "atacado_izquierda")
                self.set_atacado(False)
            else:
                self.set_accion(self.get_ultima_accion())

        elif self.get_accion() == "lanza_ki":
            if not self.get_salta():
                if self.get_accion() != "atacado":
                    self.lanzar_ki(20, 10)
                    if self.get_ultima_accion() == "derecha":
                        self.animar(pantalla, "lanza_ki_derecha")
                    if self.get_ultima_accion() == "izquierda":
                        self.animar(pantalla, "lanza_ki_izquierda")
                    self.disparo_cooldown -= 1

        elif self.get_accion() == "golpea":
            if not self.get_salta():
                if self.get_accion() != "atacado":
                    self.golpear(pantalla)
                    if self.get_ultima_accion() == "derecha":
                        self.animar(pantalla, "golpea_derecha")
                    if self.get_ultima_accion() == "izquierda":
                        self.animar(pantalla, "golpea_izquierda")

    def actualizar(self, pantalla:pygame.Surface, lista_plataformas:list):
        '''actualiza y muestra el personaje en pantalla'''
        self.actualizar_animacion(pantalla)
        self.actualizar_bolas_de_ki(pantalla)
        self.verificar_colision_piso(lista_plataformas)
        self.verificar_salto(pantalla)
