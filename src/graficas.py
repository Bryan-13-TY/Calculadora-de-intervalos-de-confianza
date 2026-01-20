import matplotlib.pyplot as plt # graficar intervalos de confianza
import matplotlib.image as mpimg # agregar imagenes a las gráficas
import numpy as np

from scipy.stats import (
    norm, # para calcula la distribución Z
    t, # para calcular la distribución T
    f, # para calcular la distribución F
    chi2, # para calcula la distribución Chi2  
)

from config.config import (
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
    error_estandar = desv_estandar_poblacional / np.sqrt(tamano_muestra)

    # rango para la ditribución normal
    x = np.linspace(media_muestral - 4 * error_estandar, media_muestral + 4 *error_estandar, 1000)
    y = norm.pdf(x, loc=media_muestral, scale=error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_1)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_1}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, label='Distribución normal estándar (Z)', color='black')
    
    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%",
    )

    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        media_muestral,
        color='blue',
        linestyle='--',
        label=f"Media muestral (X̄): {media_muestral:.2f}")

    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de μ")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off')  # oculta ejes

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
    error_estandar = desv_estandar_muestral / np.sqrt(tamano_muestra)

    # crear dominio para la curva t centrada en Media
    x = np.linspace(media_muestral - 4 * error_estandar, media_muestral + 4 * error_estandar, 1000)
    # distribución t centrada en media y escalada (ya que usamos t_alpha2 externo, aquí solo graficamos pdf t estándar centrada en Media)
    y = np.power((1 + ((x - media_muestral) / error_estandar) ** 2 / (tamano_muestra - 1)), - (tamano_muestra) / 2)  # t pdf formula alternativa
    # mejor usar scipy.stats.t.pdf con df=n-1 para exactitud:
    y = t.pdf((x - media_muestral) / error_estandar, df=tamano_muestra - 1) / error_estandar

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_2)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_2}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, label='Distribución t (t de Student)', color='black')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3, label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        media_muestral,
        color='blue',
        linestyle='--',
        label=f"Media muestral (X̄): {media_muestral:.2f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de (μ)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

    plt.tight_layout()
    plt.show()


