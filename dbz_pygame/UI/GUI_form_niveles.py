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
from UI.GUI_button_image import ButtonImage
from UI.GUI_form import Form
from UI.GUI_label import Label

NARANJA = (64, 207, 255)

class FormNiveles(Form):
    '''class form niveles'''
    def __init__(self, screen, x, y, w, h, nivel_max, color_background=None, color_border="Magenta", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        ancho_label = 300
        alto_label = 50
        alto_nivel = 40
        ancho_nivel = 200
        pos_x_label_uno = (w-ancho_label)/2
        pos_x_niveles = (w-ancho_nivel)/2

        y_uno = 90
        espacio = 20

        self.nivel_max = nivel_max

        self.label_elegir = Label(self._slave, pos_x_label_uno, 10, ancho_label, 50, "ELEGIR NIVEL", "Avenir Next", 40, "White", "dbz_pygame/recursos/ui/text_box.png")

        pos_inicial_y = y_uno

        for nivel in range(nivel_max+1):

            boton_nivel = ButtonImage(self._slave,
                                      x= pos_x_niveles,
                                      y= pos_inicial_y,
                                      master_x= x,
                                      master_y= y,
                                      w= ancho_nivel,
                                      h= alto_nivel,
                                      color_background= None,
                                      color_border= (255,0,255),
                                      border_size= -1,
                                      onclick= self.btn_jugar_click,
                                      onclick_param= nivel,
                                      font= "Avenir Next",
                                      font_size= 25,
                                      font_color= "White",
                                      path_image= "dbz_pygame/recursos/ui/text_box.png",
                                      text= f"NIVEL {nivel+1}")

            self.lista_widgets.append(boton_nivel)

            pos_inicial_y += alto_label + espacio

        self.boton_atras = ButtonImage(self._slave,
                                       x= pos_x_niveles + 150,
                                       y= pos_inicial_y + 150,
                                       master_x= x,
                                       master_y= y,
                                       w=70,
                                       h= 70,
                                       color_background= None,
                                       color_border= (255,0,255),
                                       border_size= -1,
                                       onclick= self.btn_atras_click,
                                       onclick_param= "",
                                       font= "Avenir Next",
                                       font_size= 25,
                                       font_color= "White",
                                       path_image= "dbz_pygame/recursos/ui/btn_reset.png",
                                       text= "")

        self.lista_widgets.append(self.label_elegir)
        self.lista_widgets.append(self.boton_atras)
        self.render()

    def btn_jugar_click(self, param):
        self.end_dialog()
        self.padre.nivel = param
        self.padre.flag_jugar = True

    def btn_atras_click(self, param):
        self.end_dialog()

    def render(self):
        self.draw()

    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()

            for widget in self.lista_widgets:
                widget.update(lista_eventos)

        return super().update(lista_eventos)
