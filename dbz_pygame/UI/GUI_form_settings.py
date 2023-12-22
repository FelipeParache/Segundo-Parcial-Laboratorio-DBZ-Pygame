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
from UI.GUI_button import Button
from UI.GUI_label import Label
from UI.GUI_slider import Slider
from UI.GUI_button_image import ButtonImage

NARANJA = (255, 128, 0)

class FormSettings(Form):
    '''class form settings'''
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        pygame.mixer.init()
        ancho_txt = 500
        pos_x = w/2 - 250
        pos_x_txt_dos = w/2 - ancho_txt/2
        ancho_slider = 500
        pos_x_slider = w/2 - ancho_slider/2
        ancho_label_volumen = 70
        pos_x_label_volumen = w/2 - ancho_label_volumen/2
        self.jugando = True
        self.pausado = True
        self.sonido_silenciado = False
        self.label_settings = Label(self._slave, pos_x, 10, 500, 50, "CONFIGURACION", "Avenir Next", 30, "White", "dbz_pygame/recursos/ui/text_box.png")
        self.label_volumen = Label(self._slave, pos_x_txt_dos, 60, ancho_txt, 80, "VOLUMEN MUSICA", "Avenir Next", 30, "White", "")
        self.label_porcentaje_volumen = Label(self._slave, pos_x_label_volumen, 150, 80, 80, '', "Avenir Next", 30, "White", "dbz_pygame/recursos/ui/text_box.png")
        self.slider_volumen = Slider(self._slave, x, y, pos_x_slider, 250, ancho_slider, 15, pygame.mixer.music.get_volume(), "White", NARANJA)

        if pygame.mixer.music.get_busy():
            texto_musica = "SILENCIAR MUSICA"
        else:
            texto_musica = "REANUDAR MUSICA"

        self.boton_musica = Button(self._slave, x, y, w/2-ancho_txt/2, 300, ancho_txt, 50, NARANJA, "Blue", self.btn_play_click, "x", texto_musica, "Avenir Next", 30, "Black")
        self.boton_atras = ButtonImage(self._slave,
                                       x= w-70,
                                       y= h-70,
                                       master_x= x,
                                       master_y= y,
                                       w= 50,
                                       h= 50,
                                       color_background= (255,0,0),
                                       color_border= (255,0,255),
                                       onclick= self.btn_back_click,
                                       onclick_param= "",
                                       font_size= 25,
                                       font_color= (0,255,0),
                                       path_image= "dbz_pygame/recursos/ui/btn_reset.png")

        self.lista_widgets.append(self.label_settings)
        self.lista_widgets.append(self.boton_musica)
        self.lista_widgets.append(self.label_porcentaje_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.boton_atras)
        self.render()

    def btn_play_click(self, param):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.boton_musica.set_text("REANUDAR MUSICA")
        else:
            pygame.mixer.music.unpause()
            self.boton_musica.set_text("SILENCIAR MUSICA")

    def update_volumen(self, lista_eventos):
        nuevo_texto = f"{round(self.slider_volumen.value * 100)}%"
        self.label_porcentaje_volumen.set_text(nuevo_texto)
        pygame.mixer.music.set_volume(self.slider_volumen.value)

    def btn_back_click(self, param) -> None:
        self.pausado = False
        self.end_dialog()

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

            self.update_volumen(lista_eventos)

        return super().update(lista_eventos)
