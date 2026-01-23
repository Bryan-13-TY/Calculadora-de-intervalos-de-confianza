"""
En este módulo se definen las funciones para graficar el intervalo de
confianza correspondiente a cada parámetro a estimar y caso.
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from scipy.stats import (
    norm,
    t,
    f,
    chi2,
)

from config import (
    IMAGE_INTERVAL_CASE_1,
    IMAGE_INTERVAL_CASE_2,
    IMAGE_INTERVAL_CASE_3,
    IMAGE_INTERVAL_CASE_4,
    IMAGE_INTERVAL_CASE_5,
    IMAGE_INTERVAL_CASE_6,
    IMAGE_INTERVAL_CASE_7,
    IMAGE_INTERVAL_CASE_8,
    IMAGE_INTERVAL_CASE_9,
    IMAGE_INTERVAL_CASE_10,
)

def graficar_intervalo_z_caso_1(
        media_muestral: float,
        limite_superior: float,
        limite_inferior: float,
        desv_estandar_poblacional: float,
        tamano_muestra: int,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Gráfica el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Una media poblacional (μ).
    - Situación: Distribución normal, muestra grande
    y varianza conocida.
    - Estimador puntual: Una media muestral (X̄).
    
    :param media_muestral: Media muestral (X̄).
    :type media_muestral: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_inferior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param desv_estandar_poblacional: Desviación estándar
    poblacional (σ).
    :type desv_estandar_poblacional: float
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    error_estandar = desv_estandar_poblacional / np.sqrt(tamano_muestra)

    # Rango para la ditribución normal
    x = np.linspace(media_muestral - 4 * error_estandar, media_muestral + 4 *error_estandar, 1000)
    y = norm.pdf(x, loc=media_muestral, scale=error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_1)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_1}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, label='Distribución normal estándar (Z)', color='black')
    
    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )

    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        media_muestral,
        color='blue',
        linestyle='--',
        label=f"Media muestral (X̄): {media_muestral:.3f}",
    )

    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de μ")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_t_caso_2(
        media_muestral: float,
        limite_superior: float,
        limite_inferior: float,
        desv_estandar_muestral: float,
        tamano_muestra: int,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Gráfica el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Una media poblacional (μ).
    - Situación: Distribución normal, muestra grande
    y varianza desconocida.
    - Estimador puntual: Una media muestral (X̄).
    
    :param media_muestral: Media muestral (X̄).
    :type media_muestral: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param desv_estandar_muestral: Desviación estándar muestral (S).
    :type desv_estandar_muestral: float
    :param tamano_muestra: Tamaño de una muestra (n).
    :type tamano_muestra: int
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    error_estandar = desv_estandar_muestral / np.sqrt(tamano_muestra)

    # Crear dominio para la curva t centrada en Media
    x = np.linspace(media_muestral - 4 * error_estandar, media_muestral + 4 * error_estandar, 1000)
    # Distribución t centrada en media y escalada (ya que usamos
    # t_alpha2 externo, aquí solo graficamos pdf t estándar
    # centrada en Media)
    y = np.power(
        (1 + ((x - media_muestral) / error_estandar) ** 2 / (tamano_muestra - 1)),
        - (tamano_muestra) / 2,
    )  # t pdf fórmula alternativa
    # Mejor usar scipy.stats.t.pdf con df=n-1 para exactitud:
    y = t.pdf((x - media_muestral) / error_estandar, df=tamano_muestra - 1) / error_estandar

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_2)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_2}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, label='Distribución t (t de Student)', color='black')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3, label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        media_muestral,
        color='blue',
        linestyle='--',
        label=f"Media muestral (X̄): {media_muestral:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de (μ)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_z_caso_3(
        dif_medias_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras independientes de poblaciones
    normales con varianzas
    conocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param dif_medias_muestrales: Diferencia de medias
    muestrales (X̄₁ - X̄₂).
    :type dif_medias_muestrales: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Aproximar el error estándar desde los límites si se quiere la curva
    aprox_error_estandar = (limite_superior - limite_inferior) / 2

    # Rango para la ditribución normal
    x = np.linspace(
        dif_medias_muestrales - 4 * aprox_error_estandar,
        dif_medias_muestrales + 4 * aprox_error_estandar,
        1000,
    )
    y = norm.pdf(x, loc=dif_medias_muestrales, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_3)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_3}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, color='black', label='Distribución normal estándar (Z)')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias muestrales (X̄₁ - X̄₂): {dif_medias_muestrales:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_z_caso_4(
        dif_medias_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        valor_critico_Z: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras grandes (n > 30) independientes
    de poblaciones normales con
    varianzas diferentes y desconocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param dif_medias_muestrales: Diferencia de medias
    muestrales (X̄₁ - X̄₂).
    :type dif_medias_muestrales: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param valor_critico_Z: Valor crítico de la distribución
    normal estándar (Z).
    :type valor_critico_Z: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Aproximar el error estándar inversamente a partir del margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_Z)

    # Rango para la ditribución normal
    x = np.linspace(
        dif_medias_muestrales - 4 * aprox_error_estandar,
        dif_medias_muestrales + 4 * aprox_error_estandar,
        1000,
    )
    y = norm.pdf(x, loc=dif_medias_muestrales, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_4)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_4}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, label='Distribución normal estándar (Z)', color='black')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias muestrales (X̄₁ - X̄₂): {dif_medias_muestrales:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(f"{titulo_intervalo}")
    axs[0].set_xlabel("Valor de la diferencia (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_t_caso_5(
        dif_medias_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        valor_critico_t: float,
        grados_libertad: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras chicas independientes de
    poblaciones normales con
    varianzas diferentes y desconocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param dif_medias_muestrales: Diferencia de medias
    muestrales (X̄₁ - X̄₂).
    :type dif_medias_muestrales: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param valor_critico_t: Valor crítico de la distribución t.
    :type valor_critico_t: float
    :param grados_libertad: Grados de libertad del valor crítico.
    :type grados_libertad: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Aproximar el error estándar desde el margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_t)

    # Rango para la ditribución t de Student
    x = np.linspace(
        dif_medias_muestrales - 4 * aprox_error_estandar,
        dif_medias_muestrales + 4 * aprox_error_estandar,
        1000,
    )
    y = t.pdf(
        (x - dif_medias_muestrales) / aprox_error_estandar,
        df=grados_libertad,
    ) / aprox_error_estandar  # escalada

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_5)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_5}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, color='black', label='Distribución t (t de Welch)')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias muestrales (X̄₁ - X̄₂): {dif_medias_muestrales:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la diferencia (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_t_caso_6(
        dif_medias_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        valor_critico_t: float,
        grados_libertad: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de medias
    poblacionales (μ₁ - μ₂).
    - Situación: Para dos muestras independientes de poblaciones
    normales con varianzas
    iguales y desconocidas.
    - Estimador puntual: Diferencia de medias muestrales (X̄₁ - X̄₂).
    
    :param dif_medias_muestrales: Diferencia de medias
    muestrales (X̄₁ - X̄₂).
    :type dif_medias_muestrales: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param valor_critico_t: Valor crítico de la distribución t.
    :type valor_critico_t: float
    :param grados_libertad: Grados de libertad del valor crítico.
    :type grados_libertad: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Aproximar el error estándar desde el margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_t)

    # Rango para la ditribución t de Student
    x = np.linspace(
        dif_medias_muestrales - 4 * aprox_error_estandar,
        dif_medias_muestrales + 4 * aprox_error_estandar,
        1000,
    )
    y = t.pdf(
        (x - dif_medias_muestrales) / aprox_error_estandar,
        df=grados_libertad
    ) / aprox_error_estandar

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_6)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_6}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, color='black', label='Distribución t (t de Student)')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias (X̄₁ - X̄₂): {dif_medias_muestrales:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la diferencia (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_z_caso_7(
        proporcion_muestral: float,
        limite_superior: float,
        limite_inferior: float,
        valor_critico_Z: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Proporción poblacional (𝑃).
    - Situación: Para una muestra grande con 𝑃 pequeña.
    - Estimador puntual: Proporción muestral (𝑝).
    
    :param proporcion_muestral: Proporción muestral (𝑝).
    :type proporcion_muestral: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param valor_critico_Z: Valor crítico de la distribución normal
    estándar (Z).
    :type valor_critico_Z: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Aproximar el error estándar inverso desde los márgenes
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_Z)

    # Rango para la ditribución normal
    x = np.linspace(
        proporcion_muestral - 4 * aprox_error_estandar,
        proporcion_muestral + 4 * aprox_error_estandar,
        1000,
    )
    y = norm.pdf(x, loc=proporcion_muestral, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_7)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_7}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, color='black', label='Distribución normal estándar (Z)')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        proporcion_muestral,
        color='blue',
        linestyle='--',
        label=f"Proporción muestral p = {proporcion_muestral:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la proporción (p)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_z_caso_8(
        dif_proporciones_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        valor_critico_Z: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Diferencia de proporciones
    poblacionales (𝑃₁ - 𝑃₂).
    - Situación: Para dos muestra grandes e independientes de una
    distribución normal.
    - Estimador puntual: Diferencia de proporciones
    muestrales (𝑝₁ - 𝑝₂).
    
    :param dif_proporciones_muestrales: Diferencia de proporciones
    muestrales (𝑝₁ - 𝑝₂).
    :type dif_proporciones_muestrales: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param valor_critico_Z: Valor crítico de la distribución normal
    estándar (Z).
    :type valor_critico_Z: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Aproximar el error estándar desde del margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_Z)    

    # Rango para la ditribución normal
    x = np.linspace(
        dif_proporciones_muestrales - 4 * aprox_error_estandar,
        dif_proporciones_muestrales + 4 * aprox_error_estandar,
        1000,
    )
    y = norm.pdf(x, loc=dif_proporciones_muestrales, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_8)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_8}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})
    
    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, color='black', label='Distribución normal estándar (Z)')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        dif_proporciones_muestrales,
        color='blue',
        linestyle='--',
        label=(
            f"Diferencia de proporciones muestrales (p₁ - p₂) = "
            f"{dif_proporciones_muestrales:.3f}"
        ),
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la diferencia (P₁ - P₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_chi2_caso_9(
        varianza_muestral: float,
        limite_superior: float,
        limite_inferior: float,
        grados_libertad: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Varianza poblacional (σ²).
    - Situación: Para una muestra cualquiera.
    - Estimador puntual: Varianza muestral (𝑠²).
    
    :param varianza_muestral: Varianza muestral (𝑠²).
    :type varianza_muestral: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param grados_libertad: Grador de libertad del valor crítico.
    :type grados_libertad: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Rango para valores de sigma cuadrada
    x = np.linspace(0.01, limite_superior * 1.5, 1000)
    # Cambio de variable: x = (gl * s²) / χ²
    chi_vals = (grados_libertad * varianza_muestral) / x
    y = chi2.pdf(
        chi_vals,
        df=grados_libertad
    ) * (grados_libertad * varianza_muestral) / (x ** 2)  # PDF transformada

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_9)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_9}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, label='Distribución X² (Chi-cuadrada)', color='black')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        varianza_muestral,
        color='blue',
        linestyle='--',
        label=f"Varianza muestral (S²): {varianza_muestral:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la varianza (σ²)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper right')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_f_caso_10(
        coc_varianzas_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        grados_libertad_1: float,
        grados_libertad_2: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    """
    Calcula el intervalo de confianza para la siguiente situación:
    - Parámetro a estimar: Cociente de varianzas
    poblacionales (σ₁² / σ₂²).
    - Situación: Para dos muestras independientes de
    poblaciones normales.
    - Estimador puntual: Cocientes de varianzas muestrales (𝑠₁² / 𝑠₂²).
    
    :param coc_varianzas_muestrales: Cocientes de varianzas
    muestrales (𝑠₁² / 𝑠₂²)
    :type coc_varianzas_muestrales: float
    :param limite_superior: Límite superior del intervalo de confianza.
    :type limite_superior: float
    :param limite_superior: Límite inferior del intervalo de confianza.
    :type limite_inferior: float
    :param grados_libertad_1: Primeros grados de libertad del
    valor crítico.
    :type grados_libertad_1: float
    :param grados_libertad_2: Segundos grados de libtertad del
    valor crítico.
    :type grados_libertad_2: float
    :param porcentaje_confianza: Porcentaje de confianza para el
    intervalo de confianza.
    :type porcentaje_confianza: int
    :param titulo_intervalo: Título de la gráfica del intervalo.
    :type titulo_intervalo: str
    """
    # Dominio para la curva de la razón
    x = np.linspace(0.01, limite_superior * 1.5, 1000)
    f_vals = (x / coc_varianzas_muestrales)
    y = f.pdf(
        f_vals,
        dfn=grados_libertad_1,
        dfd=grados_libertad_2
    ) / coc_varianzas_muestrales  # Transformación del PDF de F

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_10)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_10}")
        return
    
    # Crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ==============
    # Gráfica
    # ==============
    axs[0].plot(x, y, color='black', label='Distribución F (F de Fisher)')

    # Sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )
    
    # Líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}",
    )
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}",
    )
    axs[0].axvline(
        coc_varianzas_muestrales,
        color='blue',
        linestyle='--',
        label=f"Razón muestral (S₁² / S₂²): {coc_varianzas_muestrales:.3f}",
    )
    
    # Título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Razón de varianzas (σ₁² / σ₂²)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper right')
    axs[0].grid(True)

    # =========================================
    # Imagen de la fórmula del intervalo
    # =========================================
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # Oculta ejes

    plt.tight_layout()
    plt.show()
