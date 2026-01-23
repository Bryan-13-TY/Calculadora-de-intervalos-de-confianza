"""
Módulo que se encarga de pedir los parámetros necesarios para calcular
un intervalo de confianza a partir de la estmación de una diferencia
de medias poblaciones.
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
    ERR_NUMERO,
    ERR_DESV_ESTANDAR_POBLACIONAL,
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
    intervalo_caso_3,
    intervalo_caso_4,
    intervalo_caso_5,
    intervalo_caso_6,
    intervalo_caso_10,
)

from src.visualization.graficas import (
    graficar_intervalo_z_caso_3,
    graficar_intervalo_z_caso_4,
    graficar_intervalo_t_caso_5,
    graficar_intervalo_t_caso_6,
)

def intervalo_dif_medias_poblacionales() -> None:
    """
    Estima una diferencia de medias poblacionales, para:

    - Dos muestras independientes de poblaciones normales con
    varianzas conocidas.
    - Dos muestras grandes (n > 30) independientes de poblaciones
    normales con varianzas diferentes y desconocidas.
    - Dos muestras chicas independientes de poblaciones normales
    con varianzas diferentes y desconocidas.
    - Dos muestras independientes de poblaciones normales con
    varianzas iguales y desconocidas.
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
            "Escribe el tamaño de la muestra (n₂): "
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

    varianzas_poblacionales = input(
        f"{BRIGHT_BLUE}\n>>>{RESET} "
        "¿Las varianzas poblacioneales (σ₁ y σ₂) son conocidas (si / no)?"
    ).strip().lower()
    match varianzas_poblacionales:
        case "si":
            try:
                desv_estandar_poblacional_1 = float(input(
                    f"{BRIGHT_BLUE}\n>>>{RESET} "
                    "Escribe el valor de la desviación estándar poblacional (σ₁): "
                ))
            except ValueError:
                mostrar_error(ERR_NUMERO)
                return
            
            if not validar_desviacion_estandar_poblacional(desv_estandar_poblacional_1):
                mostrar_error(ERR_DESV_ESTANDAR_POBLACIONAL)
                return
            
            try:
                desv_estandar_poblacional_2 = float(input(
                    f"{BRIGHT_BLUE}\n>>>{RESET} "
                    "Escribe el valor de la desviación estándar poblacional (σ₂): "
                ))
            except ValueError:
                mostrar_error(ERR_NUMERO)
                return
            
            if not validar_desviacion_estandar_poblacional(desv_estandar_poblacional_2):
                mostrar_error(ERR_DESV_ESTANDAR_POBLACIONAL)
                return
            
            # ================================
            # Tercer caso de estimación
            # ================================

            # Mostrar información descriptiva del caso seleccionado
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 3{RESET}")
            print("\n- Parámetro a estimar: μ₁ - μ₂")
            print(
                "- Situación: Para dos muestras independientes "
                "de poblaciones normales con varianzas conocidas.")
            print("- Estimador puntual: X̄₁ - X̄₂")

            # Calcular el intervalo de confianza y otro datos
            # necesarios para la gráfica
            (
                limite_superior,
                limite_inferior,
                dif_medias_muestrales,
            ) = intervalo_caso_3(
                tamano_muestra_1,
                tamano_muestra_2,
                desv_estandar_poblacional_1,
                desv_estandar_poblacional_2,
                muestra_1,
                muestra_2,
                porcentaje_confianza,
            )

            print(
                f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                f"[{limite_superior}, {limite_inferior}]{RESET}"
            )

            # Graficar el intervalo de confianza
            graficar_intervalo_z_caso_3(
                dif_medias_muestrales,
                limite_superior,
                limite_inferior,
                porcentaje_confianza,
                (
                    f"Intervalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂ "
                    "(dos muestras independientes de poblaciones normales con varianzas "
                    "conocidas)"
                    f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}, "
                    f"n₂ = {tamano_muestra_2}, σ₁ = {desv_estandar_poblacional_1}, "
                    f"σ₂ = {desv_estandar_poblacional_2}"
                )
            )
        case "no":
            varianzas_poblacionales = input(
                f"{BRIGHT_BLUE}\n>>>{RESET} "
                "¿Las varianzas poblacionales (σ₁ y σ₂) son diferentes (si / no / no se)? "
            ).strip().lower()
            match varianzas_poblacionales:
                case "si":
                    # Determinar si las muestras son grandes o chicas
                    if tamano_muestra_1 >= 30 and tamano_muestra_2 >= 30:
                        # ================================
                        # Cuarto caso de estimación
                        # ================================

                        # Mostrar información descriptiva del caso
                        # seleccionado
                        print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 4{RESET}")
                        print("\n- Parámetro a estimar: μ₁ - μ₂")
                        print(
                            "- Situación: Para dos muestras grandes (n > 30) independientes "
                            "de poblaciones normales con varianzas diferentes y desconocidas."
                        )
                        print("- Estimador puntual: X̄₁ - X̄₂")

                        # Calcular el intervalo de confianza y otros
                        # datos necesarios para la gráfica
                        (
                            limite_superior,
                            limite_inferior,
                            dif_medias_muestrales,
                            valor_critico_Z,
                        ) = intervalo_caso_4(
                            tamano_muestra_1,
                            tamano_muestra_2,
                            muestra_1,
                            muestra_2,
                            porcentaje_confianza,
                        )

                        print(
                            f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                            f"[{limite_superior}, {limite_inferior}]{RESET}"
                        )

                        # Graficar el intervalo de confianza
                        graficar_intervalo_z_caso_4(
                            dif_medias_muestrales,
                            limite_superior,
                            limite_inferior,
                            valor_critico_Z,
                            porcentaje_confianza,
                            (
                                f"Intervalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂"
                                "(dos muestras grandes (n > 30) independientes de poblaciones "
                                "normales con varianzas diferentes y desconocidas)"
                                f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}"
                                f", n₂ = {tamano_muestra_2}"
                            ),
                        )
                    # Determinar si las muestras son grandes o chicas
                    if tamano_muestra_1 < 30 and tamano_muestra_2 < 30:
                        # ================================
                        # Quinto caso de estimación
                        # ================================

                        # Mostrar información descriptiva del caso
                        # seleccionado
                        print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 5{RESET}")
                        print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                        print(
                            f"{BRIGHT_YELLOW}- Situación: Para dos muestras chicas "
                            "independientes de poblaciones normales con varianzas diferentes "
                            f"y desconocidas.{RESET}")
                        print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

                        # Calcular el intervalo de confianza y otros
                        # datos necesarios para la gráfica
                        (
                            limite_superior,
                            limite_inferior,
                            dif_medias_muestrales,
                            valor_critico_t,
                            grados_libertad_efectivos,
                        ) = intervalo_caso_5(
                            tamano_muestra_1,
                            tamano_muestra_2,
                            muestra_1,
                            muestra_2,
                            porcentaje_confianza,
                        )

                        print(
                            f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                            f"[{limite_superior}, {limite_inferior}]{RESET}"
                        )

                        # Graficar el intervalo de confianza
                        graficar_intervalo_t_caso_5(
                            dif_medias_muestrales,
                            limite_superior,
                            limite_inferior,
                            valor_critico_t,
                            grados_libertad_efectivos,
                            porcentaje_confianza,
                            (
                                f"Intrvalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂ "
                                "(dos muestras chicas independientes de poblaciones normales "
                                "con varianzas diferentes y desconocidas)"
                                f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}"
                                f", n₂ = {tamano_muestra_2}"
                            ),
                        )
                case "no":
                    # ===============================
                    # Sexto caso de estimación
                    # ===============================

                    # Mostrar información descriptiva del caso
                    # seleccionado
                    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 6{RESET}")
                    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                    print(
                        f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de "
                        f"poblaciones normales con varianzas iguales y desconocidas.{RESET}"
                    )
                    print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

                    # Calcular el intervalo de confianza y otros datos
                    # necesarios para la gráfica
                    (
                        limite_superior,
                        limite_inferior,
                        dif_medias_muestrales,
                        valor_critico_t,
                        grados_libertad,
                    ) = intervalo_caso_6(
                        tamano_muestra_1,
                        tamano_muestra_2,
                        muestra_1,
                        muestra_2,
                        porcentaje_confianza,
                    )

                    print(
                        f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                        f"[{limite_superior}, {limite_inferior}]{RESET}"
                    )

                    # Graficar el intervalo de confianza
                    graficar_intervalo_t_caso_6(
                        dif_medias_muestrales,
                        limite_superior,
                        limite_inferior,
                        valor_critico_t,
                        grados_libertad,
                        porcentaje_confianza,
                        (
                            f"Intervalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂ "
                            "(dos muestras independientes de poblaciones normales con varianzas "
                            f"iguales y desconocidas)\nX̄₁ - X̄₂ = {dif_medias_muestrales}, "
                            f"n₁ = {tamano_muestra_1}, n₂ = {tamano_muestra_2}"
                        ),
                    )
                case "no se":
                    print(
                        f"\n{BRIGHT_BLUE}>>> Dado que no se conocen las varianzas poblacionales se "
                        "requiere averiguar si éstas son estadísticamente diferentes o no. "
                        "Para ello construimos el intervalo de confianza para el cociente de"
                        " las varianzas poblacionales (σ₁² / σ₂²), si tal intervalo contiene "
                        "al 1 se concluye que las varianzas aunque desconocidas se pueden "
                        f"considerar estadísticamente iguales.{RESET}"
                    )

                    # Calcular el intervalo de confianza y otros datos
                    # necesarios para la gráfica
                    (
                        limite_superior,
                        limite_inferior,
                        varianzas_son_iguales,
                        *_,
                    ) = intervalo_caso_10(
                        tamano_muestra_1,
                        tamano_muestra_2,
                        muestra_1,
                        muestra_2,
                        porcentaje_confianza,
                    )

                    if varianzas_son_iguales:
                        # ===============================
                        # Sexto caso de estimación
                        # ===============================

                        # Mostrar información descriptiva del caso
                        # seleccionado
                        print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 6{RESET}")
                        print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                        print(
                            f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de "
                            f"poblaciones normales con varianzas iguales y desconocidas.{RESET}"
                        )
                        print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

                        # Calcular el intervalo de confianza y otros
                        # datos necesarios para la gráfica
                        (
                            limite_superior,
                            limite_inferior,
                            dif_medias_muestrales,
                            valor_critico_t,
                            grados_libertad,
                        ) = intervalo_caso_6(
                            tamano_muestra_1,
                            tamano_muestra_2,
                            muestra_1,
                            muestra_2,
                            porcentaje_confianza,
                        )

                        print(
                            f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                            f"[{limite_superior}, {limite_inferior}]{RESET}"
                        )

                        # Graficar el intervalo de confianza
                        graficar_intervalo_t_caso_6(
                            dif_medias_muestrales,
                            limite_superior,
                            limite_inferior,
                            valor_critico_t,
                            grados_libertad,
                            porcentaje_confianza,
                            (
                                f"Intervalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂ "
                                "(dos muestras independientes de poblaciones normales con "
                                f"varianzas iguales y desconocidas)\nX̄₁ - X̄₂ = "
                                f"{dif_medias_muestrales}, n₁ = {tamano_muestra_1}, "
                                f"n₂ = {tamano_muestra_2}"
                            ),
                        )

                    if not varianzas_son_iguales:
                        print(
                            f"\n{BRIGHT_BLUE}>> El intervalo resultante es "
                            f"[{limite_superior}, {limite_superior}] en donde el 1 si se "
                            "encuentra, entonces las varianzas poblacionales se consideran "
                            f"estadísticamente diferentes{RESET}"
                        )

                        # Determinar si las muestras son grandes o 
                        # chicas
                        if tamano_muestra_1 >= 30 and tamano_muestra_2 >= 30:
                            # ===============================
                            # Sexto caso de estimación
                            # ===============================

                            # Mostrar información descriptiva del caso
                            # seleccionado
                            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 4{RESET}")
                            print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                            print(
                                f"{BRIGHT_YELLOW}- Situación: Para dos muestras grandes (n > 30) "
                                "independientes de poblaciones normales con varianzas diferentes "
                                f"y desconocidas.{RESET}"
                            )
                            print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

                            # Calcular el intervalo de confianza y 
                            # otro datos necesarios para la gráfica
                            (
                                limite_superior,
                                limite_inferior,
                                dif_medias_muestrales,
                                valor_critico_Z,
                            ) = intervalo_caso_4(
                                tamano_muestra_1,
                                tamano_muestra_2,
                                muestra_1,
                                muestra_2,
                                porcentaje_confianza,
                            )

                            print(
                                f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                                f"[{limite_superior}, {limite_inferior}]{RESET}"
                            )

                            # Graficar el intervalo de confianza
                            graficar_intervalo_z_caso_4(
                                dif_medias_muestrales,
                                limite_superior,
                                limite_inferior,
                                valor_critico_Z,
                                porcentaje_confianza,
                                (
                                    f"Intervalo de confianza al {porcentaje_confianza}% para "
                                    "μ₁ - μ₂ (dos muestras grandes (n > 30) independientes de "
                                    "poblaciones normales con varianzas diferentes y desconocidas)"
                                    f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, "
                                    f"n₁ = {tamano_muestra_1}, n₂ = {tamano_muestra_2}"
                                ),
                            )
                        
                        # Determinar si las muestras son grandes o 
                        # chicas
                        if tamano_muestra_1 < 30 and tamano_muestra_2 < 30:
                            # ================================
                            # Quinto caso de estimación
                            # ================================

                            # Mostrar información descriptiva del caso
                            # seleccionado
                            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 5{RESET}")
                            print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                            print(
                                f"{BRIGHT_YELLOW}- Situación: Para dos muestras chicas "
                                "independientes de poblaciones normales con varianzas diferentes "
                                f"y desconocidas.{RESET}"
                            )
                            print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

                            # Calcular el intervalo de confianza y 
                            # otro datos necesarios para la gráfica
                            (
                                limite_superior,
                                limite_inferior,
                                dif_medias_muestrales,
                                valor_critico_t,
                                grados_libertad_efectivos,
                            ) = intervalo_caso_5(
                                tamano_muestra_1,
                                tamano_muestra_2,
                                muestra_1,
                                muestra_2,
                                porcentaje_confianza,
                            )

                            print(
                                f"\n{BRIGHT_GREEN}>> El intervalo de confianza es "
                                f"[{limite_superior}, {limite_inferior}]{RESET}"
                            )

                            # Graficar el intervalo de confianza
                            graficar_intervalo_t_caso_5(
                                dif_medias_muestrales,
                                limite_superior,
                                limite_inferior,
                                valor_critico_t,
                                grados_libertad_efectivos,
                                porcentaje_confianza,
                                (
                                    f"Intrvalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂ "
                                    "(dos muestras chicas independientes de poblaciones normales "
                                    "con varianzas diferentes y desconocidas)"
                                    f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}, "
                                    f"n₂ = {tamano_muestra_2}"
                                ),
                            )
                case _:
                    mostrar_error(ERR_OPCION_NO_VALIDA)
        case _:
            mostrar_error(ERR_OPCION_NO_VALIDA)