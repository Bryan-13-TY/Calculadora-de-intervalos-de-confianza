import re

def validar_tamano_muestra(tamano_muestra: int) -> bool:
    if not tamano_muestra >= 1:
        return False
    
    return True


def validar_formato_muestra(muestra: str) -> bool | None:
    formato = r'^\d+(\.\d+)?( \d+(\.\d+)?)*$'
    return re.fullmatch(formato, muestra.strip()) is not None


def validar_numero_observaciones(muestra: str, tamano_muestra: int) -> bool:
    observaciones = muestra.strip().split()
    if not len(observaciones) == tamano_muestra:
        return False
    
    return True


def validar_porcentaje_confianza(porcentaje_confianza: int) -> bool:
    if not 0 < porcentaje_confianza <= 100:
        return False
    
    return True


def validar_desviacion_estandar_poblacional(desv_estandar_poblacional: float) -> bool:
    if not desv_estandar_poblacional >= 0:
        return False
    
    return True