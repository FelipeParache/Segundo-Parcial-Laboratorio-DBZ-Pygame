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
from UI.GUI_widget import Widget

class Form(Widget):
    '''class form'''
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        self._slave = pygame.Surface((w,h))
        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None

    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo is None or self.hijo.dialog_result is not None

    def render(self):
        pass

    def update(self, lista_eventos):
        pass
