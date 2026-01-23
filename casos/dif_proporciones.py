"""
Módulo que se encarga de pedir los parámetros necesarios para calcular
un intervalo de confianza a partir de la estmación de una diferencia
de proporciones poblacionales.
"""
from src import (
    BRIGHT_GREEN,
    BRIGHT_RED,
    BRIGHT_BLUE,
    BRIGHT_YELLOW,
    RESET,
    ERR_NUMERO_ENTERO,
    ERR_TAMANO_MUESTRA,
    ERR_PORCENTAJE_CONFIANZA,
    ERR_APROXIMACION_NORMAL,
    mostrar_error,
    mostrar_error_especial,
)

from src.validaciones import (
    validar_tamano_muestra,
    validar_numero_exitos,
    validar_porcentaje_confianza,
    validar_condicion_normalidad_dif_proporciones,
)

from src.advertencias import (
    ad_porcentaje_confianza,
)

from src.services.calculos import (
    intervalo_caso_8,
)

from src.visualization.graficas import (
    graficar_intervalo_z_caso_8,
)

def intervalo_dif_proporciones() -> None:
    """
    Estima una diferencia de proporciones para dos muestras grandes
    e independientes de una distribución normal.
    """
    try:
        tamano_muestra_1 = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el tamaño de la muestra (n₁): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_tamano_muestra(tamano_muestra_1):
        mostrar_error(ERR_TAMANO_MUESTRA)
        return
    
    try:
        numero_exitos_1 = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el número de exitos de la muestra (n₁): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_numero_exitos(tamano_muestra_1, numero_exitos_1):
        print(
            f"{BRIGHT_RED}>> ERROR{RESET} "
            f"Debe ser mayor o igual a 1, o menor o igual a {tamano_muestra_1}"
        )
        return
    
    try:
        tamano_muestra_2 = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el tamaño de la muestra (n₂): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_tamano_muestra(tamano_muestra_2):
        mostrar_error(ERR_TAMANO_MUESTRA)
        return
    
    try:
        numero_exitos_2 = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el número de exitos de la muestra (n₂): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_numero_exitos(tamano_muestra_2, numero_exitos_2):
        print(
            f"{BRIGHT_RED}>> ERROR{RESET} "
            f"Debe ser mayor o igual a 1, o menor o igual a {tamano_muestra_2}"
        )
        return
    
    try:
        porcentaje_confianza = int(input(
            f"{BRIGHT_BLUE}\n>>>{RESET} "
            "Escribe el porcentaje (%) de confianza: "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_porcentaje_confianza(porcentaje_confianza):
        mostrar_error(ERR_PORCENTAJE_CONFIANZA)
        return
    
    ad_porcentaje_confianza(porcentaje_confianza)

    if not validar_condicion_normalidad_dif_proporciones(
        tamano_muestra_1,
        numero_exitos_1,
        tamano_muestra_2,
        numero_exitos_2,
    ):
        mostrar_error_especial(ERR_APROXIMACION_NORMAL)
        return
    
    # ================================
    # Octavo caso de estimación
    # ================================

    # Mostrar información descriptiva del caso seleccionado
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 8{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: 𝑃₁ - 𝑃₂{RESET}")
    print(
        f"{BRIGHT_YELLOW}- Situación: Para dos muestras grandes e independientes de una "
        f"distribución normal.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑝₁ - 𝑝₂{RESET}")
    
    # Calcular el intervalo de confianza y otro datos necesarios
    # para la gráfica
    (
        limite_superior,
        limite_inferior,
        dif_proporciones_muestrales,
        valor_critico_Z,
    ) = intervalo_caso_8(
        numero_exitos_1,
        numero_exitos_2,
        tamano_muestra_1,
        tamano_muestra_2,
        porcentaje_confianza,
    )

    print(
        f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
        f"[{limite_superior}, {limite_inferior}]{RESET}"
    )

    # Graficar el intervalo de confianza
    graficar_intervalo_z_caso_8(
        dif_proporciones_muestrales,
        limite_superior,
        limite_inferior,
        valor_critico_Z,
        porcentaje_confianza,
        (
            f"Intervalo de confianza al {porcentaje_confianza}% para P₁ - P₂"
            "(dos muestras grandes e independientes de una distribución normal)"
            f"\n X₁ = {numero_exitos_1}, N₁ = {tamano_muestra_1}, " 
            f"X₂ = {numero_exitos_2}, N₂ = {tamano_muestra_2}, "
            f"p₁ - p₂ = {dif_proporciones_muestrales}"
        ),
    )