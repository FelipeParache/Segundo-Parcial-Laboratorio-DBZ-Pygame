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

class FormRanking(Form):
    '''class form ranking'''
    def __init__(self, screen, x, y, w, h,color_background, color_border, border_size, active, scores, margen_x, margen_y, espacio):
        super().__init__(screen, x,y, w,h,color_background, color_border, border_size, active)

        self._scores = scores
        self._margen_x = margen_x
        self._margen_y = margen_y

        pos_x_label = margen_x + 10
        ancho_label = w/2-margen_x-10

        self.label_usuario = Label(self._slave, pos_x_label, 25, ancho_label, 50, "USUARIO", "Avenir Next", 30, "White", "dbz_pygame/recursos/ui/text_box.png")

        self.label_puntos = Label(self._slave, pos_x_label + ancho_label, 25, w/2-margen_x-10, 50, "PUNTOS", "Avenir Next", 30, "White", "dbz_pygame/recursos/ui/text_box.png")

        self.boton_home = ButtonImage(self._slave,
                                      x= w-70,
                                      y= h-70,
                                      master_x= x,
                                      master_y= y,
                                      w= 50,
                                      h= 50,
                                      color_background= (255,0,0),
                                      color_border= (255,0,255),
                                      onclick= self.btn_home_click,
                                      onclick_param= "",
                                      font_size= 25,
                                      font_color= (0,255,0),
                                      path_image= "dbz_pygame/recursos/ui/btn_home.png")

        self.lista_widgets.append(self.label_usuario)
        self.lista_widgets.append(self.label_puntos)
        self.lista_widgets.append(self.boton_home)

        pos_inicial_y = margen_y

        if type(self._scores) == bool:
            pass
        else:
            for jugador in self._scores:
                pos_inicial_x = margen_x
                for x in jugador:
                    cadena = ""
                    cadena += f"{x}"
                    aux = Label(self._slave, pos_inicial_x, pos_inicial_y, w/2-margen_x, 50, cadena, "Avenir Next", 30, "White", "dbz_pygame/recursos/ui/text_box.png")
                    self.lista_widgets.append(aux)
                    pos_inicial_x += w/2 - margen_x

                pos_inicial_y += 50 + espacio

    def btn_home_click(self, param) -> None:
        self.end_dialog()

    def render(self):
        self.draw()
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.render()
        return super().update(lista_eventos)
