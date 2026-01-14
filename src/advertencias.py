from src.utils import (
    BRIGHT_YELLOW,
    RESET,
)

def ad_porcentaje_confianza(porcentaje_confianza: int):
    """
    Docstring for ad_porcentaje_confianza
    
    :param porcentaje_confianza: Description
    :type porcentaje_confianza: int
    """
    if porcentaje_confianza < 90:
        print(f"{BRIGHT_YELLOW}>> ADVERTENCIA{RESET} Usar un nivel de confianza menor a 90% implica un mayor riesgo de que el intervalo no contenga el valor real. Se recomienda 90% o más")
    
    if porcentaje_confianza == 100:
        print(f"{BRIGHT_YELLOW}>> ADVERTENCIA{RESET} Un nivel de confianza del 100% genera un intervalo demasiado amplio y poco útil. Se recomienda usar 90%, 95% o 99%")