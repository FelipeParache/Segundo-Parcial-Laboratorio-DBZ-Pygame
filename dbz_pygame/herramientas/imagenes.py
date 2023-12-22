# pylint: disable=consider-using-dict-items
# pylint: disable=non-ascii-name
# pylint: disable=consider-using-enumerate
# pylint: disable=line-too-long
'''funciones para las imagenes'''
import pygame

#################### FUNCIONES DE CONFIGURACIÓN ####################

def reescalar_imagenes(diccionario_animaciones:dict, tamaño:tuple) -> None:
    '''Ajusta las imagenes al tamaño que se le pasa por parametro'''
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = pygame.transform.scale(img, tamaño)

def rotar_imagenes(lista_imagenes:list) -> list:
    '''Rota las imagenes'''
    lista_imagenes_rotadas = []
    for imagen in lista_imagenes:
        imagen_rotada = pygame.transform.flip(imagen, True, False)
        lista_imagenes_rotadas.append(imagen_rotada)
    return lista_imagenes_rotadas

def obtener_rectangulos(rectangulo_principal:pygame.Rect) -> dict:
    '''Obtiene los lados del rectangulo'''
    diccionario = {}
    diccionario = {
        'main': rectangulo_principal,
        'bottom': pygame.Rect(rectangulo_principal.left, rectangulo_principal.bottom-10, rectangulo_principal.width, 10),
        'right': pygame.Rect(rectangulo_principal.right-5, rectangulo_principal.top, 5, rectangulo_principal.height),
        'left': pygame.Rect(rectangulo_principal.left, rectangulo_principal.top, 5, rectangulo_principal.height),
        'top': pygame.Rect(rectangulo_principal.left, rectangulo_principal.top, rectangulo_principal.width, 10)
    }

    return diccionario

def dibujar_rectangulos(pantalla:pygame.Surface, lados_rectangulo:dict, color:str):
    '''Dibuja los rectangulos de un color'''
    for lado in lados_rectangulo:
        pygame.draw.rect(pantalla, color, lados_rectangulo[lado], 3)

