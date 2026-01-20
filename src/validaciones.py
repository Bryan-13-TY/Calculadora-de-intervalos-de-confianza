import re

def validar_tamano_muestra(tamano_muestra: int) -> bool:
    return tamano_muestra >= 1


def validar_formato_muestra(muestra: str) -> bool | None:
    formato = r'^\d+(\.\d+)?( \d+(\.\d+)?)*$'
    return re.fullmatch(formato, muestra.strip()) is not None


def validar_numero_observaciones(muestra: str, tamano_muestra: int) -> bool:
    observaciones = muestra.strip().split()
    return len(observaciones) == tamano_muestra


def validar_porcentaje_confianza(porcentaje_confianza: int) -> bool:
    return 0 < porcentaje_confianza <= 100


def validar_desviacion_estandar_poblacional(desv_estandar_poblacional: float) -> bool:
    return desv_estandar_poblacional >= 0


def validar_numero_exitos(tamano_muestra: int, numero_exitos: int) -> bool:
    return 1 <= numero_exitos < tamano_muestra


def validar_condicion_normalidad_proporcion(
        tamano_muestra: int,
        numero_exitos: int,
    ) -> bool:
    parte_1 = numero_exitos / tamano_muestra

    return (
        tamano_muestra * parte_1 >= 5
        and tamano_muestra * (1 - parte_1) >= 5
    )


def validar_condicion_normalidad_dif_proporciones(
        tamano_muestra_1: int,
        numero_exitos_1: int,
        tamano_muestra_2: int,
        numero_exitos_2: int,
    ) -> bool:
    parte_1 = numero_exitos_1 / tamano_muestra_1
    parte_2 = numero_exitos_2 / tamano_muestra_2

    return (
        tamano_muestra_1 * parte_1 >= 5
        and tamano_muestra_1 * (1 - parte_1) >= 5
        and tamano_muestra_2 * parte_2 >= 5
        and tamano_muestra_2 * (1 - parte_2) >= 5
    )