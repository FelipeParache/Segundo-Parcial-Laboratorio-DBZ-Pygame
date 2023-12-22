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
'''clase juego'''
import pygame
from UI.GUI_button_image import ButtonImage
from UI.GUI_form_nivel import FormNivel
from UI.GUI_form_pausa import FormPausa
from UI.GUI_form_settings import FormSettings
from UI.GUI_picture_box import PictureBox
from clases.clase_jugador import Jugador
from clases.clase_nivel import Nivel
from herramientas.config_bdd import actualizar_jugador
from herramientas.datos_juego import HEIGHT, WIDTH, TRANSPARENTE, NARANJA
from herramientas.modo import cambiar_modo
from herramientas.datos_nivel_uno import nivel_uno
from herramientas.datos_nivel_dos import nivel_dos
from herramientas.datos_nivel_tres import nivel_tres

class Juego():
    '''clase juego'''
    def __init__(self, pantalla:pygame.Surface, jugador:"Jugador", nivel_actual:"Nivel", base_datos, usuario) -> None:
        pygame.mixer.init()
        self.pantalla = pantalla
        self.usuario = usuario
        self.jugando = True
        self.base_datos = base_datos
        self.jugador = jugador
        self.nivel_actual = nivel_actual
        self.niveles = [nivel_uno, nivel_dos, nivel_tres]
        self.estado_juego = None

        self.sonido_victoria = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/victoria.ogg")
        self.sonido_derrota = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/derrota.ogg")
        self.sonido_paso_nivel = pygame.mixer.Sound("dbz_pygame/recursos/efectos_de_sonido/nivel_completado.ogg")

        if pygame.mixer.music.get_busy():
            pygame.mixer.music.load("dbz_pygame/recursos/efectos_de_sonido/musica_dos.ogg")
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume())
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load("dbz_pygame/recursos/efectos_de_sonido/musica_dos.ogg")

        self.boton_config = ButtonImage(pantalla, 0, 0, WIDTH-60, 115, 50, 50, "dbz_pygame/recursos/ui/btn_config.png", self.btn_config_click, "x")

        self.boton_pausa = ButtonImage(pantalla, 0, 0, WIDTH-60, 175, 50, 50, "dbz_pygame/recursos/ui/btn_pause.png", self.btn_pausar_click, "x")

    def generar_posicionar_enemigos_img(self, pantalla, lista_eventos):
        entero = self.niveles[self.nivel_actual].enemigos_requeridos - self.niveles[self.nivel_actual].enemigos_muertos
        imgs = []
        x = 10

        for _ in range(0, entero):
            img_enemigo = PictureBox(pantalla, x, 55, 30, 30, self.niveles[self.nivel_actual].img_enemigo)

            imgs.append(img_enemigo)
            x += 40

        for img in imgs:
            img.update(lista_eventos)

    def generar_img_vidas_boss(self, pantalla, lista_eventos):
        imgs = []
        x = 10
        for enemigo in self.niveles[self.nivel_actual].enemigos:
            vidas = enemigo.get_vidas() // 1000

            for _ in range(0, vidas):
                img_vida = PictureBox(pantalla, x, 55, 30, 30, "dbz_pygame/recursos/ultimate_cell/cabeza_ultimate_cell.png")
                imgs.append(img_vida)
                x += 40

        for img in imgs:
            img.update(lista_eventos)

    def generar_img_vidas(self, pantalla, lista_eventos):
        vidas = self.jugador.get_vidas() // 1000

        imgs = []
        x = WIDTH-50

        for _ in range(0, vidas):
            img_vida = PictureBox(pantalla, x, 5, 30, 30, "dbz_pygame/recursos/goku_super_saiyajin/cabeza_goku.png")
            imgs.append(img_vida)
            x -= 40

        for img in imgs:
            img.update(lista_eventos)

    def generar_posicionar_textos(self, pantalla, fuente) -> None:
        texto = fuente.render("VIDAS:", False, NARANJA, "Blue")

        texto_vidas = {
            "texto": texto,
            "pos_x": 1000,
            "pos_y": 2
        }

        texto = fuente.render(f"KI: {self.jugador.get_ki()}", False, NARANJA, "Blue")

        texto_ki = {
            "texto": texto,
            "pos_x": 1000,
            "pos_y": 50
        }

        texto = fuente.render(f"PUNTOS: {self.jugador.get_puntos()}", False, NARANJA, "Blue")

        texto_puntos = {
            "texto": texto,
            "pos_x": 10,
            "pos_y": 2
        }

        texto = fuente.render(f"TIEMPO RESTANTE: {self.niveles[self.nivel_actual].get_tiempo()}", False, NARANJA, "Blue")

        ancho_texto = texto.get_width()

        texto_tiempo = {
            "texto": texto,
            "pos_x": pantalla.get_width()/2-(ancho_texto/2),
            "pos_y": 2
        }

        textos = [texto_ki, texto_vidas, texto_puntos, texto_tiempo]

        for texto in textos:
            pantalla.blit(texto['texto'], (texto['pos_x'], texto['pos_y']))

    def btn_pausar_click(self, param):
        form_pausa = FormPausa(self.pantalla,
                               x= WIDTH/2-300,
                               y= 25,
                               w= 600,
                               h= 500,
                               color_background= TRANSPARENTE,
                               color_border= "White",
                               border_size= -1,
                               active= True)
        self.pausar_juego(form_pausa)

    def btn_config_click(self, param):
        form_settings = FormSettings(self.pantalla,
                                     x= WIDTH/2-400,
                                     y= 25,
                                     w= 800,
                                     h= 500,
                                     color_background= TRANSPARENTE,
                                     color_border= "White",
                                     border_size= -1,
                                     active= True)
        self.pausar_juego(form_settings)

    def posicionar_form_general(self, lista_eventos) -> None:
        self.boton_config.update(lista_eventos)
        self.boton_pausa.update(lista_eventos)

    def cerrar_juego(self):
        pygame.quit()

    def mostrar_form_nivel(self) -> None:
        nivel = {
            'tipo_enemigo': self.niveles[self.nivel_actual].tipo_enemigo,
            'numero': self.nivel_actual + 1,
            'img_enemigo': self.niveles[self.nivel_actual].img_enemigo,
            'cantidad': self.niveles[self.nivel_actual].enemigos_requeridos,
        }

        form_nivel = FormNivel(self.pantalla,
                               x= WIDTH/2-((WIDTH-200)/2),
                               y= 50,
                               w= WIDTH-200,
                               h= HEIGHT-100,
                               color_background= TRANSPARENTE,
                               color_border= "White",
                               border_size= -1,
                               active= True,
                               nivel= nivel)

        self.pausar_juego(form_nivel)

    def verificar_puntos_tiempo(self, eventos):
        if self.niveles[self.nivel_actual].enemigos_muertos >= self.niveles[self.nivel_actual].enemigos_requeridos:
            if self.nivel_actual < len(self.niveles) - 1:
                self.sonido_paso_nivel.set_volume(self.jugador.volumen)
                self.sonido_paso_nivel.play()
                self.jugador.set_puntos(self.niveles[self.nivel_actual].get_tiempo() * 100)
                self.jugador.bolas_de_ki.clear()
                self.nivel_actual += 1
                self.mostrar_form_nivel()
            else:
                if self.jugador.get_puntos() > self.usuario['puntos']:
                    actualizar_jugador(self.nivel_actual, self.jugador.get_puntos(), self.usuario['usuario'], self.base_datos)
                    pygame.mixer.stop()
                    self.sonido_victoria.set_volume(self.jugador.volumen)
                    self.sonido_victoria.play()
                    self.estado_juego = "gano"

        if self.niveles[self.nivel_actual].get_tiempo() <= 0 and self.niveles[self.nivel_actual].enemigos_muertos < self.niveles[self.nivel_actual].enemigos_requeridos:
            if self.usuario['nivel_max'] < self.nivel_actual:
                if self.usuario['puntos'] == 0:
                    actualizar_jugador(self.nivel_actual, self.jugador.get_puntos(), self.usuario['usuario'], self.base_datos)
            pygame.mixer.stop()
            self.sonido_derrota.set_volume(self.jugador.volumen)
            self.sonido_derrota.play()
            self.estado_juego = "perdio"
            self.reiniciar_juego()

    def verificar_vida_jugador(self):
        if self.jugador.get_vidas() <= 999:
            if self.usuario['nivel_max'] < self.nivel_actual:
                if self.usuario['puntos'] == 0:
                    actualizar_jugador(self.nivel_actual, self.jugador.get_puntos(), self.usuario['usuario'], self.base_datos)
            pygame.mixer.stop()
            self.sonido_derrota.set_volume(self.jugador.volumen)
            self.sonido_derrota.play()
            self.estado_juego = "murio"

    def pausar_juego(self, formulario):
        while formulario.pausado:
            eventos = pygame.event.get()
            self.pantalla.fill('black')
            formulario.update(eventos)
            if formulario.jugando is False:
                self.jugando = False
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    self.cerrar_juego()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_TAB:
                        cambiar_modo()
            pygame.display.flip()

    def manejar_eventos_juego(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                self.cerrar_juego()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()

    def reiniciar_juego(self):
        for nivel in self.niveles:
            if type(nivel) == Nivel:
                nivel.resetear_nivel()

    def actualizar(self, pantalla, fuente, eventos):
        self.verificar_puntos_tiempo(eventos)
        self.verificar_vida_jugador()
        self.niveles[self.nivel_actual].actualizar(pantalla, self.jugador)
        self.generar_posicionar_textos(pantalla, fuente)
        self.generar_img_vidas(pantalla, eventos)
        self.posicionar_form_general(eventos)
        if self.niveles[self.nivel_actual].nivel_numero != 3:
            self.generar_posicionar_enemigos_img(pantalla, eventos)
        else:
            self.generar_img_vidas_boss(pantalla, eventos)
