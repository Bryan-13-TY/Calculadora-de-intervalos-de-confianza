import math
from scipy.stats import (
    norm, # para calcula la Z
    t, # para calcular la T
    f, # para calcular la F
    chi2, # para calcula la Chi2
)

def calcular_media(muestra: str) -> float:
    numeros = muestra.split()
    numeros_float = [float(numero) for numero in numeros]
    media = round(sum(numeros_float) / len(numeros_float), 4)
    return media


def calcular_s2(tamano_muestra: int, muestra: str, media: float) -> float:
    numeros = muestra.split()
    suma = 0
    for i in range(tamano_muestra):
        suma = round(suma + ((float(numeros[i]) - media) ** 2), 4)

    s2 = round((1 / (tamano_muestra - 1)) * suma, 4)
    return s2


def calcular_v(s12: float, s22: float, tamano_muestra_1: int, tamano_muestra_2: int) -> float:
    numerador = ((s12 / tamano_muestra_1) + (s22 / tamano_muestra_2)) ** 2
    denominador = (((s12 / tamano_muestra_1) ** 2) / tamano_muestra_1 + 1) + ((s22 / tamano_muestra_2 ** 2) / tamano_muestra_1 + 1)
    v = round((numerador / denominador) - 2, 4)
    return v


def calcular_sp(s12: float, s22: float, tamano_muestra_1: int, tamano_muestra_2: int) -> float:
    sp = math.sqrt((((tamano_muestra_1 - 1) * s12) + ((tamano_muestra_2 - 1) * s22)) / tamano_muestra_1 + tamano_muestra_2 - 2)
    return round(sp, 4)


def calcular_p(numero_exitos: int, tamano_muestra: int) -> float:
    p = round(numero_exitos / tamano_muestra, 4)
    return p


def calcular_zalpha2(porcentaje_confianza: int) -> float:
    alpha = 1 - (porcentaje_confianza / 100)
    Z = round(norm.ppf(1 - round(alpha / 2), 4), 4) # type: ignore
    return Z


def calcular_talpha2(porcentaje_confianza: int, gl: float, caso: int) -> float:
    alpha = 1 - (porcentaje_confianza / 100)

    if caso == 2:
        gL = gl - 1
    if caso == 5:
        gL = gl
    if caso == 6:
        gL = gl - 2

    T = round(t.ppf(1 - round(alpha / 2, 4), gL), 3) # type: ignore
    return T


def calcular_falpha2(porcentaje_confianza: int, tamano_muestra_1: int, tamano_muestra_2: int) -> tuple[float, float]:
    alpha = 1 - (porcentaje_confianza / 100)
    gl1 = tamano_muestra_1 - 1
    gl2 = tamano_muestra_2 - 1
    f_superior = round(f.ppf(1 - (alpha / 2), gl1, gl2), 3) # type: ignore
    f_inferior = round(f.ppf(alpha / 2, gl1, gl2), 3) # type: ignore
    return f_superior, f_inferior


def calcular_chialpha2(porcentaje_confianza: int, tamano_muestra: int) -> tuple[float, float]:
    alpha = 1 - (porcentaje_confianza / 100)
    gl = tamano_muestra - 1
    chi2_superior = round(chi2.ppf(1 - (alpha / 2), gl), 3) # type: ignore
    chi2_inferior = round(chi2.ppf(alpha / 2, gl), 3) # type: ignore
    return chi2_superior, chi2_inferior


def intervalo_caso_1(tamano_muestra: int, muestra: str, porcentaje_confianza: int, desv_estandar_poblacional: float) -> tuple[float, float, float]:
    media_Z = round(calcular_media(muestra), 2)
    Z = calcular_zalpha2(porcentaje_confianza)
    intervalo_l = media_Z - (Z * (desv_estandar_poblacional / math.sqrt(tamano_muestra)))
    intervalo_u = media_Z + (Z * (desv_estandar_poblacional / math.sqrt(tamano_muestra)))
    return media_Z, intervalo_u, intervalo_l


def intervalo_caso_2(tamano_muestra: int, muestra: str, porcentaje_confianza: int) -> tuple[float, float, float, float]:
    media_T = round(calcular_media(muestra), 2)
    T = calcular_talpha2(porcentaje_confianza, tamano_muestra, 2)
    S = math.sqrt(calcular_s2(tamano_muestra, muestra, media_T))
    intervalo_l = media_T - (T * (S / math.sqrt(tamano_muestra)))
    intervalo_u = media_T + (T * (S / math.sqrt(tamano_muestra)))
    return media_T, intervalo_u, intervalo_l, S