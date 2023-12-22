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

class PictureBox(Widget):
    """
    Clase que representa un cuadro de imagen en una interfaz gráfica.
    Hereda de la clase Widget.
    """
    def __init__(self, screen, x, y, w, h, path_image):
        """
        Inicializa una instancia de PictureBox.

        Argumentos:
        - screen: La superficie de la pantalla donde se dibujará el cuadro de imagen.
        - x: Coordenada x del punto de referencia del widget en la superficie dada.
        - y: Coordenada y del punto de referencia del widget en la superficie dada.
        - w: Ancho del cuadro de imagen.
        - h: Altura del cuadro de imagen.
        - path_image: Ruta de la imagen a cargar en el cuadro de imagen.
        """
        super().__init__(screen, x, y, w, h)

        self.esta_prendido = False

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))

        self._slave = aux_image

        self.render()

    def render(self):
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y

    def update(self, lista_eventos):
        self.draw()

    def set_imagen(self, imagen: pygame.Surface):
        self._slave = imagen
