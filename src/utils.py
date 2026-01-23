"""
En este módulo se definen las constantes para darle color al texto de
la calculadora así como algunas funciones genéricas.
"""
import os
import msvcrt

BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

def limpiar_consola() -> None:
    os.system('cls' if os .name == 'nt' else 'clear')


def esperar_enter() -> None:
    msvcrt.getch()
