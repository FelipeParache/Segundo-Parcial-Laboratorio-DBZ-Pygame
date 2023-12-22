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

class Widget:
    '''clase widget'''
    def __init__(self,screen, x, y, w, h, color_background=None, color_border="Red", border_size=-1):

        self._master = screen
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._color_background = color_background
        self._color_border = color_border
        self._slave = None
        self.slave_rect = None
        self.border_size = border_size

    def render(self):
        pass

    def update(self, lista_eventos):
        pass

    def draw(self):
        self._master.blit(self._slave,self.slave_rect)
        pygame.draw.rect(self._master, self._color_border, self.slave_rect, self.border_size)
