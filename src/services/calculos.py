"""
En este módulo se definen las funciones necesarias para calcular
al intervalo de confianza dependiendo del parámetro que se desea
estimar.
"""
import math

from scipy.stats import (
    norm,
    t,
    f,
    chi2,  
)

__all__ = [
    "intervalo_caso_1",
    "intervalo_caso_2",
    "intervalo_caso_3",
    "intervalo_caso_4",
    "intervalo_caso_5",
    "intervalo_caso_6",
    "intervalo_caso_7",
    "intervalo_caso_8",
    "intervalo_caso_9",
    "intervalo_caso_10",
]

def _calcular_media(muestra: str) -> float:
    """
    Calcula la media muestral (X̄) de una muestra válida. 
    
    :param muestra: Una muestra válida.
    :type muestra: str
    :return: Media muestral (X̄) redondeada a cuatro decimales.
    :rtype: float
    """
    numeros = muestra.split()
    numeros_float = [float(numero) for numero in numeros]
    media = sum(numeros_float) / len(numeros_float)
    media_round = round(media, 4)
    return media_round


def _calcular_varianza_muestral(
        tamano_muestra: int,
        muestra: str,
        media_muestral: float,
    ) -> float:
    """
    Calcula la varianza muestral (𝑠²) de una muestra válida.
    
    :param tamano_muestra: Tamaño de la muestra (n).
    :type tamano_muestra: int
    :param muestra: Una muestra válida.
    :type muestra: str
    :param media_muestral: Media muestral (X̄).
    :type media_muestral: float
    :return: Varianza muestral (𝑠²) redondeada a cuatro decimales.
    :rtype: float
    """
    numeros = muestra.split()
    suma = 0
    for i in range(tamano_muestra):
        suma = round(suma + ((float(numeros[i]) - media_muestral) ** 2), 4)

    varianza_muestral = (1 / (tamano_muestra - 1)) * suma
    varianza_muestral_round = round(varianza_muestral, 4)
    return varianza_muestral_round


def _calcular_grados_libertad_efectivos(
        varianza_muestral_1: float,
        varianza_muestral_2: float,
        tamano_muestra_1: int,
        tamano_muestra_2: int,
    ) -> float:
    """
    Calcula los grados de libertad efectivos (ν).
    
    :param varianza_muestral_1: Varianza muestral (𝑠₁²) de una
    primera muestra.
    :type varianza_muestral_1: float
    :param varianza_muestral_2: Varianza muestral (𝑠₂²) de una
    segunda muestra.
    :type varianza_muestral_2: float
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :return: Grados de libertad efectivos (ν) redondeados a
    cuatro decimales.
    :rtype: float
    """
    numerador_suma_1 = varianza_muestral_1 / tamano_muestra_1
    numerador_suma_2 = varianza_muestral_2 / tamano_muestra_2
    numerador = (numerador_suma_1 + numerador_suma_2) ** 2
    denominador_cuadrado_1 = (varianza_muestral_1 / tamano_muestra_1) ** 2
    denominador_division_1 = denominador_cuadrado_1 / (tamano_muestra_1 + 1)
    denominador_cuadrado_2 = (varianza_muestral_2 / tamano_muestra_2) ** 2
    denominador_division_2 = denominador_cuadrado_2 / (tamano_muestra_2 + 1)
    denominador = denominador_division_1 + denominador_division_2
    
    grados_libertad_efectivos = (numerador / denominador) - 2
    grados_libertad_efectivos_round = round(grados_libertad_efectivos, 4)
    return grados_libertad_efectivos_round


