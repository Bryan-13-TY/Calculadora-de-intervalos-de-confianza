from src.utils import (
    BRIGHT_RED,
    BRIGHT_YELLOW,
    BRIGHT_GREEN,
    BRIGHT_BLUE,
    RESET,
)

from src.validaciones import (
    validar_tamano_muestra,
    validar_formato_muestra,
    validar_numero_observaciones,
    validar_porcentaje_confianza,
    validar_desviacion_estandar_poblacional,
    validar_numero_exitos,
    validar_condicion_normalidad_proporcion,
    validar_condicion_normalidad_dif_proporciones,
)

from src.advertencias import (
    ad_porcentaje_confianza,
)

from src.calculos import *
from src.graficas import *

def media_poblacional() -> None:
    """
    Estima una media poblacional.

    Considera las siguientes situaciones:
    - Distribución normal, muestra grande y varianza conocida
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
            (
                limite_superior,
                limite_inferior,
                media_muestral,
            ) = intervalo_caso_1(
                tamano_muestra,
                muestra,
                porcentaje_confianza,
                desv_estandar_poblacional
            )
            
            if tamano_muestra >= 30: # muestra grande
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
                    )
                )
            else: # muestra pequeña
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
                    )
                )
        case "no":
            # se muestra el caso correspondiente
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 2{RESET}")
            print("\n- Parámetro a estimar: μ")

            if tamano_muestra >= 30: # muestra grande
                print("- Situación: Distribución normal, muestra grande y varianza desconocida")
            else: # muestra pequeña
                print("- Situación: Distribución normal, muestra pequeña y varianza desconocida")

            print("- Estimador puntual: X̄")

            (
                limite_superior,
                limite_inferior,
                media_muestral,
                desv_estandar_muestral,
            ) = intervalo_caso_2(tamano_muestra, muestra, porcentaje_confianza)

            if tamano_muestra >= 30: # muestra grande
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
                    )
                )
            else: # muestra pequeña
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
                    )
                )
        case _:
            print(f"{BRIGHT_RED}>> ERROR{RESET} La opción no es válida")


def dif_medias_poblacionales() -> None:
    """
    Estima una diferencia de medias poblacionales.

    Considera las siguientes situaciones:
    - Para dos muestras independientes de poblaciones normales con varianzas conocidas.
    - Para dos muestras grandes (n > 30) independientes de poblaciones normales con varianzas diferentes y desconocidas.
    - Para dos muestras chicas independientes de poblaciones normales con varianzas diferentes y desconocidas.
    - Para dos muestras independientes de poblaciones normales con varianzas iguales y desconocidas.
    """
    try:
        tamano_muestra_1 = int(input("Escribe el tamaño de la muestra (n₁): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_tamano_muestra(tamano_muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    muestra_1 = input(f"\nEscribe las {tamano_muestra_1} observaciones (x₁ x₂ ... xₙ): ")
    if not validar_formato_muestra(muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El formato de las observaciones no es correcto")
        return
    
    if not validar_numero_observaciones(muestra_1, tamano_muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El número de observaciones no coincide con el tamaño de la muestra (n)")
        return
    
    try:
        tamano_muestra_2 = int(input("Escribe el tamaño de la muestra (n₂): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_tamano_muestra(tamano_muestra_2):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    muestra_2 = input(f"\nEscribe las {tamano_muestra_2} observaciones (x₁ x₂ ... xₙ): ")
    if not validar_formato_muestra(muestra_2):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El formato de las observaciones no es correcto")
        return
    
    if not validar_numero_observaciones(muestra_2, tamano_muestra_2):
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

    varianzas_poblacionales = input("\n¿Las varianzas poblacioneales (σ₁ y σ₂) son conocidas (si / no)?").strip().lower()
    match varianzas_poblacionales:
        case "si":
            try:
                desv_estandar_poblacional_1 = float(input("\nEscribe el valor de la desviación estándar poblacional (σ₁): "))
            except ValueError:
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar pobrlacional debe ser un número")
                return
            
            if not validar_desviacion_estandar_poblacional(desv_estandar_poblacional_1):
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar poblacional debe ser mayor o igual a cero")
                return
            
            try:
                desv_estandar_poblacional_2 = float(input("\nEscribe el valor de la desviación estándar poblacional (σ₂): "))
            except ValueError:
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar pobrlacional debe ser un número")
                return
            
            if not validar_desviacion_estandar_poblacional(desv_estandar_poblacional_2):
                print(f"{BRIGHT_RED}>> ERROR{RESET} La desviación estándar poblacional debe ser mayor o igual a cero")
                return
            
            # se muestra el caso correspondiente
            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 3{RESET}")
            print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
            print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de poblaciones normales con varianzas conocidas.{RESET}")
            print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

            print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

            graficar_intervalo_z_caso_3(
                dif_medias_muestrales,
                limite_superior,
                limite_inferior,
                porcentaje_confianza,
                (
                    f"Intervalo de confianza al {porcentaje_confianza}% para μ₁ - μ₂ "
                    "(dos muestras independientes de poblaciones normales con varianzas conocidas)"
                    f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}, "
                    f"n₂ = {tamano_muestra_2}, σ₁ = {desv_estandar_poblacional_1}, "
                    f"σ₂ = {desv_estandar_poblacional_2}"
                )
            )
        case "no":
            varianzas_poblacionales = input("\n¿Las varianzas poblacionales (σ₁ y σ₂) son diferentes (si / no / no se)? ").strip().lower()
            match varianzas_poblacionales:
                case "si":
                    if tamano_muestra_1 >= 30 and tamano_muestra_2 >= 30: # dos muestras grandes
                        print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 4{RESET}")
                        print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                        print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras grandes (n > 30) independientes de poblaciones normales con varianzas diferentes y desconocidas.{RESET}")
                        print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

                        print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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
                                f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}, "
                                f"n₂ = {tamano_muestra_2}"
                            )
                        )
                    if tamano_muestra_1 < 30 and tamano_muestra_2 < 30: # dos muestra pequeñas
                        print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 5{RESET}")
                        print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                        print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras chicas independientes de poblaciones normales con varianzas diferentes y desconocidas.{RESET}")
                        print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

                        print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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
                            )
                        )
                case "no":
                    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 6{RESET}")
                    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                    print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de poblaciones normales con varianzas iguales y desconocidas.{RESET}")
                    print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

                    print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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
                        )
                    )
                case "no se":
                    print(f"\n{BRIGHT_BLUE}Dado que no se conocen las varianzas poblacionales se requiere averiguar si éstas son estadísticamente diferentes o no. Para ello construimos el intervalo de confianza para el cociente de las varianzas poblacionales (σ₁² / σ₂²), si tal intervalo contiene al 1 se concluye que las varianzas aunque desconocidas se pueden considerar estadísticamente iguales.{RESET}")
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
                        print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 6{RESET}")
                        print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                        print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de poblaciones normales con varianzas iguales y desconocidas.{RESET}")
                        print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

                        print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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
                            )
                        )

                    if not varianzas_son_iguales:
                        print(f"\n{BRIGHT_BLUE}>> El intervalo resultante es [{limite_superior}, {limite_superior}] en donde el 1 si se encuentra, entonces las varianzas poblacionales se consideran estadísticamente diferentes{RESET}")

                        if tamano_muestra_1 >= 30 and tamano_muestra_2 >= 30:
                            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 4{RESET}")
                            print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                            print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras grandes (n > 30) independientes de poblaciones normales con varianzas diferentes y desconocidas.{RESET}")
                            print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

                            print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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
                                    f"\nX̄₁ - X̄₂ = {dif_medias_muestrales}, n₁ = {tamano_muestra_1}, "
                                    f"n₂ = {tamano_muestra_2}"
                                )
                            )
                        
                        if tamano_muestra_1 < 30 and tamano_muestra_2 < 30:
                            print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 5{RESET}")
                            print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: μ₁ - μ₂{RESET}")
                            print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras chicas independientes de poblaciones normales con varianzas diferentes y desconocidas.{RESET}")
                            print(f"{BRIGHT_YELLOW}- Estimador puntual: X̄₁ - X̄₂{RESET}")

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

                            print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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
                                )
                            )
                case _:
                    print(f"{BRIGHT_RED}>> ERROR{RESET} La opción no es válida")
        case _:
            print(f"{BRIGHT_RED}>> ERROR{RESET} La opción no es válida")


def proporcion() -> None:
    """
    Estima una proporción.

    Considera la siguiente situación:
    - Para una muestra grande con 𝑃 pequeña.
    """
    try:
        tamano_muestra = int(input("Escribe el tamaño de la muestra (n): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_tamano_muestra(tamano_muestra):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    try:
        numero_exitos = int(input("Escribe el número de exitos de la muestra (n): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_numero_exitos(tamano_muestra, numero_exitos):
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser mayor o igual a 1, o menor o igual a {tamano_muestra}")
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

    if not validar_condicion_normalidad_proporcion(
        tamano_muestra,
        numero_exitos,
    ):
        print(f"{BRIGHT_RED}\n>> ERROR{RESET} No se puede usar la aproximación normal para la diferencia de proporciones porque alguna de las muestras no cumple con las condiciones de normalidad: np >= 5 y n(1-p) >= 5. Usa un método exacto o corregido")
        return
    
    # se muestra el caso correspondiente
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 7{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: 𝑃{RESET}")
    print(f"{BRIGHT_YELLOW}- Situación: Para una muestra grande con 𝑃 pequeña.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑝{RESET}")

    (
        limite_superior,
        limite_inferior,
        proporcion_muestral,
        valor_critico_Z,
    ) = intervalo_caso_7(numero_exitos, tamano_muestra, porcentaje_confianza)

    print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")

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


def dif_proporciones() -> None:
    """
    Estima una diferencia de proporciones.

    Considera la siguiente situación:
    - Para dos muestras grandes e independientes de una distribución normal.
    """
    try:
        tamano_muestra_1 = int(input("Escribe el tamaño de la muestra (n₁): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_tamano_muestra(tamano_muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    try:
        numero_exitos_1 = int(input("Escribe el número de exitos de la muestra (n₁): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_numero_exitos(tamano_muestra_1, numero_exitos_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser mayor o igual a 1, o menor o igual a {tamano_muestra_1}")
        return
    
    try:
        tamano_muestra_2 = int(input("Escribe el tamaño de la muestra (n₂): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_tamano_muestra(tamano_muestra_2):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    try:
        numero_exitos_2 = int(input("Escribe el número de exitos de la muestra (n₂): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return
    
    if not validar_numero_exitos(tamano_muestra_2, numero_exitos_2):
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser mayor o igual a 1, o menor o igual a {tamano_muestra_1}")
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

    if not validar_condicion_normalidad_dif_proporciones(
        tamano_muestra_1,
        numero_exitos_1,
        tamano_muestra_2,
        numero_exitos_2
    ):
        print(f"{BRIGHT_RED}\n>> ERROR{RESET} No se puede usar la aproximación normal para la diferencia de proporciones porque alguna de las muestras no cumple con las condiciones de normalidad: np >= 5 y n(1-p) >= 5. Usa un método exacto o corregido")
        return
    
    # se muestra el caso correspondiente
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 8{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: 𝑃₁ - 𝑃₂{RESET}")
    print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras grandes e independientes de una distribución normal.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑝₁ - 𝑝₂{RESET}")
    
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

    print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")
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


def varianza_poblacional() -> None:
    """
    Estima una varianza poblacional.

    Considera la siguiente situación:
    - Para una muestra cualquiera.
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

    # se muestra el caso correspondiente
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 9{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: σ²{RESET}")
    print(f"{BRIGHT_YELLOW}- Situación: Para una muestra cualquiera.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑠²{RESET}")

    (
        limite_superior,
        limite_inferior,
        varianza_muestral,
        grados_libertad
    ) = intervalo_caso_9(tamano_muestra, muestra, porcentaje_confianza)
    print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}]{RESET}")
    graficar_intervalo_chi2_caso_9(
        varianza_muestral,
        limite_superior,
        limite_inferior,
        grados_libertad,
        porcentaje_confianza,
        (
            f"Intervalo de confianza al {porcentaje_confianza}% para σ²"
            f"(una muestra cualquiera)\nn = {tamano_muestra}, S² = {varianza_muestral}"
        )
    )


