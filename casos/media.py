"""
Módulo que se encarga de pedir los parámetros necesarios para calcular
un intervalo de confianza a partir de la estmación de una
media poblacional.
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
    ERR_DESV_ESTANDAR_POBLACIONAL,
    ERR_NUMERO,
    ERR_OPCION_NO_VALIDA,
    mostrar_error,
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

from src.services.calculos import (
    intervalo_caso_1,
    intervalo_caso_2,
)

from src.visualization.graficas import (
    graficar_intervalo_z_caso_1,
    graficar_intervalo_t_caso_2,
)

def intervalo_media_poblacional() -> None:
    """
    Estima una media poblacional, para:

    - Una distribución normal, muestra grande y varianza conocida
    - Una distribución normal, muestra grande y varianza desconocida
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

    varianza_poblacional = input(
        f"{BRIGHT_BLUE}\n>>>{RESET} "
        "¿La varianza poblacional (σ²) es conocida (si / no)? "
    ).strip().lower()
    match varianza_poblacional:
        case "si":
            try:
                desv_estandar_poblacional = float(input(
                    f"{BRIGHT_BLUE}\n>>>{RESET} "
                    "Escribe el valor de la desviación estándar poblacional (σ): "
                ))
            except ValueError:
                mostrar_error(ERR_NUMERO)
                return
            
            if not validar_desviacion_estandar_poblacional(desv_estandar_poblacional):
                mostrar_error(ERR_DESV_ESTANDAR_POBLACIONAL)
                return
            
            # ================================
            # Primer caso de estimación
            # ================================
            
            # Mostrar información descriptiva del caso seleccionado
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 1{RESET}")
            print("\n- Parámetro a estimar: μ")

            # Determinar si la muestra es grande o pequeña
            if tamano_muestra >= 30:
                print("- Situación: Distribución normal, muestra grande y varianza conocida")
            else:
                print("- Situación: Distribución normal, muestra pequeña y varianza conocida")
            
            print("- Estimador puntual: X̄")
            
            # Calcular el intervalo de confianza y otro datos
            # necesarios para la gráfica
            (
                limite_superior,
                limite_inferior,
                media_muestral,
            ) = intervalo_caso_1(
                tamano_muestra,
                muestra,
                porcentaje_confianza,
                desv_estandar_poblacional,
            )

            print(
                f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                f"[{limite_superior}, {limite_inferior}]{RESET}"
            )
            
            # Determinar si la muestra es grande o pequeña y mostrar la
            # gráfica correspindiente
            if tamano_muestra >= 30:
                graficar_intervalo_z_caso_1(
                    media_muestral,
                    limite_superior,
                    limite_inferior,
                    desv_estandar_poblacional,
                    tamano_muestra,
                    porcentaje_confianza,
                    (
                        f"Intervalo de confianza al {porcentaje_confianza}% para μ "
                        f"(muestra grande y varianza conocida)\n X̄ = {media_muestral}, "
                        f"n = {tamano_muestra}, σ = {desv_estandar_poblacional}"
                    ),
                )
            else:
                graficar_intervalo_z_caso_1(
                    media_muestral,
                    limite_superior,
                    limite_inferior,
                    desv_estandar_poblacional,
                    tamano_muestra,
                    porcentaje_confianza,
                    (
                        f"Intervalo de confianza al {porcentaje_confianza}% para μ "
                        f"(muestra pequeña y varianza conocida)\n X̄ = {media_muestral}, "
                        f"n = {tamano_muestra}, σ = {desv_estandar_poblacional}"
                    ),
                )
        case "no":
            # =================================
            # Segundo caso de estimación
            # =================================

            # Mostrar información descriptiva del caso seleccionado
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 2{RESET}")
            print("\n- Parámetro a estimar: μ")

            # Determinar si la muestra es grande o pequeña
            if tamano_muestra >= 30:
                print("- Situación: Distribución normal, muestra grande y varianza desconocida")
            else:
                print("- Situación: Distribución normal, muestra pequeña y varianza desconocida")

            print("- Estimador puntual: X̄")

            # Calcular el intervalo de confianza y otro datos
            # necesarios para la gráfica
            (
                limite_superior,
                limite_inferior,
                media_muestral,
                desv_estandar_muestral,
            ) = intervalo_caso_2(tamano_muestra, muestra, porcentaje_confianza)

            print(
                f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                f"[{limite_superior}, {limite_inferior}]{RESET}"
            )

            # Determinar si la muestra es grande o pequeña y mostrar la
            # gráfica correspindiente
            if tamano_muestra >= 30:
                graficar_intervalo_t_caso_2(
                    media_muestral,
                    limite_superior,
                    limite_inferior,
                    desv_estandar_muestral,
                    tamano_muestra,
                    porcentaje_confianza,
                    (
                        f"Intervalo de confianza al {porcentaje_confianza}% para μ "
                        f"(muestra grande y varianza desconocida)\nX̄ = {media_muestral}, "
                        f"n = {tamano_muestra}"
                    ),
                )
            else:
                graficar_intervalo_t_caso_2(
                    media_muestral,
                    limite_superior,
                    limite_inferior,
                    desv_estandar_muestral,
                    tamano_muestra,
                    porcentaje_confianza,
                    (
                        f"Intervalo de confianza al {porcentaje_confianza}% para μ "
                        f"(muestra pequeña y varianza desconocida)\nX̄ = {media_muestral}, "
                        f"n = {tamano_muestra}"
                    ),
                )
        case _:
            mostrar_error(ERR_OPCION_NO_VALIDA)
