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
# pylint: disable=attribute-defined-outside-init
# pylint: disable=invalid-name
# pylint: disable=unused-argument
import unicodedata
import pygame
from UI.GUI_widget import Widget

FPS = 18

class TextBox(Widget):
    '''clase text box'''
    def __init__(self, screen, master_x, master_y, x, y, w, h, color_background, color_background_seleccionado, color_border, color_border_seleccionado, border_size , font, font_size, font_color):

        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        pygame.font.init()
        self._color_background_default = color_background
        self._color_border_default = color_border
        self._color_background_seleccionado = color_background_seleccionado
        self._color_border_seleccionado = color_border_seleccionado
        self._text = ""
        self._font = pygame.font.SysFont(font,font_size)
        self._font_color = font_color
        self._master_x = master_x
        self._master_y = master_y

        self.is_selected = False

        self.render()

    def get_text(self):
        '''getter text'''
        return self._text

    def set_text(self, texto):
        '''setter text'''
        self._text = texto
        self.render()

    def render(self):
        '''render text'''
        image_text = self._font.render(self._text, True, self._font_color, self._color_background)

        self._slave = pygame.Surface((self._w,self._h))

        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y

        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self._master_x
        self.slave_rect_collide.y += self._master_y

        self._slave.fill(self._color_background)

        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self._w / 2
        media_vertical = self._h / 2
        diferencia_horizontal = media_horizontal - media_texto_horizontal
        diferencia_vertical = media_vertical - media_texto_vertical

        self._slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))

    def update(self, lista_eventos):
        '''actualiza'''
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.slave_rect_collide.collidepoint(evento.pos):
                    self._color_background = self._color_background_seleccionado
                    self._color_border = self._color_border_seleccionado
                    self.is_selected = True
                else:
                    self._color_background = self._color_background_default
                    self._color_border = self._color_border_default
                    self.is_selected = False
                self.render()
            elif self.is_selected and evento.type == pygame.KEYDOWN:
                caracter = evento.unicode
                if evento.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                elif len(caracter) == 1 and unicodedata.category(caracter)[0] != 'C':
                    self._text += caracter
                self.render()
        self.draw()
