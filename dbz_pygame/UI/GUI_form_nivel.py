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
# pylint: disable=unused-argument
import pygame
from UI.GUI_button import Button
from UI.GUI_form import Form
from UI.GUI_form_estado_juego import NARANJA
from UI.GUI_label import Label
from UI.GUI_button_image import ButtonImage
from UI.GUI_picture_box import PictureBox

class FormNivel(Form):
    '''class form nivel'''
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, nivel:dict):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        self.jugando = True
        self.pausado = True

        self.label = Label(screen= self._slave,
                           x= 0,
                           y= 0,
                           w= w,
                           h= 50,
                           text= f"PROXIMO NIVEL: {nivel['numero']}",
                           font= "Avenir Next",
                           font_size= 20,
                           font_color= "White",
                           path_image= "dbz_pygame/recursos/ui/text_box.png")

        self.label_enemigos = Label(screen= self._slave,
                                    x= 100,
                                    y= 70,
                                    w= 500,
                                    h= 50,
                                    text= f"EL ENEMIGO DEL NIVEL ES {nivel['tipo_enemigo']}",
                                    font= "Avenir Next",
                                    font_size= 20,
                                    font_color= "White")

        self.label_cantidad = Label(screen= self._slave,
                                    x= 110,
                                    y= 130,
                                    w= 450,
                                    h= 50,
                                    text= f"CANTIDAD DE ENEMIGOS: {nivel['cantidad']}",
                                    font= "Avenir Next",
                                    font_size= 20,
                                    font_color= "White")

        self.icono_enemigo = PictureBox(self._slave, 0, 70, 100, 100, nivel['img_enemigo'])

        self.label_descripcion_uno = Label(screen=self._slave,
                                           x= 0,
                                           y= 170,
                                           w= w,
                                           h= 150,
                                           text= "TENDRAS 60 SEGUNDOS PARA ALCANZAR EL OBJETIVO",
                                           font= "Avenir Next",
                                           font_size= 20,
                                           font_color= "White")

        self.label_descripcion_dos = Label(screen= self._slave,
                                           x= 0,
                                           y= 170,
                                           w= w,
                                           h= 150,
                                           text= "LAS SEMILLAS Y CAPSULAS SON MUY IMPORTANTES!",
                                           font= "Avenir Next",
                                           font_size= 20,
                                           font_color= "White")

        self.label_descripcion_tres = Label(screen= self._slave,
                                           x= 0,
                                           y= 170,
                                           w= w,
                                           h= 150,
                                           text= "CONSIGUE LAS 7 ESFERAS DEL DRAGÓN Y DERROTA AL JEFE FINAL!",
                                           font= "Avenir Next",
                                           font_size= 20,
                                           font_color= "White")

        self.boton_continuar = Button(self._slave, x, y, w-200, h-50, 200, 40, NARANJA, "Blue", self.btn_continuar_click, "Nombre", "COMENZAR NIVEL", "Avenir Next", 20, "Black")

        self.boton_home = ButtonImage(self._slave, x, y, 0, h-50, 50, 50, "dbz_pygame/recursos/ui/btn_home.png", self.btn_home_click, "x")

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_enemigos)
        self.lista_widgets.append(self.label_cantidad)
        self.lista_widgets.append(self.icono_enemigo)
        self.lista_widgets.append(self.label_descripcion_uno)
        if nivel["numero"] != 3:
            self.lista_widgets.append(self.label_descripcion_dos)
        else:
            self.lista_widgets.append(self.label_descripcion_tres)
        self.lista_widgets.append(self.boton_continuar)
        self.lista_widgets.append(self.boton_home)

    def btn_continuar_click(self, param) -> None:
        self.pausado = False
        self.end_dialog()

    def btn_home_click(self, param) -> None:
        pygame.mixer.init()
        self.jugando = False
        self.pausado = False
        pygame.mixer.music.load("dbz_pygame/recursos/efectos_de_sonido/fondo.ogg")
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1) # bucle
        self.end_dialog()

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

        return super().update(lista_eventos)
