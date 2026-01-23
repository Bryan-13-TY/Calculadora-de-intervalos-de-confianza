"""
En este módulo se definen las funciones para validar los valores
y formatos de los parámetros que pide la calculadora.
"""
import re

__all__ = [
    "validar_condicion_normalidad_dif_proporciones",
    "validar_condicion_normalidad_proporcion",
    "validar_desviacion_estandar_poblacional",
    "validar_formato_muestra",
    "validar_numero_exitos",
    "validar_numero_observaciones",
    "validar_porcentaje_confianza",
    "validar_tamano_muestra",
]

def _condicion_normalidad(tamano_muestra: int, proporcion: float) -> bool:
    return (
        tamano_muestra * proporcion >= 5
        and tamano_muestra * (1 - proporcion) >= 5
    )


def validar_condicion_normalidad_dif_proporciones(
        tamano_muestra_1: int,
        numero_exitos_1: int,
        tamano_muestra_2: int,
        numero_exitos_2: int,
    ) -> bool:
    proporcion_1 = numero_exitos_1 / tamano_muestra_1
    proporcion_2 = numero_exitos_2 / tamano_muestra_2

    return (
        _condicion_normalidad(tamano_muestra_1, proporcion_1)
        and _condicion_normalidad(tamano_muestra_2, proporcion_2)
    )


def validar_condicion_normalidad_proporcion(
        tamano_muestra: int,
        numero_exitos: int,
    ) -> bool:
    proporcion = numero_exitos / tamano_muestra

    return _condicion_normalidad(tamano_muestra, proporcion)


def validar_desviacion_estandar_poblacional(desv_estandar_poblacional: float) -> bool:
    return desv_estandar_poblacional >= 0


def validar_formato_muestra(muestra: str) -> bool:
    formato = r'^\d+(\.\d+)?( \d+(\.\d+)?)*$'
    return re.fullmatch(formato, muestra.strip()) is not None


def validar_numero_exitos(tamano_muestra: int, numero_exitos: int) -> bool:
    return 1 <= numero_exitos < tamano_muestra


def validar_numero_observaciones(muestra: str, tamano_muestra: int) -> bool:
    observaciones = muestra.strip().split()
    return len(observaciones) == tamano_muestra


def validar_porcentaje_confianza(porcentaje_confianza: int) -> bool:
    return 0 < porcentaje_confianza <= 100


def validar_tamano_muestra(tamano_muestra: int) -> bool:
    return tamano_muestra >= 1
