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
'''
FORMULARIO INICIO
'''
import pygame
from UI.GUI_form import Form
from UI.GUI_button import Button
from UI.GUI_form_niveles import FormNiveles
from UI.GUI_form_reglas import FormReglas
from UI.GUI_form_settings import FormSettings
from UI.GUI_textbox import TextBox
from UI.GUI_label import Label
from UI.GUI_button_image import ButtonImage
from UI.GUI_form_ranking import FormRanking
from herramientas.config_bdd import buscar_usuario_bdd, insertar_jugador, traer_ranking_bdd, crear_base, verificar_tabla_existente
from herramientas.datos_juego import NARANJA, HEIGHT, TRANSPARENTE, WIDTH

class FormInicio(Form):
    '''class form inicio'''
    def __init__(self, screen, x, y, w, h, path_image, color_border="Magenta", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, TRANSPARENTE, color_border, border_size, active)

        self.usuario_existente = False
        self.flag_jugar = False
        self.nivel = 0
        self.sonido_silenciado = False

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        pygame.mixer.init()

        ancho_label = 250
        alto_label = 40
        ancho_txt = 330
        alto_txt = 30

        pos_x = w/2 - 250
        self.centro = w/2
        pos_x_label_uno = w/4 - ancho_label/2
        pos_x_label_dos = (w/4)*3 - ancho_label/2

        pos_x_txt_uno = w/4 - ancho_txt/2
        pos_x_txt_dos = (w/4)*3 - ancho_txt/2

        y_uno = 120
        espacio = 15

        ancho_btn = 50

        self.label_bienvenida = Label(self._slave, pos_x, 10, 500, 50, "BIENVENIDO", "Avenir Next", 40, "White", "dbz_pygame/recursos/ui/text_box.png")

        self.usuario_jugador = ""

        self.label_jugador_nuevo = Label(self._slave, pos_x_label_uno, y_uno, ancho_label, alto_label, "NUEVO JUGADOR", "Avenir Next", 20, "White", "dbz_pygame/recursos/ui/text_box.png")

        self.usuario_jugador_nuevo = TextBox(self._slave, x, y, pos_x_txt_uno, y_uno + alto_label + espacio, ancho_txt, alto_txt, "Grey", "White", NARANJA, NARANJA, 5, "Avenir Next", 20, "Black")

        self.boton_crear_jugar = Button(self._slave, x, y, pos_x_txt_uno,  y_uno + alto_txt + alto_label + espacio*2, ancho_txt, 50, NARANJA, "Blue", self.btn_crear_jugar_click, "Nombre", "INICIAR AVENTURA", "Avenir Next", 25, "Black")

        self.label_jugador_existente = Label(self._slave, pos_x_label_dos, y_uno, ancho_label, alto_label, "JUGADOR EXISTENTE", "Avenir Next", 20,  "White", "dbz_pygame/recursos/ui/text_box.png")

        self.usuario_jugador_existente = TextBox(self._slave, x,y, pos_x_txt_dos, y_uno + alto_label + espacio, ancho_txt, alto_txt, "Grey", "White", NARANJA, NARANJA, 5, "Avenir Next", 20, "Black")

        self.boton_jugar = Button(self._slave, x, y, pos_x_txt_dos, y_uno + alto_txt + alto_label + espacio*2, ancho_txt, 50,NARANJA, "Blue", self.btn_jugar_click, "Nombre", "CONTINUAR AVENTURA", "Avenir Next", 23, "Black")

        self.boton_ranking = ButtonImage(self._slave, x, y, w/2 - ancho_btn * 1.5 - 5, 200, ancho_btn, ancho_btn, "dbz_pygame/recursos/ui/btn_ranking.png", self.btn_ranking_click, "x")

        self.boton_settings = ButtonImage(self._slave, x, y, w/2-ancho_btn/2, 200, ancho_btn, ancho_btn, "dbz_pygame/recursos/ui/btn_config.png", self.btn_settings_click, "x")

        self.boton_reglas = ButtonImage(self._slave, x, y, w/2+ ancho_btn*0.5 + 5, 200, ancho_btn, ancho_btn, "dbz_pygame/recursos/ui/btn_info.png", self.btn_info_click, "x")

        self.label_error = Label(self._slave, self.centro-115, 365, 215, 45, "", "Avenir Next", 20, "White", "dbz_pygame/recursos/ui/text_box.png")

        self.mostrar_error = False

        self.lista_widgets.append(self.label_bienvenida)
        self.lista_widgets.append(self.label_jugador_nuevo)
        self.lista_widgets.append(self.label_jugador_existente)
        self.lista_widgets.append(self.usuario_jugador_nuevo)
        self.lista_widgets.append(self.usuario_jugador_existente)
        self.lista_widgets.append(self.boton_crear_jugar)
        self.lista_widgets.append(self.boton_jugar)
        self.lista_widgets.append(self.boton_settings)
        self.lista_widgets.append(self.boton_ranking)
        self.lista_widgets.append(self.label_error)
        self.lista_widgets.append(self.boton_reglas)

        pygame.mixer.music.load("dbz_pygame/recursos/efectos_de_sonido/fondo.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.render()

    def mostrar_label_error(self, mensaje) -> None:
        self.label_error.set_text(mensaje)

    def btn_crear_jugar_click(self, param):
        if not verificar_tabla_existente("Jugadores", "dbz_pygame/jugadores.bdd"):
            crear_base()
        else:
            if self.usuario_jugador_nuevo.get_text() != "":
                guardado = insertar_jugador(0, 0, self.usuario_jugador_nuevo.get_text(), "dbz_pygame/jugadores.bdd")

                if guardado:
                    self.usuario_jugador = {
                        "usuario": self.usuario_jugador_nuevo.get_text(),
                        "puntos": 0,
                        "nivel_max": 0
                    }

                    self.label_error.set_text("")
                    self.flag_jugar = True
                else:
                    self.mostrar_label_error("Ya existe ese usuario")

    def btn_jugar_click(self, param):
        if self.usuario_jugador_existente.get_text() != "":
            usuario = buscar_usuario_bdd("dbz_pygame/jugadores.bdd", self.usuario_jugador_existente.get_text())
            if usuario:
                self.usuario_jugador = {
                    "usuario": usuario[0],
                    "puntos": usuario[1],
                    "nivel_max": usuario[2]
                }

                form_niveles = FormNiveles(self._master,
                                           x= self._w/2-(500/2),
                                           y= 25,
                                           w= 500,
                                           h= 550,
                                           nivel_max= self.usuario_jugador['nivel_max'],
                                           color_background= (220,0,220),
                                           color_border= "White",
                                           border_size= -1,
                                           active= True)

                self.label_error.set_text("")
                self.show_dialog(form_niveles)
            else:
                self.mostrar_label_error("Usuario inexistente")

    def btn_ranking_click(self, param):
        dic_score = traer_ranking_bdd("dbz_pygame/jugadores.bdd")

        form_ranking = FormRanking(self._master,
                                   x= self._w/2-(500/2),
                                   y= 25,
                                   w= 500,
                                   h= 550,
                                   color_background= TRANSPARENTE,
                                   color_border= "White",
                                   border_size= -1,
                                   active= True,
                                   scores= dic_score,
                                   margen_x= 10,
                                   margen_y= 100,
                                   espacio= 10)

        self.show_dialog(form_ranking)

    def btn_settings_click(self, param):
        form_settings = FormSettings(self._master,
                                     x= WIDTH/2-400,
                                     y= 25,
                                     w= 800,
                                     h= 500,
                                     color_background= TRANSPARENTE,
                                     color_border= "White",
                                     border_size= -1,
                                     active= True)

        self.show_dialog(form_settings)

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
        self.draw()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
        else:
            self.hijo.update(lista_eventos)
