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
from UI.GUI_form import Form
from UI.GUI_label import Label
from UI.GUI_button_image import ButtonImage

class FormHistoria(Form):
    '''class form historia'''
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active, path_img):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.label = Label(screen=self._slave,
                           x= 0,
                           y= 0,
                           w= w,
                           h= 50,
                           text= "HISTORIA DEL JUEGO",
                           font= "Avenir Next",
                           font_size= 30,
                           font_color= "White",
                           path_image= "dbz_pygame/recursos/ui/text_box.png")

        self.label_uno = Label(screen= self._slave,
                               x= 0,
                               y= 70,
                               w= w,
                               h= 50,
                               text= "EN UN UNIVERSO ALTERNATIVO GOKU ES EL UNICO SOBREVIVIENTE EN LA TIERRA",
                               font= "Avenir Next",
                               font_size= 20,
                               font_color= "White")

        self.label_dos = Label(screen= self._slave,
                               x= 0,
                               y= 120,
                               w= w,
                               h= 50,
                               text= "ES NECESSARIO CONSEGUIR LAS SIETE ESFERAS DEL DRAGON LO ANTES POSIBLE PARA REVIVIR A SUS AMIGOS",
                               font= "Avenir Next",
                               font_size= 20,
                               font_color= "White")

        self.label_tres = Label(screen=self._slave,
                                x= 0,
                                y= 170,
                                w= w,
                                h= 50,
                                text= "SUS ENEMIGOS MAS TEMIDOS INTENTARAN INTERPONERSE EN SU CAMINO",
                                font= "Avenir Next",
                                font_size= 20,
                                font_color= "White")

        self.label_cuatro = Label(screen= self._slave,
                                  x= 0,
                                  y= 220,
                                  w= w,
                                  h= 50,
                                  text= "PREPARATE PARA LUCHAR PORQUE NO SERA FACIL",
                                  font= "Avenir Next",
                                  font_size= 20,
                                  font_color= "White")

        self.boton_atras = ButtonImage(self._slave, x, y, w-50, h-50, 50, 50, "dbz_pygame/recursos/ui/btn_reset.png", self.btn_back_click, "x")

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_uno)
        self.lista_widgets.append(self.label_dos)
        self.lista_widgets.append(self.label_tres)
        self.lista_widgets.append(self.label_cuatro)
        self.lista_widgets.append(self.boton_atras)

    def btn_back_click(self, param) -> None:
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
