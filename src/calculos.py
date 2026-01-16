__all__ = ["intervalo_caso_1", "intervalo_caso_2", "intervalo_caso_3",
           "intervalo_caso_4", "intervalo_caso_5", "intervalo_caso_6",
           "intervalo_caso_7", "intervalo_caso_8", "intervalo_caso_9",
           "intervalo_caso_10"]

import math
from scipy.stats import (
    norm, # para calcula la distribución Z
    t, # para calcular la distribución T
    f, # para calcular la distribución F
    chi2, # para calcula la distribución Chi2   
)

def _calcular_media(muestra: str) -> float:
    numeros = muestra.split()
    numeros_float = [float(numero) for numero in numeros]
    media = round(sum(numeros_float) / len(numeros_float), 4)
    return media


def _calcular_s2(tamano_muestra: int, muestra: str, media: float) -> float:
    numeros = muestra.split()
    suma = 0
    for i in range(tamano_muestra):
        suma = round(suma + ((float(numeros[i]) - media) ** 2), 4)

    s2 = round((1 / (tamano_muestra - 1)) * suma, 4)
    return s2


def _calcular_v(s12: float, s22: float, tamano_muestra_1: int, tamano_muestra_2: int) -> float:
    numerador = ((s12 / tamano_muestra_1) + (s22 / tamano_muestra_2)) ** 2
    denominador = (((s12 / tamano_muestra_1) ** 2) / tamano_muestra_1 + 1) + ((s22 / tamano_muestra_2 ** 2) / tamano_muestra_1 + 1)
    v = round((numerador / denominador) - 2, 4)
    return v


def _calcular_sp(s12: float, s22: float, tamano_muestra_1: int, tamano_muestra_2: int) -> float:
    sp = math.sqrt((((tamano_muestra_1 - 1) * s12) + ((tamano_muestra_2 - 1) * s22)) / tamano_muestra_1 + tamano_muestra_2 - 2)
    return round(sp, 4)


def _calcular_p(numero_exitos: int, tamano_muestra: int) -> float:
    p = round(numero_exitos / tamano_muestra, 4)
    return p


def _calcular_zalpha2(porcentaje_confianza: int) -> float:
    alpha = 1 - (porcentaje_confianza / 100)
    Z = round(norm.ppf(1 - round(alpha / 2), 4), 4) # type: ignore
    return Z


def _calcular_talpha2(porcentaje_confianza: int, gl: float, caso: int) -> float:
    alpha = 1 - (porcentaje_confianza / 100)

    if caso == 2:
        gL = gl - 1
    if caso == 5:
        gL = gl
    if caso == 6:
        gL = gl - 2

    T = round(t.ppf(1 - round(alpha / 2, 4), gL), 3) # type: ignore
    return T


def _calcular_falpha2(tamano_muestra_1: int, tamano_muestra_2: int, porcentaje_confianza: int) -> tuple[float, float]:
    alpha = 1 - (porcentaje_confianza / 100)
    gl1 = tamano_muestra_1 - 1
    gl2 = tamano_muestra_2 - 1
    f_superior = round(f.ppf(1 - (alpha / 2), gl1, gl2), 3) # type: ignore
    f_inferior = round(f.ppf(alpha / 2, gl1, gl2), 3) # type: ignore
    return f_superior, f_inferior


def _calcular_chialpha2(tamano_muestra: int, porcentaje_confianza: int) -> tuple[float, float]:
    alpha = 1 - (porcentaje_confianza / 100)
    gl = tamano_muestra - 1
    chi2_superior = round(chi2.ppf(1 - (alpha / 2), gl), 3) # type: ignore
    chi2_inferior = round(chi2.ppf(alpha / 2, gl), 3) # type: ignore
    return chi2_superior, chi2_inferior


def intervalo_caso_1(tamano_muestra: int, muestra: str, porcentaje_confianza: int, desv_estandar_poblacional: float) -> tuple[float, float, float]:
    # datos necesarios
    media = round(_calcular_media(muestra), 2)
    Z = _calcular_zalpha2(porcentaje_confianza)
    
    # intervalos
    multiplicacion = Z * (desv_estandar_poblacional / math.sqrt(tamano_muestra))
    intervalo_l = media - multiplicacion
    intervalo_u = media + multiplicacion
    return intervalo_u, intervalo_l, media


