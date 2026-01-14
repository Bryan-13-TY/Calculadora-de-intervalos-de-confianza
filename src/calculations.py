import re
import math
from scipy.stats import (
    norm, # para calcula la Z
    t, # para calcular la T
    f, # para calcular la F
    chi2, # para calcula la Chi2
)

def validar_formato_muestra(muestra: str) -> bool | None:
    """
    Docstring for validar_formato_muestra

    Formato de la 
    
    
    :param muestra: Description
    :type muestra: str
    :return: Description
    :rtype: bool | None
    """
    formato = r'^\d+(\.\d+)?( \d+(\.\d+)?)*$'

    return re.fullmatch(formato, muestra.strip()) is not None


def validar_numero_observaciones(muestra: str, tamano_muestra: str) -> bool:
    observaciones = muestra.strip().split(" ")

    if len(observaciones) != int(tamano_muestra):
        return False
    
    return True