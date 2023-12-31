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

NARANJA = (255, 128, 0)
TRANSPARENTE = (0,0,0,0)

class FormFinal(Form):
    '''class form final'''
    def __init__(self, screen, x, y, w, h, path_image, estado_juego, puntos, color_background=None, color_border="Magenta", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        pos_x = w/2 - 250

        self.estado_juego = estado_juego

        if estado_juego == "gano":
            texto = f"GANASTE - TUS PUNTOS: {puntos}"
        elif estado_juego == "perdio":
            texto = "PERDISTE: NO ALCANZASTE EL OBJETIVO"
        else:
            texto = "PERDISTE: TE QUEDASTE SIN VIDA"

        self.label_bienvenida = Label(self._slave, pos_x, 60, 550, 100, f"{texto}", "Avenir Next", 20, "White", "dbz_pygame/recursos/ui/text_box.png")

        self.boton_home = Button(self._slave, x, y, w/2-150, h/2+100, 300, 50, NARANJA, "Blue", self.btn_home_click, "x", "VOLVER AL MENU PRINCIPAL", "Avenir Next", 20, "Black")

        self.lista_widgets.append(self.label_bienvenida)
        self.lista_widgets.append(self.boton_home)

        pygame.mixer.init()
        pygame.mixer.music.rewind()
        pygame.mixer.music.pause()

        self.render()

    def btn_home_click(self, param) -> None:
        self.estado_juego = "again"

    def render(self):
        self.draw()

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
