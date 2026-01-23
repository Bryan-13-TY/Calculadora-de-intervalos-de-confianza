"""
Author: García Escamilla Bryan Alexis
Versión: 1.2

En este módulo se presenta un menú interactivo en consola que le
permite al usuario elegir algún caso de estimación e intervalos de
confianza para medias, varianzas y proporciones poblaciones.

Uso:
    py main.py
"""
from src import (
    esperar_enter,
    limpiar_consola,
    ERR_OPCION_NO_VALIDA,
    mostrar_error,
)

from config import (
    INFO_COC_VARIANZAS_POBLACIONALES,
    INFO_DIF_MEDIAS_POBLACIONALES,
    INFO_DIF_PROPORCIONES,
    INFO_MEDIA_POBLACIONAL,
    INFO_PROPORCION,
    INFO_VARIANZA_POBLACIONAL,
    MENU_PRINCIPAL,
)

from casos import (
    intervalo_coc_varianzas_poblacionales,
    intervalo_dif_medias_poblacionales,
    intervalo_dif_proporciones,
    intervalo_media_poblacional,
    intervalo_proporcion,
    intervalo_varianza_poblacional,
)

def main() -> None:
    """Ejecuta el menú principal del programa."""
    limpiar_consola()

    while True:
        print(MENU_PRINCIPAL)
        param = input("Opción: ").strip().lower()
        match param:
            case "1":
                print(INFO_MEDIA_POBLACIONAL)
                intervalo_media_poblacional()
                esperar_enter()
                limpiar_consola()
            case "2":
                print(INFO_DIF_MEDIAS_POBLACIONALES)
                intervalo_dif_medias_poblacionales()
                esperar_enter()
                limpiar_consola()
            case "3":
                print(INFO_PROPORCION)
                intervalo_proporcion()
                esperar_enter()
                limpiar_consola()
            case "4":
                print(INFO_DIF_PROPORCIONES)
                intervalo_dif_proporciones()
                esperar_enter()
                limpiar_consola()
            case "5":
                print(INFO_VARIANZA_POBLACIONAL)
                intervalo_varianza_poblacional()
                esperar_enter()
                limpiar_consola()
            case "6":
                print(INFO_COC_VARIANZAS_POBLACIONALES)
                intervalo_coc_varianzas_poblacionales()
                esperar_enter()
                limpiar_consola()
            case "salir":
                break
            case _:
                mostrar_error(ERR_OPCION_NO_VALIDA)
                esperar_enter()
                limpiar_consola()

if __name__ == "__main__":
    main()
