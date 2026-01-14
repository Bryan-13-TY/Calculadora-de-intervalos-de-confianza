from src.utils import (
    BRIGHT_RED,
    RESET,
)

from src.validators import (
    validar_tamano_muestra,
    validar_formato_muestra,
    validar_numero_observaciones,
    validar_porcentaje_confianza,
    validar_desviacion_estandar_poblacional,
)

from src.warnings import (
    ad_porcentaje_confianza,
)

def media_poblacional():
    """
    Docstring for media_poblacional

    Estima una media poblacional.

    Considera las siguientes situaciones:
    - Dsitribución normal, muestra grande y varianza conocida
    - Distribución normal, muestra grande y varianza desconocida
    """
    try:
        tamano_muestra = int(input("Escribe el tamaño de la muestra (n): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return

    if not validar_tamano_muestra(tamano_muestra):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    muestra = input(f"\nEscribe las {tamano_muestra} observaciones (x₁ x₂ ... xₙ): ")
    if not validar_formato_muestra(muestra):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El formato de las observaciones no es correcto")
        return
    
    if not validar_numero_observaciones(muestra, tamano_muestra):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El número de observaciones no coincide con el tamaño de la muestra (n)")
        return
    
    try:
        porcentaje_confianza = int(input("\nEscribe el porcentaje (%) de confianza: "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_porcentaje_confianza(porcentaje_confianza):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El porcentaje debe ser un número entero mayor que cero y menor o igual a 100")
        return
    
    ad_porcentaje_confianza(porcentaje_confianza)

    varianza_poblacional = input("\n¿La varianza poblacional (σ²) es conocida (si / no)? ").strip().lower()
    match varianza_poblacional:
        case "si":
            try:
                desviacion_estandar_poblacional = float(input("\nEscribe el valor de la desviación estándar poblacional (σ): "))
            except ValueError:
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar pobrlacional debe ser un número")
                return
            
            if not validar_desviacion_estandar_poblacional(desviacion_estandar_poblacional):
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar poblacional debe ser mayor o igual a cero")
                return
        case "no":
            ...
        case _:
            ...


def dif_medias_poblacionales():
    ...


def proporcion():
    ...


def dif_proporciones():
    ...


def varianza_poblacional():
    ...


def coc_varianzas_poblacionales():
    ...