def graficar_intervalo_z_caso_3(
        dif_medias_muestrales: float,
        limite_superior: float,
        limite_inferior: float,
        porcentaje_confianza: int,
        titulo_intervalo: str
    ) -> None:
    # aproximar el error estándar desde los límites si se quiere la curva
    aprox_error_estandar = (limite_superior - limite_inferior) / 2

    # rango para la ditribución normal
    x = np.linspace(dif_medias_muestrales - 4 * aprox_error_estandar, dif_medias_muestrales + 4 * aprox_error_estandar, 1000)
    y = norm.pdf(x, loc=dif_medias_muestrales, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_3)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_3}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, color='black', label='Distribución normal estándar (Z)')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias muestrales (X̄₁ - X̄₂): {dif_medias_muestrales:.2f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # aproximar el error estándar inversamente a partir del margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_Z)

    # rango para la ditribución normal
    x = np.linspace(dif_medias_muestrales - 4 * aprox_error_estandar, dif_medias_muestrales + 4 * aprox_error_estandar, 1000)
    y = norm.pdf(x, loc=dif_medias_muestrales, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_4)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_4}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, label='Distribución normal estándar (Z)', color='black')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias muestrales (X̄₁ - X̄₂): {dif_medias_muestrales:.2f}")
    
    # título y etiquetas
    axs[0].set_title(f"{titulo_intervalo}")
    axs[0].set_xlabel("Valor de la diferencia (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # aproximar el error estándar desde el margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_t)

    # rango para la ditribución t de Student
    x = np.linspace(dif_medias_muestrales - 4 * aprox_error_estandar, dif_medias_muestrales + 4 * aprox_error_estandar, 1000)
    y = t.pdf((x - dif_medias_muestrales) / aprox_error_estandar, df=grados_libertad) / aprox_error_estandar  # escalada

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_5)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_5}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, color='black', label='Distribución t (t de Welch)')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--', label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--', label=f"Diferencia de medias muestrales (X̄₁ - X̄₂): {dif_medias_muestrales:.2f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la diferencia (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # aproximar el error estándar desde el margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_t)

    # rango para la ditribución t de Student
    x = np.linspace(dif_medias_muestrales - 4 * aprox_error_estandar, dif_medias_muestrales + 4 * aprox_error_estandar, 1000)
    y = t.pdf((x - dif_medias_muestrales) / aprox_error_estandar, df=grados_libertad) / aprox_error_estandar

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_6)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_6}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, color='black', label='Distribución t (t de Student)')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        dif_medias_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de medias (X̄₁ - X̄₂): {dif_medias_muestrales:.2f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la diferencia (μ₁ - μ₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # aproximar el error estándar inverso desde los márgenes
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_Z)

    # rango para la ditribución normal
    x = np.linspace(proporcion_muestral - 4 * aprox_error_estandar, proporcion_muestral + 4 * aprox_error_estandar, 1000)
    y = norm.pdf(x, loc=proporcion_muestral, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_7)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_7}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, color='black', label='Distribución normal estándar (Z)')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}")
    axs[0].axvline(
        proporcion_muestral,
        color='blue',
        linestyle='--',
        label=f"Proporción muestral p = {proporcion_muestral:.3f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la proporción (p)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # aproximar el error estándar desde del margen
    aprox_error_estandar = (limite_superior - limite_inferior) / (2 * valor_critico_Z)    

    # rango para la ditribución normal
    x = np.linspace(dif_proporciones_muestrales - 4 * aprox_error_estandar, dif_proporciones_muestrales + 4 * aprox_error_estandar, 1000)
    y = norm.pdf(x, loc=dif_proporciones_muestrales, scale=aprox_error_estandar)

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_8)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_8}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})
    
    # ====== gráfica ======
    axs[0].plot(x, y, color='black', label='Distribución normal estándar (Z)')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}")
    axs[0].axvline(
        dif_proporciones_muestrales,
        color='blue',
        linestyle='--',
        label=f"Diferencia de proporciones muestrales (p₁ - p₂) = {dif_proporciones_muestrales:.3f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la diferencia (P₁ - P₂)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper left')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # rango para valores de sigma cuadrada
    x = np.linspace(0.01, limite_superior * 1.5, 1000)
    chi_vals = (grados_libertad * varianza_muestral) / x # cambio de variable: x = (gl * s²) / χ²
    y = chi2.pdf(chi_vals, df=grados_libertad) * (grados_libertad * varianza_muestral) / (x ** 2)  # PDF transformada

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_9)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_9}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, label='Distribución X² (Chi-cuadrada)', color='black')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.2f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.2f}")
    axs[0].axvline(
        varianza_muestral,
        color='blue',
        linestyle='--',
        label=f"Varianza muestral (S²): {varianza_muestral:.2f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Valor de la varianza (σ²)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper right')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

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
    # dominio para la curva de la razón
    x = np.linspace(0.01, limite_superior * 1.5, 1000)
    f_vals = (x / coc_varianzas_muestrales)
    y = f.pdf(f_vals, dfn=grados_libertad_1, dfd=grados_libertad_2) / coc_varianzas_muestrales # transformación del PDF de F

    try:
        formula_intervalo = mpimg.imread(IMAGE_INTERVAL_CASE_10)
    except FileNotFoundError:
        print(f"Imagen no encontrada en: {IMAGE_INTERVAL_CASE_10}")
        return
    
    # crear figura con 2 subplots (gráfica + imagen de la fórmula)
    _, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [3, 1]})

    # ====== gráfica ======
    axs[0].plot(x, y, color='black', label='Distribución F (F de Fisher)')

    # sombrear el nivel de confianza
    axs[0].fill_between(
        x, y,
        where=(x >= limite_superior) & (x <= limite_inferior),
        color='green',
        alpha=0.3,
        label=f"Nivel de confianza: {porcentaje_confianza}%")
    
    # líneas verticales
    axs[0].axvline(
        limite_superior,
        color='orange',
        linestyle='--',
        label=f"Límite inferior: {limite_superior:.3f}")
    axs[0].axvline(
        limite_inferior,
        color='red',
        linestyle='--',
        label=f"Límite superior: {limite_inferior:.3f}")
    axs[0].axvline(
        coc_varianzas_muestrales,
        color='blue',
        linestyle='--',
        label=f"Razón muestral (S₁² / S₂²): {coc_varianzas_muestrales:.3f}")
    
    # título y etiquetas
    axs[0].set_title(titulo_intervalo)
    axs[0].set_xlabel("Razón de varianzas (σ₁² / σ₂²)")
    axs[0].set_ylabel("Densidad de probabilidad")
    axs[0].legend(loc='upper right')
    axs[0].grid(True)

    # ====== imagen de la fórmula del intervalo ======
    axs[1].imshow(formula_intervalo)
    axs[1].axis('off') # oculta ejes

    plt.tight_layout()
    plt.show()