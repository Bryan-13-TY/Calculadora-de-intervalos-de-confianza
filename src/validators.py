import re

def validar_tamano_muestra(tamano_muestra: int) -> bool:
    """
    Docstring for validar_tamano_muestra
    
    :param tamano_muestra: Description
    :type tamano_muestra: int
    :return: Description
    :rtype: bool
    """
    if not tamano_muestra >= 1:
        return False
    
    return True


def validar_formato_muestra(muestra: str) -> bool | None:
    """
    Docstring for validar_formato_muestra

    :param muestra: Description
    :type muestra: str
    :return: Description
    :rtype: bool | None
    """
    formato = r'^\d+(\.\d+)?( \d+(\.\d+)?)*$'

    return re.fullmatch(formato, muestra.strip()) is not None


def validar_numero_observaciones(muestra: str, tamano_muestra: int) -> bool:
    """
    Docstring for validar_numero_observaciones
    
    :param muestra: Description
    :type muestra: str
    :param tamano_muestra: Description
    :type tamano_muestra: int
    :return: Description
    :rtype: bool
    """
    observaciones = muestra.strip().split(" ")
    if not len(observaciones) == tamano_muestra:
        return False
    
    return True


def validar_porcentaje_confianza(porcentaje_confianza: int) -> bool:
    """
    Docstring for validar_porcentaje_confianza
    
    :param porcentaje_confianza: Description
    :type porcentaje_confianza: int
    :return: Description
    :rtype: bool
    """
    if not 0 < porcentaje_confianza <= 100:
        return False
    
    return True


def validar_desviacion_estandar_poblacional(desviacion_estandar_poblacional: float) -> bool:
    """
    Docstring for validar_desviacion_estandar_poblacional
    
    :param desviacion_estandar_poblacional: Description
    :type desviacion_estandar_poblacional: float
    :return: Description
    :rtype: bool
    """
    if not desviacion_estandar_poblacional >= 0:
        return False
    
    return True