"""
Módulo que se encarga de pedir los parámetros necesarios para calcular
un intervalo de confianza a partir de la estmación del cociente de
varianzas poblacionales.
"""
from src import (
    BRIGHT_GREEN,
    BRIGHT_YELLOW,
    BRIGHT_BLUE,
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
    intervalo_caso_10,
)

from src.visualization.graficas import (
    graficar_intervalo_f_caso_10,
)

def intervalo_coc_varianzas_poblacionales() -> None:
    """
    Estima un cociente de varianzas poblacionales para dos muestras
    independientes de poblaciones normales.
    """
    try:
        tamano_muestra_1 = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el tamaño de la primera muestra (n₁): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return

    if not validar_tamano_muestra(tamano_muestra_1):
        mostrar_error(ERR_TAMANO_MUESTRA)
        return
    
    muestra_1 = input(
        f"{BRIGHT_BLUE}\n>>>{RESET} "
        f"Escribe las {tamano_muestra_1} observaciones (x₁ x₂ ... xₙ): "
    )
    if not validar_formato_muestra(muestra_1):
        mostrar_error(ERR_FORMATO_OBSERVACIONES)
        return
    
    if not validar_numero_observaciones(muestra_1, tamano_muestra_1):
        mostrar_error(ERR_NUMERO_OBSERVACIONES)
        return
    
    try:
        tamano_muestra_2 = int(input(
            f"{BRIGHT_BLUE}>>>{RESET} "
            "Escribe el tamaño de la segunda muestra (n₂): "
        ))
    except ValueError:
        mostrar_error(ERR_NUMERO_ENTERO)
        return

    if not validar_tamano_muestra(tamano_muestra_2):
        mostrar_error(ERR_TAMANO_MUESTRA)
        return
    
    muestra_2 = input(
        f"{BRIGHT_BLUE}\n>>>{RESET} "
        f"Escribe las {tamano_muestra_2} observaciones (x₁ x₂ ... xₙ): "
    )
    if not validar_formato_muestra(muestra_2):
        mostrar_error(ERR_FORMATO_OBSERVACIONES)
        return
    
    if not validar_numero_observaciones(muestra_2, tamano_muestra_2):
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
    # Décimo caso de estimación
    # ================================

    # Mostrar información descriptiva del caso seleccionado
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 10{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: σ₁² / σ₂²{RESET}")
    print(
        f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de poblaciones "
        f"normales.{RESET}"
    )
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑠₁² / 𝑠₂²{RESET}")
    
    # Calcular el intervalo de confianza y otro datos necesarios
    # para la gráfica
    (
        limite_superior,
        limite_inferior,
        varianzas_son_iguales,
        coc_varianzas_muestrales,
        grados_libertad_1,
        grados_libertad_2,
    ) = intervalo_caso_10(
        tamano_muestra_1,
        tamano_muestra_2,
        muestra_1,
        muestra_2,
        porcentaje_confianza,
    )
    
    if varianzas_son_iguales:
        print(
            f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
            f"[{limite_superior}, {limite_inferior}] y el 1 si se encuentra en este{RESET}"
        )

        # Graficar el intervalo de confianza
        graficar_intervalo_f_caso_10(
            coc_varianzas_muestrales,
            limite_superior,
            limite_inferior,
            grados_libertad_1,
            grados_libertad_2,
            porcentaje_confianza,
            (
                f"Intervalo de confianza al {porcentaje_confianza} para σ₁² / σ₂²" 
                "(dos muestras independientes de poblaciones normales)"
                f"\n n₁ = {tamano_muestra_1}, n₂ = {tamano_muestra_2}, "
                f"S₁² / S₂² = {coc_varianzas_muestrales}"
            ),
        )
    if not varianzas_son_iguales:
        print(
            f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
            f"[{limite_superior}, {limite_inferior}] y el 1 no se encuentra en este{RESET}"
        )

        # Graficar el intervalo de confianza
        graficar_intervalo_f_caso_10(
            coc_varianzas_muestrales,
            limite_superior,
            limite_inferior,
            grados_libertad_1,
            grados_libertad_2,
            porcentaje_confianza,
            (
                f"Intervalo de confianza al {porcentaje_confianza} para σ₁² / σ₂²" 
                "(dos muestras independientes de poblaciones normales)"
                f"\n n₁ = {tamano_muestra_1}, n₂ = {tamano_muestra_2}, "
                f"S₁² / S₂² = {coc_varianzas_muestrales}"
            ),
        )
