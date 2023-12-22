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
from UI.GUI_button import Button
from UI.GUI_form import Form
from UI.GUI_form_estado_juego import NARANJA
from UI.GUI_form_historia import FormHistoria
from UI.GUI_label import Label
from UI.GUI_button_image import ButtonImage
from UI.GUI_picture_box import PictureBox
from herramientas.datos_juego import HEIGHT, TRANSPARENTE, WIDTH

class FormReglas(Form):
    '''class form reglas'''
    def __init__(self, screen, x, y, w, h, color_background, color_border, border_size, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.label = Label(screen=self._slave,
                           x= 0,
                           y= 0,
                           w= w,
                           h= 50,
                           text= "REGLAS E INFORMACION",
                           font= "Avenir Next",
                           font_size= 30,
                           font_color= "White",
                           path_image= "dbz_pygame/recursos/ui/text_box.png")

        self.icono_vidas_goku = PictureBox(self._slave, 20, 70, 65, 65, "dbz_pygame/recursos/goku_super_saiyajin/cabeza_goku.png")

        self.label_vidas = Label(screen= self._slave,
                                 x= 50,
                                 y= 80,
                                 w= 400,
                                 h= 50,
                                 text= "REPRESENTA LA VIDAS DE GOKU",
                                 font= "Avenir Next",
                                 font_size= 18,
                                 font_color= "White")

        self.icono_cantidad_cell = PictureBox(self._slave, 20, 160, 65, 65, "dbz_pygame/recursos/cell/cabeza_cell.png")

        self.label_cantidad_cell = Label(screen= self._slave,
                                         x= 90,
                                         y= 170,
                                         w= 450,
                                         h= 50,
                                         text= "CANTIDAD DE ENEMIGOS A DERROTAR EN EL PRIMER NIVEL",
                                         font= "Avenir Next",
                                         font_size= 15,
                                         font_color= "White")

        self.icono_cantidad_freezer = PictureBox(self._slave, 20, 250, 65, 65, "dbz_pygame/recursos/freezer/cabeza_freezer.png")

        self.label_cantidad_freezer = Label(screen= self._slave,
                                            x= 75,
                                            y= 260,
                                            w= 500,
                                            h= 50,
                                            text= "CANTIDAD DE ENEMIGOS A DERROTAR EN EL SEGUNDO NIVEL",
                                            font= "Avenir Next",
                                            font_size= 15,
                                            font_color= "White")

        self.icono_vidas_boss = PictureBox(self._slave, 20, 340, 65, 65, "dbz_pygame/recursos/ultimate_cell/cabeza_ultimate_cell.png")

        self.label_vidas_boss = Label(screen= self._slave,
                                      x= 40,
                                      y= 350,
                                      w= 500,
                                      h= 50,
                                      text= "REPRESENTA LA VIDA DEL ULTIMATE CELL (BOSS)",
                                      font= "Avenir Next",
                                      font_size= 15,
                                      font_color= "White")

        self.icono_semilla = PictureBox(self._slave, w/2+50, 70, 65, 65, "dbz_pygame/recursos/power_ups/semilla_vida.png")

        self.label_semilla = Label(screen= self._slave,
                                   x= w/2+130,
                                   y= 80,
                                   w= 170,
                                   h= 50,
                                   text= "+1 VIDA AL RECOGER",
                                   font= "Avenir Next",
                                   font_size= 15,
                                   font_color= "White")

        self.icono_capsula = PictureBox(self._slave, w/2+50, 170, 65, 65, "dbz_pygame/recursos/power_ups/capsula_ki.png")

        self.label_capsula = Label(screen= self._slave,
                                   x= w/2+115,
                                   y= 170,
                                   w= 200,
                                   h= 50,
                                   text= "+5 KI AL RECOGER",
                                   font= "Avenir Next",
                                   font_size= 15,
                                   font_color= "White")

        self.icono_trampa = PictureBox(self._slave, w/2+50, 260, 65, 65, "dbz_pygame/recursos/trampa.png")

        self.label_trampa = Label(screen= self._slave,
                                    x= w/2+115,
                                    y= 260,
                                    w= 200,
                                    h= 50,
                                    text= "-10 VIDA Y PTS AL TOCAR",
                                    font= "Avenir Next",
                                    font_size= 15,
                                    font_color= "White")

        self.icono_esfera = PictureBox(self._slave, w/2+50, 350, 65, 65, "dbz_pygame/recursos/esferas/siete.png")

        self.label_esfera = Label(screen= self._slave,
                                    x= w/2+115,
                                    y= 350,
                                    w= 200,
                                    h= 50,
                                    text= "+500 PTS AL RECOGER",
                                    font= "Avenir Next",
                                    font_size= 15,
                                    font_color= "White")

        self.label_enemigos = Label(screen= self._slave,
                                    x= 0,
                                    y= 550,
                                    w= w,
                                    h= 50,
                                    text= "TODOS LOS ENEMIGOS DISPARAN PROYECTILES - SI TOCAS AL ENEMIGO O UN PROYECTIL TE ALCANZA PERDERAS VIDAS",
                                    font= "Avenir Next",
                                    font_size= 20,
                                    font_color= "White")

        self.boton_atras = ButtonImage(self._slave, x, y, w-50, h-50, 50, 50, "dbz_pygame/recursos/ui/btn_reset.png", self.btn_back_click, "x")

        self.boton_historia = Button(self._slave, x, y, w-150, 70, 150, 40, NARANJA, "Blue", self.btn_historia_click, "Nombre", "HISTORIA", "Avenir Next", 20, "Black")

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_vidas)
        self.lista_widgets.append(self.boton_atras)
        self.lista_widgets.append(self.icono_vidas_goku)
        self.lista_widgets.append(self.icono_cantidad_cell)
        self.lista_widgets.append(self.label_cantidad_cell)
        self.lista_widgets.append(self.icono_cantidad_freezer)
        self.lista_widgets.append(self.label_cantidad_freezer)
        self.lista_widgets.append(self.icono_vidas_boss)
        self.lista_widgets.append(self.label_vidas_boss)
        self.lista_widgets.append(self.icono_semilla)
        self.lista_widgets.append(self.label_semilla)
        self.lista_widgets.append(self.icono_capsula)
        self.lista_widgets.append(self.label_capsula)
        self.lista_widgets.append(self.icono_trampa)
        self.lista_widgets.append(self.label_trampa)
        self.lista_widgets.append(self.icono_esfera)
        self.lista_widgets.append(self.label_esfera)
        self.lista_widgets.append(self.boton_historia)
        self.lista_widgets.append(self.label_enemigos)

    def btn_historia_click(self, param) -> None:
        form_historia = FormHistoria(self._master,
                                     x= WIDTH/2-((WIDTH-200)/2),
                                     y= 50,
                                     w= WIDTH-200,
                                     h= HEIGHT-100,
                                     color_background= TRANSPARENTE,
                                     color_border= "White",
                                     border_size= -1,
                                     active= True,
                                     path_img= "")

        self.show_dialog(form_historia)

    def btn_back_click(self, param) -> None:
        self.end_dialog()

    def render(self):
        self._slave.fill(self._color_background)
        # self._slave.blit()

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
