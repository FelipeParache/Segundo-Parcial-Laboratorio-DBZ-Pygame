# pylint: disable=broad-exception-caught
'''
config excepcion
'''

import datetime

def escribir_excepcion(nombre_archivo:str, excepcion) -> None:
    '''escribe una excepcion en un archivo'''
    try:
        hora_actual = datetime.datetime.now()
        archivo = open(f"dbz_pygame/{nombre_archivo}", "a", encoding="utf-8")
        archivo.write(f"{hora_actual}: {excepcion}\n")
        archivo.close()
    except Exception as e:
        print("Excepcion:", e)
