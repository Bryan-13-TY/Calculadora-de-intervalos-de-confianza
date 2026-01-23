"""
Módulo que se encarga de pedir los parámetros necesarios para calcular
un intervalo de confianza a partir de la estmación de una varianza
poblacional.
"""
from src import (
    BRIGHT_GREEN,
    BRIGHT_BLUE,
    BRIGHT_YELLOW,
    RESET,
    ERR_NUMERO_ENTERO,
    ERR_TAMANO_MUESTRA,
    ERR_FORMATO_OBSERVACIONES,
    ERR_NUMERO_OBSERVACIONES,
    ERR_PORCENTAJE_CONFIANZA,
    mostrar_error,
)

from src.validaciones import (
    validar_tamano_muestra,
    validar_formato_muestra,
    validar_numero_observaciones,
    validar_porcentaje_confianza,
)

from src.advertencias import (
    ad_porcentaje_confianza,
)

from src.services.calculos import (
    intervalo_caso_9,
)

from src.visualization.graficas import (
    graficar_intervalo_chi2_caso_9,
)

def intervalo_varianza_poblacional() -> None:
    """
    Estima una varianza poblacional para una muestra cualquiera.
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
    
    muestra = input(
        f"{BRIGHT_BLUE}\n>>>{RESET} "
        f"Escribe las {tamano_muestra} observaciones (x₁ x₂ ... xₙ): "
    )
    if not validar_formato_muestra(muestra):
        mostrar_error(ERR_FORMATO_OBSERVACIONES)
        return
    
    if not validar_numero_observaciones(muestra, tamano_muestra):
        mostrar_error(ERR_NUMERO_OBSERVACIONES)
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

    # ================================
    # Noveno caso de estimación
    # ================================

    # Mostrar información descriptiva del caso seleccionado
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 9{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: σ²{RESET}")
    print(f"{BRIGHT_YELLOW}- Situación: Para una muestra cualquiera.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑠²{RESET}")

    # Calcular el intervalo de confianza y otro datos necesarios
    # para la gráfica
    (
        limite_superior,
        limite_inferior,
        varianza_muestral,
        grados_libertad
    ) = intervalo_caso_9(tamano_muestra, muestra, porcentaje_confianza)

    print(
        f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
        f"[{limite_superior}, {limite_inferior}]{RESET}"
    )

    # Graficar el intervalo de confianza
    graficar_intervalo_chi2_caso_9(
        varianza_muestral,
        limite_superior,
        limite_inferior,
        grados_libertad,
        porcentaje_confianza,
        (
            f"Intervalo de confianza al {porcentaje_confianza}% para σ²"
            f"(una muestra cualquiera)\nn = {tamano_muestra}, S² = {varianza_muestral}"
        ),
    )
