"""
En este módulo se definen los diferentes errores que se pueden mostrar
al usar la calculadora.
"""
from .utils import (
    BRIGHT_RED,
    RESET,
)

def mostrar_error(mensaje: str) -> None:
    print(f"{BRIGHT_RED}>> ERROR{RESET} {mensaje}")


def mostrar_error_especial(mesaje: str) -> None:
    print(f"{BRIGHT_RED}\n>> ERROR{RESET} {mesaje}")

ERR_TAMANO_MUESTRA = "El tamaño de la muestra debe ser mayor o igual a 1"

ERR_FORMATO_OBSERVACIONES = "El formato de las observaciones no es correcto"

ERR_NUMERO_OBSERVACIONES = "El número de observaciones no coincide con el tamaño de la muestra"

ERR_NUMERO_ENTERO = "Debe ser un número entero"

ERR_PORCENTAJE_CONFIANZA = "Debe ser un número entero mayor que cero y menor o igual a 100"

ERR_NUMERO = "Debe ser un número"

ERR_DESV_ESTANDAR_POBLACIONAL = "La desviación estándar poblacional debe ser mayor o igual a cero"

ERR_APROXIMACION_NORMAL = (
    "No se puede usar la aproximación normal para la diferencia de "
    "proporciones porque alguna de las muestras no cumple con las condiciones de normalidad: "
    "np >= 5 y n(1-p) >= 5. Usa un método exacto o corregido"
)

ERR_OPCION_NO_VALIDA = "La opción no es valida"
