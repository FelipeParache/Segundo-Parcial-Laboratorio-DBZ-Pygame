# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=global-statement
DEBUG = False

def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG

def get_modo():
    return DEBUG
