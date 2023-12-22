# pylint: disable=invalid-name
# pylint: disable=broad-exception-caught
# pylint: disable=import-error
'''base de datos config'''
import sqlite3
from herramientas.config_excepcion import escribir_excepcion

def crear_base() -> None:
    '''crea la base de datos'''
    create = '''
                    create table Jugadores
                    (
                        id integer primary key autoincrement,
                        usuario text UNIQUE,
                        puntos integer,
                        nivel_max integer
                    )
                '''

    with sqlite3.connect("dbz_pygame/jugadores.bdd") as conexion:
        try:
            conexion.execute(create)
        except Exception as e:
            print("Error", e)
            escribir_excepcion("excepciones_bdd.txt", str(e))

def insertar_jugador(nivel, puntos, usuario, nombre_bdd) -> None:
    '''inserta un jugador'''
    insert = ''' insert into Jugadores (usuario, puntos, nivel_max) values (?, ?, ?) '''

    with sqlite3.connect(nombre_bdd) as conexion:
        try:
            conexion.execute(insert, (usuario, puntos, nivel))
            return True
        except Exception as e:
            print("Error", e)
            escribir_excepcion("excepciones_bdd.txt", str(e))
            return False

def actualizar_jugador(nivel, puntos, usuario, nombre_bdd) -> None:
    '''actualiza el jugador'''
    update = "update Jugadores set nivel_max = ?, puntos = ? where usuario = ?"

    with sqlite3.connect(nombre_bdd) as conexion:
        try:
            conexion.execute(update, (nivel, puntos, usuario))
            return True
        except Exception as e:
            print("Error", e)
            escribir_excepcion("excepciones_bdd.txt", str(e))
            return False

def buscar_usuario_bdd(nombre_bdd, usuario) -> list:
    '''busca un jugador'''
    select = "SELECT usuario, puntos, nivel_max from Jugadores WHERE usuario = ?"

    with sqlite3.connect(nombre_bdd) as conexion:
        try:
            usuario = conexion.execute(select, (usuario,)).fetchall()
            return usuario[0]
        except Exception as e:
            print("Error", e)
            escribir_excepcion("excepciones_bdd.txt", str(e))
            return False

def traer_ranking_bdd(nombre_bdd):
    '''trae el ranking de los jugadores'''
    select = "SELECT usuario, puntos from Jugadores ORDER BY puntos desc limit 5"

    with sqlite3.connect(nombre_bdd) as conexion:
        try:
            usuarios = conexion.execute(select).fetchall()
            return list(usuarios)
        except Exception as e:
            print("Error", e)
            escribir_excepcion("excepciones_bdd.txt", str(e))
            return False

def verificar_tabla_existente(nombre_tabla, nombre_bdd):
    '''Verifica si una tabla existe en la base de datos'''
    consulta = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nombre_tabla}'"

    with sqlite3.connect(nombre_bdd) as conexion:
        cursor = conexion.cursor()
        cursor.execute(consulta)
        tabla = cursor.fetchone()

        return tabla is not None