def intervalo_caso_2(tamano_muestra: int, muestra: str, porcentaje_confianza: int) -> tuple[float, float, float, float]:
    # datos necesarios
    media = round(_calcular_media(muestra), 2)
    t = _calcular_talpha2(porcentaje_confianza, tamano_muestra, 2)
    S = math.sqrt(_calcular_s2(tamano_muestra, muestra, media))
    
    # intervalos
    multiplicacion = t * (S / math.sqrt(tamano_muestra))
    intervalo_l = media - multiplicacion
    intervalo_u = media + multiplicacion
    return intervalo_u, intervalo_l, media, S


def intervalo_caso_3(tamano_muestra_1: int, tamano_muestra_2: int, desv_estandar_poblacional_1: float, desv_estandar_poblacional_2: float,
                     muestra_1: str, muestra_2: str, porcentaje_confianza: int) -> tuple[float, float, float]:
    # datos necesarios
    media_1 = round(_calcular_media(muestra_1), 2)
    media_2 = round(_calcular_media(muestra_2), 2)
    Z = _calcular_zalpha2(porcentaje_confianza)

    # intervalos
    raiz = math.sqrt(((desv_estandar_poblacional_1 ** 2) / tamano_muestra_1) + ((desv_estandar_poblacional_2 ** 2) / tamano_muestra_2))
    intervalo_l = (media_1 - media_2) - (Z * raiz)
    intervalo_u = (media_1 - media_2) + (Z * raiz)
    return intervalo_u, intervalo_l, media_1 - media_2


def intervalo_caso_4(tamano_muestra_1: int, tamano_muestra_2: int, muestra_1: str, muestra_2: str, porcentaje_confianza: int) -> tuple[float, float, float, float]:
    # datos necesarios
    media_1 = round(_calcular_media(muestra_1), 2)
    media_2 = round(_calcular_media(muestra_2), 2)
    Z = _calcular_zalpha2(porcentaje_confianza)
    S12 = _calcular_s2(tamano_muestra_1, muestra_1, media_1)
    S22 = _calcular_s2(tamano_muestra_2, muestra_2, media_2)

    # intervalos
    raiz = math.sqrt((S12 / tamano_muestra_1) + (S22 / tamano_muestra_2))
    intervalo_l = (media_1 - media_2) - (Z * raiz)
    intervalo_u = (media_1 - media_2) + (Z * raiz)
    return intervalo_u, intervalo_l, media_1 - media_2, Z


def intervalo_caso_5(tamano_muestra_1: int, tamano_muestra_2: int, muestra_1: str, muestra_2: str, porcentaje_confianza: int) -> tuple[float, float, float, float, float]:
    # datos necesarios
    media_1 = round(_calcular_media(muestra_1), 2)
    media_2 = round(_calcular_media(muestra_2), 2)
    S12 = _calcular_s2(tamano_muestra_1, muestra_1, media_1)
    S22 = _calcular_s2(tamano_muestra_2, muestra_2, media_2)
    V = _calcular_v(S12, S22, tamano_muestra_1, tamano_muestra_2)
    T = _calcular_talpha2(porcentaje_confianza, V, 5)
    
    # intervalos 
    raiz = math.sqrt((S12 / tamano_muestra_1) + (S22 / tamano_muestra_2))
    intervalo_l = (media_1 - media_2) - (T * raiz)
    intervalo_u = (media_1 - media_2) + (T * raiz)
    return intervalo_u, intervalo_l, media_1 - media_2, T, V