def coc_varianzas_poblacionales() -> None:
    """
    Estima un cociente de varianzas poblacionales.

    Considera la siguiente situación:
    - Para dos muestras independientes de poblaciones normales.
    """
    try:
        tamano_muestra_1 = int(input("Escribe el tamaño de la primera muestra (n₁): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return

    if not validar_tamano_muestra(tamano_muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    muestra_1 = input(f"\nEscribe las {tamano_muestra_1} observaciones (x₁ x₂ ... xₙ): ")
    if not validar_formato_muestra(muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El formato de las observaciones no es correcto")
        return
    
    if not validar_numero_observaciones(muestra_1, tamano_muestra_1):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El número de observaciones no coincide con el tamaño de la muestra (n)")
        return
    
    try:
        tamano_muestra_2 = int(input("Escribe el tamaño de la segunda muestra (n₂): "))
    except ValueError:
        print(f"{BRIGHT_RED}>> ERROR{RESET} Debe ser un número entero")
        return

    if not validar_tamano_muestra(tamano_muestra_2):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El tamaño de la muestra debe ser mayor o igual a 1")
        return
    
    muestra_2 = input(f"\nEscribe las {tamano_muestra_2} observaciones (x₁ x₂ ... xₙ): ")
    if not validar_formato_muestra(muestra_2):
        print(f"{BRIGHT_RED}>> ERROR{RESET} El formato de las observaciones no es correcto")
        return
    
    if not validar_numero_observaciones(muestra_2, tamano_muestra_2):
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

    # se muestra el caso correspondiente
    print(f"\n{BRIGHT_YELLOW}>> Los datos corresponden al caso 10{RESET}")
    print(f"\n{BRIGHT_YELLOW}- Parámetro a estimar: σ₁² / σ₂²{RESET}")
    print(f"{BRIGHT_YELLOW}- Situación: Para dos muestras independientes de poblaciones normales.{RESET}")
    print(f"{BRIGHT_YELLOW}- Estimador puntual: 𝑠₁² / 𝑠₂²{RESET}")
    
    (
        limite_superior,
        limite_inferior,
        varianzas_son_iguales,
        coc_varianzas_muestrales,
        grados_libertad_1,
        grados_libertad_2
    ) = intervalo_caso_10(
        tamano_muestra_1,
        tamano_muestra_2,
        muestra_1,
        muestra_2,
        porcentaje_confianza
    )
    
    if varianzas_son_iguales:
        print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}] y el 1 si se encuentra en este{RESET}")
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
            )  
        )
    if not varianzas_son_iguales:
        print(f"\n{BRIGHT_GREEN}>> El intervalo de confianza es [{limite_superior}, {limite_inferior}] y el 1 no se encuentra en este{RESET}")
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
            )   
        )