def _calcular_desviacion_estandar_combinada(
        varianza_muestral_1: float,
        varianza_muestral_2: float,
        tamano_muestra_1: int,
        tamano_muestra_2: int,
    ) -> float:
    """
    Calcula la desviacíon estándar combinada (Sp).

    :param varianza_muestral_1: Varianza muestral (𝑠₁²) de una
    primera muestra.
    :type varianza_muestral_1: float
    :param varianza_muestral_2: Varianza muestral (𝑠₂²) de una
    segunda muestra.
    :type varianza_muestral_2: float
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :return: Desviación estándar combinada (Sp) redondeada a
    cuatro decimales. 
    :rtype: float
    """
    numerador_multi_1 = (tamano_muestra_1 - 1) * varianza_muestral_1
    numerador_multi_2 = (tamano_muestra_2 - 1) * varianza_muestral_2 
    numerador = numerador_multi_1 + numerador_multi_2
    denominador = tamano_muestra_1 + tamano_muestra_2 - 2

    desviacion_estandar_combinada = math.sqrt(numerador / denominador)
    desviacion_estandar_combinada_round = round(desviacion_estandar_combinada, 4)
    return desviacion_estandar_combinada_round


def _calcular_proporcion_muestral(numero_exitos: int, tamano_muestra: int) -> float:
    """
    Calcula la proporción muestral (𝑝) de una proporción poblacional.
    
    :param numero_exitos: Número de exitos (X) de una proporción
    problacional.
    :type numero_exitos: int
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :return: Proporción muestral (𝑝) redondeada a cuatro decimales.
    :rtype: float
    """
    proporcion_muestral = numero_exitos / tamano_muestra
    proporcion_muestral_round = round(proporcion_muestral, 4)
    return proporcion_muestral_round


def _calcular_valor_critico_normal_estandar(porcentaje_confianza: int) -> float:
    """
    Calcula el valor crítico de la distribución normal estándar (Z).
    
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Valor crítico redondeado a cuatro decimales.
    :rtype: float
    """
    alpha = 1 - (porcentaje_confianza / 100)
    valor_critico_Z = norm.ppf(1 - round(alpha / 2, 4))
    valor_critico_Z_round = round(valor_critico_Z, 4) # type: ignore
    return valor_critico_Z_round


def _calcular_valor_critico_t_student(
        porcentaje_confianza: int,
        grados_libertad: float,
        caso_intervalo: int,
    ) -> float:
    """
    Calcula el valor crítico de la distribución t (t de Student).
    
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param grados_libertad: Grados de libertad de la distribución.
    :type grados_libertad: float
    :param caso_intervalo: Caso donde se usa el valor crítico.
    :type caso_intervalo: int
    :return: Valor crítico redondeado a cuatro decimales.
    :rtype: float
    """
    alpha = 1 - (porcentaje_confianza / 100)

    if caso_intervalo == 2:
        grados_libertad_nuevos = grados_libertad - 1
    if caso_intervalo == 5:
        grados_libertad_nuevos = grados_libertad
    if caso_intervalo == 6:
        grados_libertad_nuevos = grados_libertad - 2
    
    valor_critico_t = t.ppf(1 - round(alpha / 2, 4), grados_libertad_nuevos)
    valor_critico_t_round = round(valor_critico_t, 4) # type: ignore 
    return valor_critico_t_round


def _calcular_valor_critico_f(
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        porcentaje_confianza: int,
    ) -> tuple[float, float]:
    """
    Calcula el valor crítico de la distribución de Fisher (F).
    
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Valor crítico superior e inferior de la distribución
    redondeados a cuatro decimales.
    :rtype: tuple[float, float]
    """
    alpha = 1 - (porcentaje_confianza / 100)
    grados_libertad_1 = tamano_muestra_1 - 1
    grados_libertad_2 = tamano_muestra_2 - 1
    f_superior = f.ppf(1 - (alpha / 2), grados_libertad_1, grados_libertad_2)
    f_inferior = f.ppf(alpha / 2, grados_libertad_1, grados_libertad_2)
    f_superior_round = round(f_superior, 4) # type: ignore
    f_inferior_round = round(f_inferior, 4) # type: ignore
    return f_superior_round, f_inferior_round


