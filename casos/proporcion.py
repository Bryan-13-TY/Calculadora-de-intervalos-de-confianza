"""
Módulo que se encarga de pedir los parámetros necesarios para calcular
un intervalo de confianza a partir de la estmación de una proporción
poblacional.
"""
from src import (
    BRIGHT_GREEN,
    BRIGHT_RED,
    BRIGHT_YELLOW,
    BRIGHT_BLUE,
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
    validar_condicion_normalidad_proporcion,
)

from src.advertencias import (
    ad_porcentaje_confianza,
)

from src.services.calculos import (
    intervalo_caso_7,
)

from src.visualization.graficas import (
    graficar_intervalo_z_caso_7,
)

def intervalo_proporcion() -> None:
    """
    Estima una proporción para una muestra grande con 𝑃 pequeña.
    """
    try:
        tamano_muestra = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el tamaño de la muestra (n): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_tamano_muestra(tamano_muestra):
        mostrar_error(ERR_TAMANO_MUESTRA)
        return
    
    try:
        numero_exitos = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el número de exitos de la muestra (n): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return
    
    if not validar_numero_exitos(tamano_muestra, numero_exitos):
        print(
            f"{BRIGHT_RED}>> ERROR{RESET} "
            f"Debe ser mayor o igual a 1, o menor o igual a {tamano_muestra}"
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

    if not validar_condicion_normalidad_proporcion(
        tamano_muestra,
        numero_exitos,
    ):
        mostrar_error_especial(ERR_APROXIMACION_NORMAL)
        return
    
    # =================================
    # Séptimo caso de estimación
    # =================================

    # Mostrar información descriptiva del caso seleccionado
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 7{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: 𝑃{RESET}")
    print(f"{BRIGHT_YELLOW}- Situación: Para una muestra grande con 𝑃 pequeña.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑝{RESET}")

    # Calcular el intervalo de confianza y otro datos necesarios
    # para la gráfica
    (
        limite_superior,
        limite_inferior,
        proporcion_muestral,
        valor_critico_Z,
    ) = intervalo_caso_7(numero_exitos, tamano_muestra, porcentaje_confianza)

    print(
        f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
        f"[{limite_superior}, {limite_inferior}]{RESET}"
    )

    # Graficar el intervalo de confianza
    graficar_intervalo_z_caso_7(
        proporcion_muestral,
        limite_superior,
        limite_inferior,
        valor_critico_Z,
        porcentaje_confianza,
        (
            f"Intervalo de confianza al {porcentaje_confianza}% para P "
            f"(muestra grande con P pequeña)\n X = {numero_exitos}, "
            f"N = {tamano_muestra}, p = {proporcion_muestral}"
        ),
    )
