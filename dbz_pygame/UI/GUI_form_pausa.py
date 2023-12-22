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
from UI.GUI_form import Form
from UI.GUI_form_inicio import TRANSPARENTE
from UI.GUI_form_reglas import FormReglas
from UI.GUI_label import Label
from UI.GUI_button_image import ButtonImage
from herramientas.datos_juego import HEIGHT, WIDTH

class FormPausa(Form):
    '''class form pausa'''
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        self.jugando = True
        self.pausado = True
        self.estado_musica = pygame.mixer.music.get_busy()
        pygame.mixer.music.pause()

        ancho_btn = 50

        self.label = Label(screen=self._slave,
                           x= 0,
                           y= 100,
                           w= w,
                           h= 50,
                           text= "JUEGO PAUSADO",
                           font= "Avenir Next",
                           font_size= 35,
                           font_color= "White",
                           path_image= "dbz_pygame/recursos/ui/text_box.png")

        self.boton_atras = ButtonImage(self._slave, x, y, 0, h/2, ancho_btn, ancho_btn, "dbz_pygame/recursos/ui/btn_reset.png", self.btn_back_click, "x")

        self.boton_home = ButtonImage(self._slave, x, y, w-ancho_btn, h/2, ancho_btn, ancho_btn, "dbz_pygame/recursos/ui/btn_home.png", self.btn_home_click, "x")

        self.boton_reglas = ButtonImage(self._slave, x, y, w/2-ancho_btn/2, h/2, ancho_btn, ancho_btn, "dbz_pygame/recursos/ui/btn_info.png", self.btn_info_click, "x")

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.boton_home)
        self.lista_widgets.append(self.boton_atras)
        self.lista_widgets.append(self.boton_reglas)

    def btn_home_click(self, param) -> None:
        pygame.mixer.init()
        self.jugando = False
        self.pausado = False
        pygame.mixer.music.load("dbz_pygame/recursos/efectos_de_sonido/fondo.ogg")
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1)
        self.end_dialog()

    def btn_back_click(self, param) -> None:
        self.pausado = False

        if self.estado_musica is True:
            pygame.mixer.music.unpause()

        self.end_dialog()

    def btn_info_click(self, param):
        form_info = FormReglas(self._master,
                               x= WIDTH/2-((WIDTH-200)/2),
                               y= 50,
                               w= WIDTH-200,
                               h= HEIGHT-100,
                               color_background= TRANSPARENTE,
                               color_border= "White",
                               border_size= -1,
                               active= True)

        self.show_dialog(form_info)

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