def _calcular_valor_critico_chi_cuadrada(
        tamano_muestra: int,
        porcentaje_confianza: int,
    ) -> tuple[float, float]:
    """
    Calcula el valor crítico de la distribución Chi-cuadrada (χ²).
    
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Valor crítico superior e inferior de la distribución
    redondeados a cuatro decimales.
    :rtype: tuple[float, float]
    """
    alpha = 1 - (porcentaje_confianza / 100)
    grados_libertad = tamano_muestra - 1
    chi2_superior = chi2.ppf(1 - (alpha / 2), grados_libertad)
    chi2_inferior = chi2.ppf(alpha / 2, grados_libertad)
    chi2_superior_round = round(chi2_superior, 4) # type: ignore
    chi2_inferior_round = round(chi2_inferior, 4) # type: ignore
    return chi2_superior_round, chi2_inferior_round


def intervalo_caso_1(
        tamano_muestra: int,
        muestra: str,
        porcentaje_confianza: int,
        desv_estandar_poblacional: float,
    ) -> tuple[float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Una media poblacional (μ).
    - Situación: Distribución normal, muestra grande
    y varianza conocida.
    - Estimador puntual: Una media muestral (X̄).
    
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param muestra: Una muestra válida.
    :type muestra: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param desv_estandar_poblacional: Desviación estándar
    poblacional (σ).
    :type desv_estandar_poblacional: float
    :return: Límite superior e inferior del intervalo y la media
    muestral (X̄).
    :rtype: tuple[float, float, float]
    """
    # datos necesarios
    media_muestral = _calcular_media(muestra)
    valor_critico_Z = _calcular_valor_critico_normal_estandar(porcentaje_confianza)
    
    # intervalos
    multiplicacion = valor_critico_Z * (desv_estandar_poblacional / math.sqrt(tamano_muestra))
    intervalo_l = media_muestral - multiplicacion
    intervalo_u = media_muestral + multiplicacion
    return intervalo_l, intervalo_u, media_muestral


def intervalo_caso_2(
        tamano_muestra: int,
        muestra: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Una media poblacional (μ).
    - Situación: Distribución normal, muestra grande
    y varianza desconocida.
    - Estimador puntual: Una media muestral (X̄).
    
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param muestra: Una muestra válida.
    :type muestra: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, media
    muestral (X̄) y la desviación estándar muestral (𝑠).
    :rtype: tuple[float, float, float, float]
    """
    # datos necesarios
    media_muestral = _calcular_media(muestra)
    valor_critico_t = _calcular_valor_critico_t_student(porcentaje_confianza, tamano_muestra, 2)
    desv_estandar_muestral = math.sqrt(_calcular_varianza_muestral(
        tamano_muestra,
        muestra,
        media_muestral,
    ))
    
    # intervalos
    multiplicacion = valor_critico_t * (desv_estandar_muestral / math.sqrt(tamano_muestra))
    intervalo_l = media_muestral - multiplicacion
    intervalo_u = media_muestral + multiplicacion
    return intervalo_l, intervalo_u, media_muestral, desv_estandar_muestral


def intervalo_caso_3(
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        desv_estandar_poblacional_1: float,
        desv_estandar_poblacional_2: float,
        muestra_1: str,
        muestra_2: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras independientes de poblaciones
    normales con varianzas
    conocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param desv_estandar_poblacional_1: Desviación estándar poblacional
    de una primera muestra (σ₁).
    :type desv_estandar_poblacional_1: float
    :param desv_estandar_poblacional_2: Desviación estándar poblacional
    de una segunda muestra (σ₂).
    :type desv_estandar_poblacional_2: float
    :param muestra_1: Una primera muestra válida.
    :type muestra_1: str
    :param muestra_2: Una segunda muestra válida.
    :type muestra_2: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo y la
    diferencia de medias
    mustrales (X̄₁ - X̄₂).
    :rtype: tuple[float, float, float]
    """
    # datos necesarios
    media_muestral_1 = _calcular_media(muestra_1)
    media_muestral_2 = _calcular_media(muestra_2)
    valor_critico_Z = _calcular_valor_critico_normal_estandar(porcentaje_confianza)
    division_1 = (desv_estandar_poblacional_1 ** 2) / tamano_muestra_1
    division_2 = (desv_estandar_poblacional_2 ** 2) / tamano_muestra_2
    raiz = math.sqrt(division_1 + division_2)

    # intervalos
    intervalo_l = (media_muestral_1 - media_muestral_2) - (valor_critico_Z * raiz)
    intervalo_u = (media_muestral_1 - media_muestral_2) + (valor_critico_Z * raiz)
    return intervalo_l, intervalo_u, media_muestral_1 - media_muestral_2


def intervalo_caso_4(
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        muestra_1: str,
        muestra_2: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras grandes (n > 30) independientes
    de poblaciones normales con
    varianzas diferentes y desconocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param muestra_1: Una primera muestra válida.
    :type muestra_1: str
    :param muestra_2: Una segunda muestra válida.
    :type muestra_2: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, diferencia de
    medias muestrales (X̄₁ - X̄₂), y el valor crítico de la
    distribución normal estándar (Z).
    :rtype: tuple[float, float, float, float]
    """
    # datos necesarios
    media_muestral_1 = _calcular_media(muestra_1)
    media_muestral_2 = _calcular_media(muestra_2)
    valor_critico_Z = _calcular_valor_critico_normal_estandar(porcentaje_confianza)
    varianza_muestral_1 = _calcular_varianza_muestral(
        tamano_muestra_1,
        muestra_1,
        media_muestral_1,
    )
    varianza_muestral_2 = _calcular_varianza_muestral(
        tamano_muestra_1,
        muestra_2,
        media_muestral_2,
    )

    # intervalos
    raiz = math.sqrt(
        (varianza_muestral_1 / tamano_muestra_1) + (varianza_muestral_2 / tamano_muestra_2)
    )
    intervalo_l = (media_muestral_1 - media_muestral_2) - (valor_critico_Z * raiz)
    intervalo_u = (media_muestral_1 - media_muestral_2) + (valor_critico_Z * raiz)
    return (
        intervalo_l,
        intervalo_u,
        round(media_muestral_1 - media_muestral_2, 2),
        valor_critico_Z,
    )


def intervalo_caso_5(
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        muestra_1: str,
        muestra_2: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras chicas independientes de
    poblaciones normales con
    varianzas diferentes y desconocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param muestra_1: Una primera muestra válida.
    :type muestra_1: str
    :param muestra_2: Una segunda muestra válida.
    :type muestra_2: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, diferencia de
    medias mustrales (X̄₁ - X̄₂), valor crítico de la distribución t y
    los grados de libertad efectivos (ν).
    :rtype: tuple[float, float, float, float, float]
    """
    # datos necesarios
    media_muestral_1 = _calcular_media(muestra_1)
    media_muestral_2 = _calcular_media(muestra_2)
    varianza_muestral_1 = _calcular_varianza_muestral(
        tamano_muestra_1,
        muestra_1,
        media_muestral_1,
    )
    varianza_muestral_2 = _calcular_varianza_muestral(
        tamano_muestra_2,
        muestra_2,
        media_muestral_2,
    )
    grados_libertad_efectivos = _calcular_grados_libertad_efectivos(
        varianza_muestral_1,
        varianza_muestral_2,
        tamano_muestra_1,
        tamano_muestra_2,
    )
    valor_critico_t = _calcular_valor_critico_t_student(
        porcentaje_confianza,
        grados_libertad_efectivos,
        5,
    )
    
    # intervalos 
    raiz = math.sqrt(
        (varianza_muestral_1 / tamano_muestra_1) + (varianza_muestral_2 / tamano_muestra_2)
    )
    intervalo_l = (media_muestral_1 - media_muestral_2) - (valor_critico_t * raiz)
    intervalo_u = (media_muestral_1 - media_muestral_2) + (valor_critico_t * raiz)
    return (
        intervalo_l,
        intervalo_u,
        media_muestral_1 - media_muestral_2,
        valor_critico_t,
        grados_libertad_efectivos,
    )


def intervalo_caso_6(
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        muestra_1: str,
        muestra_2: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras independientes de poblaciones
    normales con varianzas
    iguales y desconocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param muestra_1: Una primera muestra válida.
    :type muestra_1: str
    :param muestra_2: Una segunda muestra válida.
    :type muestra_2: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, diferencia de
    medias muestrales (X̄₁ - X̄₂), valor crítico de la distribución t y
    los grados de libertad para la distribución.
    :rtype: tuple[float, float, float, float, float]
    """
    # datos necesarios
    media_muestral_1 = _calcular_media(muestra_1)
    media_muestral_2 = _calcular_media(muestra_2)
    varianza_muestral_1 = _calcular_varianza_muestral(
        tamano_muestra_1,
        muestra_1,
        media_muestral_1,
    )
    varianza_muestral_2 = _calcular_varianza_muestral(
        tamano_muestra_2,
        muestra_2,
        media_muestral_2,
    )
    desv_estandar_combinada = _calcular_desviacion_estandar_combinada(
        varianza_muestral_1,
        varianza_muestral_2,
        tamano_muestra_1,
        tamano_muestra_2,
    )
    valor_critico_t = _calcular_valor_critico_t_student(
        porcentaje_confianza,
        float(tamano_muestra_1 + tamano_muestra_2),
        6,
    )

    # intervalos
    raiz = math.sqrt((1 / tamano_muestra_1) + (1 / tamano_muestra_2))
    parte_1 = media_muestral_1 - media_muestral_2
    parte_2 = valor_critico_t * desv_estandar_combinada * raiz
    intervalo_l = parte_1 - parte_2
    intervalo_u = parte_1 + parte_2
    return (
        intervalo_l,
        intervalo_u,
        media_muestral_1 - media_muestral_2,
        valor_critico_t,
        round(tamano_muestra_1 + tamano_muestra_2 - 2, 2),
    )


def intervalo_caso_7(
        numero_exitos: int,
        tamano_muestra: int,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Proporción poblacional (𝑃).
    - Situación: Para una muestra grande con 𝑃 pequeña.
    - Estimador puntual: Proporción muestral (𝑝).
    
    :param numero_exitos: Número de exitos (X) de la muestra.
    :type numero_exitos: int
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, proporción
    muestral (𝑝) y el valor crítico de la distribución
    normal estándar (Z).
    :rtype: tuple[float, float, float, float]
    """
    # datos necesarios
    proporcion_muestral = _calcular_proporcion_muestral(numero_exitos, tamano_muestra)
    valor_critico_Z = _calcular_valor_critico_normal_estandar(porcentaje_confianza)
    
    # intervalos
    raiz = math.sqrt((proporcion_muestral * (1 - proporcion_muestral)) / tamano_muestra)
    intervalo_l = proporcion_muestral - (valor_critico_Z * raiz)
    intervalo_u = proporcion_muestral + (valor_critico_Z * raiz)
    return intervalo_l, intervalo_u, proporcion_muestral, valor_critico_Z


def intervalo_caso_8(
        numero_exitos_1: int,
        numero_exitos_2: int,
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        porcentaje_confianza: int
    ) -> tuple[float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de proporciones
    poblacionales (𝑃₁ - 𝑃₂).
    - Situación: Para dos muestra grandes e independientes de una
    distribución normal.
    - Estimador puntual: Diferencia de proporciones
    muestrales (𝑝₁ - 𝑝₂).
    
    :param numero_exitos_1: Número de exitos de una primera
    muestra (X₁).
    :type numero_exitos_1: int
    :param numero_exitos_2: Númeor de exitos de uan segunda
    muestra (X₂).
    :type numero_exitos_2: int
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, diferencia de
    proporciones muestrales (𝑝₁ - 𝑝₂), y el valor crítico de la
    distribución normal estándar (Z).
    :rtype: tuple[float, float, float, float]
    """
    # datos necesarios
    proporcion_muestral_1 = _calcular_proporcion_muestral(numero_exitos_1, tamano_muestra_1)
    proporcion_muestral_2 = _calcular_proporcion_muestral(numero_exitos_2, tamano_muestra_2)
    valor_critico_Z = _calcular_valor_critico_normal_estandar(porcentaje_confianza)
    
    # intervalos
    division_1 = (proporcion_muestral_1 * (1 - proporcion_muestral_1)) / tamano_muestra_1
    division_2 = (proporcion_muestral_2 * (1 - proporcion_muestral_2)) / tamano_muestra_2
    raiz = math.sqrt(division_1 + division_2)
    intervalo_l = (proporcion_muestral_1 - proporcion_muestral_2) - (valor_critico_Z * raiz)
    intervalo_u = (proporcion_muestral_1 - proporcion_muestral_2) + (valor_critico_Z * raiz)
    return (
        intervalo_l,
        intervalo_u,
        proporcion_muestral_1 - proporcion_muestral_2,
        valor_critico_Z,
    )


def intervalo_caso_9(
        tamano_muestra: int,
        muestra: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Varianza poblacional (σ²).
    - Situación: Para una muestra cualquiera.
    - Estimador puntual: Varianza muestral (𝑠²).
    
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param muestra: Una muestra válida.
    :type muestra: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, varianza
    muestral (𝑠²) y los grados de libertad para la distribución.
    :rtype: tuple[float, float, float, float]
    """
    # datos necesarios
    media_muestral = _calcular_media(muestra)
    varianza_muestral = _calcular_varianza_muestral(tamano_muestra, muestra, media_muestral)
    chi2_superior, chi2_inferior = _calcular_valor_critico_chi_cuadrada(
        porcentaje_confianza,
        tamano_muestra,
    )
    
    # intervalos
    intervalo_l = (varianza_muestral * (tamano_muestra - 1)) / chi2_superior
    intervalo_u = (varianza_muestral * (tamano_muestra - 1)) / chi2_inferior
    return intervalo_l, intervalo_u, varianza_muestral, tamano_muestra - 1


def intervalo_caso_10(
        tamano_muestra_1: int,
        tamano_muestra_2: int,
        muestra_1: str,
        muestra_2: str,
        porcentaje_confianza: int,
    ) -> tuple[float, float, bool, float, float, float]:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Cociente de varianzas
    poblacionales (σ₁² / σ₂²).
    - Situación: Para dos muestras independientes de
    poblaciones normales.
    - Estimador puntual: Cocientes de varianzas muestrales (𝑠₁² / 𝑠₂²).
    
    :param tamano_muestra_1: Tamaño de una primera muestra (n₁).
    :type tamano_muestra_1: int
    :param tamano_muestra_2: Tamaño de una segunda muestra (n₂).
    :type tamano_muestra_2: int
    :param muestra_1: Una primera muestra válida.
    :type muestra_1: str
    :param muestra_2: Una segunda muestra válida.
    :type muestra_2: str
    :param porcentaje_confianza: Porcentaje de confianza para un
    intervalo de confianza.
    :type porcentaje_confianza: int
    :return: Límite superior e inferior del intervalo, estatus de
    la varianza muestral, grados de libertad x3 para la distribución.
    :rtype: tuple[float, float, str, float, float, float]
    """
    # datos necesarios
    media_muestral_1 = _calcular_media(muestra_1)
    media_muestral_2 = _calcular_media(muestra_2)
    varianza_muestral_1 = _calcular_varianza_muestral(
        tamano_muestra_1,
        muestra_1,
        media_muestral_1,
    )
    varianza_muestral_2 = _calcular_varianza_muestral(
        tamano_muestra_2,
        muestra_2,
        media_muestral_2,
    ) 
    f_superior, f_inferior = _calcular_valor_critico_f(
        tamano_muestra_1,
        tamano_muestra_2,
        porcentaje_confianza,
    )
    
    # intervalos
    intervalo_l = (varianza_muestral_1 / varianza_muestral_2) * (1 / f_superior)
    intervalo_u = (varianza_muestral_1 / varianza_muestral_2) * (1 / f_inferior)
    if intervalo_l <= 1 <= intervalo_u:
        varianzas_son_iguales = True
    else:
        varianzas_son_iguales = False

    return (
        intervalo_l,
        intervalo_u,
        varianzas_son_iguales,
        round(varianza_muestral_1 / varianza_muestral_2, 2),
        tamano_muestra_1 - 1,
        tamano_muestra_2 - 1,
    )