#################### CARGAS DE ANIMACINOES ####################
# jugador goku
goku_quieto_derecha = [pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/quieto/quieto2.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/quieto/quieto3.png")]

goku_quieto_izquierda = rotar_imagenes(goku_quieto_derecha)

goku_camina_derecha = [pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/camina/camina1.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/camina/camina2.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/camina/camina3.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/camina/camina4.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/camina/camina5.png")]

goku_camina_izquierda = rotar_imagenes(goku_camina_derecha)

goku_salta_derecha = [pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/salta/salta2.png")]

goku_salta_izquierda = rotar_imagenes(goku_salta_derecha)

goku_lanza_ki_derecha = [pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/bola_de_ki/bola_de_ki3.png")]

goku_lanza_ki_izquierda = rotar_imagenes(goku_lanza_ki_derecha)

goku_golpea_derecha = [pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/golpe/golpe1.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/golpe/golpe2.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/golpe/golpe3.png"),
                       pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/golpe/golpe4.png")]

goku_golpea_izquierda = rotar_imagenes(goku_golpea_derecha)

goku_atacado_derecha = [pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/recibe_golpe/recibe_golpe1.png"),
                        pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/recibe_golpe/recibe_golpe2.png"),
                        pygame.image.load("dbz_pygame/recursos/goku_super_saiyajin/recibe_golpe/recibe_golpe3.png")]

goku_atacado_izquierda = rotar_imagenes(goku_atacado_derecha)

# enemigo cell
cell_quieto_derecha = [pygame.image.load("dbz_pygame/recursos/cell/quieto/quieto1.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/quieto/quieto2.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/quieto/quieto3.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/quieto/quieto4.png")]

cell_quieto_izquierda = rotar_imagenes(cell_quieto_derecha)

cell_camina_derecha = [pygame.image.load("dbz_pygame/recursos/cell/camina/camina1.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/camina/camina2.png")]

cell_camina_izquierda = rotar_imagenes(cell_camina_derecha)

cell_salta_derecha = [pygame.image.load("dbz_pygame/recursos/cell/salta/salta2.png")]

cell_salta_izquierda = rotar_imagenes(cell_salta_derecha)

cell_lanza_ki_derecha = [pygame.image.load("dbz_pygame/recursos/cell/bola_de_ki/bola_de_ki1.png")]

cell_lanza_ki_izquierda = rotar_imagenes(cell_lanza_ki_derecha)

cell_golpea_derecha = [pygame.image.load("dbz_pygame/recursos/cell/golpe/golpe1.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/golpe/golpe2.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/golpe/golpe3.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/golpe/golpe4.png"),
                       pygame.image.load("dbz_pygame/recursos/cell/golpe/golpe5.png")]

cell_golpea_izquierda = rotar_imagenes(cell_golpea_derecha)

cell_atacado_derecha = [pygame.image.load("dbz_pygame/recursos/cell/recibe_golpe/recibe_golpe1.png"),
                        pygame.image.load("dbz_pygame/recursos/cell/recibe_golpe/recibe_golpe2.png"),
                        pygame.image.load("dbz_pygame/recursos/cell/recibe_golpe/recibe_golpe3.png")]

cell_atacado_izquierda = rotar_imagenes(cell_atacado_derecha)

# enemigo freezer
freezer_quieto_derecha = [pygame.image.load("dbz_pygame/recursos/freezer/quieto/quieto3.png"),
                          pygame.image.load("dbz_pygame/recursos/freezer/quieto/quieto4.png")]

freezer_quieto_izquierda = rotar_imagenes(freezer_quieto_derecha)

freezer_camina_derecha = [pygame.image.load("dbz_pygame/recursos/freezer/camina/camina1.png"),
                          pygame.image.load("dbz_pygame/recursos/freezer/camina/camina3.png"),
                          pygame.image.load("dbz_pygame/recursos/freezer/camina/camina4.png")]

freezer_camina_izquierda = rotar_imagenes(freezer_camina_derecha)

freezer_salta_derecha = [pygame.image.load("dbz_pygame/recursos/freezer/salta/salta1.png")]

freezer_salta_izquierda = rotar_imagenes(freezer_salta_derecha)

freezer_lanza_ki_derecha = [pygame.image.load("dbz_pygame/recursos/freezer/bola_de_ki/bola_de_ki2.png")]

freezer_lanza_ki_izquierda = rotar_imagenes(freezer_lanza_ki_derecha)

freezer_golpea_derecha = [pygame.image.load("dbz_pygame/recursos/freezer/golpe/golpe1.png"),
                          pygame.image.load("dbz_pygame/recursos/freezer/golpe/golpe2.png"),
                          pygame.image.load("dbz_pygame/recursos/freezer/golpe/golpe3.png"),
                          pygame.image.load("dbz_pygame/recursos/freezer/golpe/golpe4.png")]

freezer_golpea_izquierda = rotar_imagenes(freezer_golpea_derecha)

freezer_atacado_derecha = [pygame.image.load("dbz_pygame/recursos/freezer/recibe_golpe/recibe_golpe1.png"),
                           pygame.image.load("dbz_pygame/recursos/freezer/recibe_golpe/recibe_golpe2.png"),
                           pygame.image.load("dbz_pygame/recursos/freezer/recibe_golpe/recibe_golpe3.png")]

freezer_atacado_izquierda = rotar_imagenes(freezer_atacado_derecha)

# enemigo ultimate cell
ultimate_quieto_derecha = [pygame.image.load("dbz_pygame/recursos/ultimate_cell/quieto/quieto2.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/quieto/quieto3.png")]

ultimate_quieto_izquierda = rotar_imagenes(ultimate_quieto_derecha)

ultimate_camina_derecha = [pygame.image.load("dbz_pygame/recursos/ultimate_cell/camina/camina1.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/camina/camina2.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/camina/camina3.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/camina/camina4.png")]

ultimate_camina_izquierda = rotar_imagenes(ultimate_camina_derecha)

ultimate_salta_derecha = [pygame.image.load("dbz_pygame/recursos/ultimate_cell/salta/salta1.png")]

ultimate_salta_izquierda = rotar_imagenes(ultimate_salta_derecha)

ultimate_lanza_ki_derecha = [pygame.image.load("dbz_pygame/recursos/ultimate_cell/bola_de_ki/bola_de_ki2.png")]

ultimate_lanza_ki_izquierda = rotar_imagenes(ultimate_lanza_ki_derecha)

ultimate_golpea_derecha = [pygame.image.load("dbz_pygame/recursos/ultimate_cell/golpe/golpe1.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/golpe/golpe2.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/golpe/golpe3.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/golpe/golpe4.png")]

ultimate_golpea_izquierda = rotar_imagenes(ultimate_golpea_derecha)

ultimate_atacado_derecha = [pygame.image.load("dbz_pygame/recursos/ultimate_cell/recibe_golpe/recibe_golpe1.png"),
                           pygame.image.load("dbz_pygame/recursos/ultimate_cell/recibe_golpe/recibe_golpe2.png")]

ultimate_atacado_izquierda = rotar_imagenes(ultimate_atacado_derecha)
#################### DICCIONARIOS DE ANIMACIONES ####################

animaciones_goku = {
    "quieto_derecha": goku_quieto_derecha,
    "quieto_izquierda": goku_quieto_izquierda,
    "camina_derecha": goku_camina_derecha,
    "camina_izquierda": goku_camina_izquierda,
    "salta_derecha": goku_salta_derecha,
    "salta_izquierda": goku_salta_izquierda,
    "lanza_ki_derecha": goku_lanza_ki_derecha,
    "lanza_ki_izquierda": goku_lanza_ki_izquierda,
    "golpea_derecha": goku_golpea_derecha,
    "golpea_izquierda": goku_golpea_izquierda,
    "atacado_derecha": goku_atacado_derecha,
    "atacado_izquierda": goku_atacado_izquierda
}

animaciones_cell = {
    "quieto_derecha": cell_quieto_derecha,
    "quieto_izquierda": cell_quieto_izquierda,
    "camina_derecha": cell_camina_derecha,
    "camina_izquierda": cell_camina_izquierda,
    "salta_derecha": cell_salta_derecha,
    "salta_izquierda": cell_salta_izquierda,
    "lanza_ki_derecha": cell_lanza_ki_derecha,
    "lanza_ki_izquierda": cell_lanza_ki_izquierda,
    "golpea_derecha": cell_golpea_derecha,
    "golpea_izquierda": cell_golpea_izquierda,
    "atacado_derecha": cell_atacado_derecha,
    "atacado_izquierda": cell_atacado_izquierda
}

animaciones_freezer = {
    "quieto_derecha": freezer_quieto_derecha,
    "quieto_izquierda": freezer_quieto_izquierda,
    "camina_derecha": freezer_camina_derecha,
    "camina_izquierda": freezer_camina_izquierda,
    "salta_derecha": freezer_salta_derecha,
    "salta_izquierda": freezer_salta_izquierda,
    "lanza_ki_derecha": freezer_lanza_ki_derecha,
    "lanza_ki_izquierda": freezer_lanza_ki_izquierda,
    "golpea_derecha": freezer_golpea_derecha,
    "golpea_izquierda": freezer_golpea_izquierda,
    "atacado_derecha": freezer_atacado_derecha,
    "atacado_izquierda": freezer_atacado_izquierda
}

animaciones_ultimate= {
    "quieto_derecha": ultimate_quieto_derecha,
    "quieto_izquierda": ultimate_quieto_izquierda,
    "camina_derecha": ultimate_camina_derecha,
    "camina_izquierda": ultimate_camina_izquierda,
    "salta_derecha": ultimate_salta_derecha,
    "salta_izquierda": ultimate_salta_izquierda,
    "lanza_ki_derecha": ultimate_lanza_ki_derecha,
    "lanza_ki_izquierda": ultimate_lanza_ki_izquierda,
    "golpea_derecha": ultimate_golpea_derecha,
    "golpea_izquierda": ultimate_golpea_izquierda,
    "atacado_derecha": ultimate_atacado_derecha,
    "atacado_izquierda": ultimate_atacado_izquierda
}
