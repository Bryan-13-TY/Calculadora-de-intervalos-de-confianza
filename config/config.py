from pathlib import Path

# ====== imagenes ======
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGES_DIR = BASE_DIR / "assets" / "images"
IMAGE_INTERVAL_CASE_1 = IMAGES_DIR / "interval_case_1.png"
IMAGE_INTERVAL_CASE_2 = IMAGES_DIR / "interval_case_2.png"
IMAGE_INTERVAL_CASE_3 = IMAGES_DIR / "interval_case_3.png"
IMAGE_INTERVAL_CASE_4 = IMAGES_DIR / "interval_case_4.png"
IMAGE_INTERVAL_CASE_5 = IMAGES_DIR / "interval_case_5.png"
IMAGE_INTERVAL_CASE_6 = IMAGES_DIR / "interval_case_6.png"
IMAGE_INTERVAL_CASE_7 = IMAGES_DIR / "interval_case_7.png"
IMAGE_INTERVAL_CASE_8 = IMAGES_DIR / "interval_case_8.png"
IMAGE_INTERVAL_CASE_9 = IMAGES_DIR / "interval_case_9.png"
IMAGE_INTERVAL_CASE_10 = IMAGES_DIR / "interval_case_10.png"

# ====== menú e información sobre los casos ======
MENU_PRINCIPAL = """
/*---------------------------------------.
| CALCULADORA DE INTERVALOS DE CONFIANZA |
`---------------------------------------*/

>> Elije el parámetro a estimar
            
1.- Una media (μ)
2.- Una diferencia de medias (μ₁ - μ₂)
3.- Una proporción (𝑃)
4.- Una diferencia de proporciones (𝑃₁ - 𝑃₂)
5.- Una varianza poblacional (σ²)
6.- El cociente de varianzas poblacionales (σ₁² / σ₂²)
              
>> Escribe 'salir' para terminar el programa
"""

INFO_MEDIA_POBLACIONAL = """
/*-------------------------------.
| Para una media poblacional (μ) |
`-------------------------------*/

- Ingresa cada una de las muestras separadas por un espacio (x₁ x₂ ... xₙ) para calcular la media muestral (X̄).
- El tamaño de la muestra (n) debe coincidir con la cantidad de muestras ingresadas.
- (n) debe ser un número entero.
- Se recomienda que el porcentaje de confianza este entre 90% y 99%. Si este no se conoce usar 95%.
"""

INFO_DIF_MEDIAS_POBLACIONALES = """
/*------------------------------------------------------.
| Para una diferencia de medias poblacionales (μ₁ - μ₂) |
`------------------------------------------------------*/

- Ingresa cada una de las muestras separadas por un espacio (x₁ x₂ ... xₙ) para calcular las medias muestrales (X̄₁ y X̄₂) respectivamente.
- Los tamaños de las muestras (n₁ y n₂) deben coincidir con la cantidad de muestras ingresadas respectivamente.
- (n₁ y n₂) deben ser números enteros.
- Se recomienda que el porcentaje de confianza este entre 90% y 99%. Si este no se conoce usar 95%.
"""

INFO_PROPORCION = """
/*------------------------.
| Para una proporción (𝑃) |
`------------------------*/

- El número de éxitos (X) no debe ser mayor que el tamaño de la muestra (N).
- El tamaño de la muestra no debe ser menor que el número de éxitos.
- Tanto (X) como (N) deben ser números enteros.
- Se recomienda que el porcentaje de confianza este entre 90% y 99%. Si este no se conoce usar 95%.
"""

INFO_DIF_PROPORCIONES = """
/*----------------------------------------------.
| Para una diferencia de proporciones (𝑃₁ - 𝑃₂) |
`----------------------------------------------*/

- El número de éxitos (X₁ y X₂) no deben ser mayores que los tamaños de la muestra (N₁ y N₂) respectivamente.
- Los tamaños de las muestras (N₁ y N₂) no deben ser menores que el número de éxitos (X₁ y X₂) respectivamente.
- Tanto (X₁ y X₂) como (N₁ y N₂) deben ser números enteros.
- Se recomienda que el porcentaje de confianza este entre 90% y 99%. Si este no se conoce usar 95%.
"""

INFO_VARIANZA_POBLACIONAL = """
/*-----------------------------------.
| Para una varianza poblacional (σ²) | 
`-----------------------------------*/

- Ingresa cada una de las muestras separadas por un espacio (x₁ x₂ ... xₙ) para calcular la media muestral (X̄).
- El tamaño de la muestra (n) debe coincidir con la cantidad de muestras ingresadas.
- (n) debe ser un número entero.
- Se recomienda que el porcentaje de confianza este entre 90% y 99%. Si este no se conoce usar 95%.
"""

INFO_COC_VARIANZAS_POBLACIONALES = """
/*--------------------------------------------------------.
| Para el cociente de varianzas poblacionales (σ₁² / σ₂²) |
`--------------------------------------------------------*/

- Ingresa cada una de las muestras separadas por un espacio (x₁ x₂ ... xₙ) para calcular las medias muestrales (X̄₁ y X̄₂) respectivamente.
- Los tamaños de las muestras (n₁ y n₂) deben coincidir con la cantidad de muestras ingresadas respectivamente.
- (n₁ y n₂) deben ser números enteros.
- Se recomienda que el porcentaje de confianza este entre 90% y 99%. Si este no se conoce usar 95%.
"""