def intervalo_caso_6(tamano_muestra_1: int, tamano_muestra_2: int, muestra_1: str, muestra_2: str, porcentaje_confianza: int) -> tuple[float, float, float, float, float]:
    # datos necesarios
    media_1 = round(_calcular_media(muestra_1), 2)
    media_2 = round(_calcular_media(muestra_2), 2)
    S12 = _calcular_s2(tamano_muestra_1, muestra_1, media_1)
    S22 = _calcular_s2(tamano_muestra_2, muestra_2, media_2)
    Sp = _calcular_sp(S12, S22, tamano_muestra_1, tamano_muestra_2)
    T = _calcular_talpha2(porcentaje_confianza, float(tamano_muestra_1 + tamano_muestra_2), 6)

    # intervalos
    raiz = math.sqrt((1 / tamano_muestra_1) + (1 / tamano_muestra_2))
    intervalo_l = (media_1 - media_2) - (T * Sp * raiz)
    intervalo_u = (media_1 - media_2) + (T * Sp * raiz)
    return intervalo_u, intervalo_l, media_1 - media_2, T, round(tamano_muestra_1 + tamano_muestra_2 - 2, 2)


def intervalo_caso_7(numero_exitos: int, tamano_muestra: int, porcentaje_confianza: int) -> tuple[float, float, float, float]:
    # datos necesarios
    p = _calcular_p(numero_exitos, tamano_muestra)
    Z = _calcular_zalpha2(porcentaje_confianza)
    
    # intervalos
    intervalo_l = p - (Z * math.sqrt((p * (1 - p)) / tamano_muestra))
    intervalo_u = p + (Z * math.sqrt((p * (1 - p)) / tamano_muestra))
    return intervalo_u, intervalo_l, p, Z


def intervalo_caso_8(numero_exitos_1: int, numero_exitos_2: int, tamano_muestra_1: int, tamano_muestra_2: int, porcentaje_confianza: int) -> tuple[float, float, float, float]:
    # datos necesarios
    p1 = round(_calcular_p(numero_exitos_1, tamano_muestra_1), 2)
    p2 = round(_calcular_p(numero_exitos_2, tamano_muestra_2), 2)
    Z = _calcular_zalpha2(porcentaje_confianza)
    
    # intervalos
    raiz = math.sqrt(((p1 * (1 - p1)) / tamano_muestra_1) + ((p2 * (1 - p2)) / tamano_muestra_2))
    intervalo_l = (p1 - p2) - (Z * raiz)
    intervalo_u = (p1 - p2) + (Z * raiz)
    return intervalo_u, intervalo_l, p1 - p2, Z


def intervalo_caso_9(tamano_muestra: int, muestra: str, porcentaje_confianza: int) -> tuple[float, float, float, float]:
    # datos necesarios
    media_X = _calcular_media(muestra)
    S2 = _calcular_s2(tamano_muestra, muestra, media_X)
    chi2_superior, chi2_inferior = _calcular_chialpha2(porcentaje_confianza, tamano_muestra)
    
    # intervalos
    intervalo_l = (S2 * (tamano_muestra - 1)) / chi2_superior
    intervalo_u = (S2 * (tamano_muestra - 1)) / chi2_inferior
    return intervalo_u, intervalo_l, S2, tamano_muestra - 1


def intervalo_caso_10(tamano_muestra_1: int, tamano_muestra_2: int, muestra_1: str, muestra_2: str, porcentaje_confianza: int) -> tuple[float, float, str, float, float, float]:
    # datos necesarios 
    media_1 = _calcular_media(muestra_1)
    media_2 = _calcular_media(muestra_2)
    S12 = _calcular_s2(tamano_muestra_1, muestra_1, media_1)
    S22 = _calcular_s2(tamano_muestra_2, muestra_2, media_2)
    f_superior, f_inferior = _calcular_falpha2(tamano_muestra_1, tamano_muestra_2, porcentaje_confianza)
    
    # intervalos
    intervalo_l = (S12 / S22) * (1 / f_superior)
    intervalo_u = (S12 / S22) * (1 / f_inferior)
    if intervalo_l <= 1 <= intervalo_u:
        varianza_estatus = "SI"
    else:
        varianza_estatus = "NO"

    return intervalo_u, intervalo_l, varianza_estatus, round(S12 / S22, 2), tamano_muestra_1 - 1, tamano_muestra_2 - 1