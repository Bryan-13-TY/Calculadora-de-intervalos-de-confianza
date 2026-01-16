from src.utils import (
    BRIGHT_RED,
    BRIGHT_YELLOW,
    RESET,
)

from src.validaciones import (
    validar_tamano_muestra,
    validar_formato_muestra,
    validar_numero_observaciones,
    validar_porcentaje_confianza,
    validar_desviacion_estandar_poblacional,
)

from src.advertencias import (
    ad_porcentaje_confianza,
)

from src.calculos import *

def media_poblacional() -> None:
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
                desv_estandar_poblacional = float(input("\nEscribe el valor de la desviación estándar poblacional (σ): "))
            except ValueError:
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar pobrlacional debe ser un número")
                return
            
            if not validar_desviacion_estandar_poblacional(desv_estandar_poblacional):
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar poblacional debe ser mayor o igual a cero")
                return
            
            # se muestra el caso correspondiente
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 1{RESET}")
            print("\n- Parámetro a estimar: μ")

            if tamano_muestra >= 30: # muestra grande
                print("- Situación: Distribución normal, muestra grande y varianza conocida")
            else: # muestra pequeña
                print("- Situación: Distribución normal, muestra pequeña y varianza conocida")

            print("- Estimador puntual: X̄")
            media, limite_superior, limite_inferior = intervalo_caso_1(tamano_muestra, muestra, porcentaje_confianza, desv_estandar_poblacional)
            
            if tamano_muestra >= 30: # muestra grande
                ... # graficar ic para z c1
            else: # muestra pequeña
                ... # graficar ic para z c1
        case "no":
            # se muestra el caso correspondiente
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 2{RESET}")
            print("\n- Parámetro a estimar: μ")

            if tamano_muestra >= 30: # muestra grande
                print("- Situación: Distribución normal, muestra grande y varianza desconocida")
            else: # muestra pequeña
                print("- Situación: Distribución normal, muestra pequeña y varianza desconocida")

            print("- Estimador puntual: X̄")

            media, limite_superior, limite_inferior, S = intervalo_caso_2(tamano_muestra, muestra, porcentaje_confianza)

            if tamano_muestra >= 30: # muestra grande
                ... # graficar ic para t c2
            else: # muestra pequeña
                ... # graficar ic para t c2
        case _:
            ...


def dif_medias_poblacionales() -> None:
    """
    Docstring for dif_medias_poblacionales

    Estima una diferencia de medias poblacionales.

    Considera las siguientes situaciones:
    - Para dos muestras independientes de poblaciones normales con varianzas conocidas.
    - Para dos muestras grandes (n > 30) independientes de poblaciones normales con varianzas diferentes y desconocidas.
    - Para dos muestras chicas independientes de poblaciones normales con varianzas diferentes y desconocidas.
    - Para dos muestras independientes de poblaciones normales con varianzas iguales y desconocidas.
    """
    ...


def proporcion() -> None:
    """
    Docstring for proporcion

    Estima una proporción.

    Considera la siguiente situación:
    - Para una muestra grande con 𝑃 pequeña.
    """
    ...


def dif_proporciones() -> None:
    """
    Docstring for dif_proporciones

    Estima una diferencia de proporciones.

    Considera la siguiente situación:
    - Para dos muestras grandes e independientes de una distribución normal.
    """
    ...


def varianza_poblacional() -> None:
    """
    Docstring for varianza_poblacional

    Estima una varianza poblacional.

    Considera la siguiente situación:
    - Para una muestra cualquiera.
    """
    ...


def coc_varianzas_poblacionales() -> None:
    """
    Docstring for coc_varianzas_poblacionales

    Estima un cociente de varianzas poblacionales.

    Considera la siguiente situación:
    - Para dos muestras independientes de poblaciones normales.
    """
    ...