from src.utils import (
    limpiar_consola,
    esperar_enter,
)

from config.config import (
    MENU_PRINCIPAL,
    INFO_MEDIA_POBLACIONAL,
    INFO_DIF_MEDIAS_POBLACIONALES,
    INFO_PROPORCION,
    INFO_DIF_PROPORCIONES,
    INFO_VARIANZA_POBLACIONAL,
    INFO_COC_VARIANZAS_POBLACIONALES,
)

from src.casos import (
    media_poblacional,
    dif_medias_poblacionales,
    proporcion,
    dif_proporciones,
    varianza_poblacional,
    coc_varianzas_poblacionales,
)

from src.errores import (
    OPCION_NO_VALIDA,
)

def main() -> None:
    limpiar_consola()

    while True:
        print(MENU_PRINCIPAL)
        param = input("Opción: ").strip().lower()
        match param:
            case "1":
                print(INFO_MEDIA_POBLACIONAL)
                media_poblacional()
                esperar_enter()
                limpiar_consola()
            case "2":
                print(INFO_DIF_MEDIAS_POBLACIONALES)
                dif_medias_poblacionales()
                esperar_enter()
                limpiar_consola()
            case "3":
                print(INFO_PROPORCION)
                proporcion()
                esperar_enter()
                limpiar_consola()
            case "4":
                print(INFO_DIF_PROPORCIONES)
                dif_proporciones()
                esperar_enter()
                limpiar_consola()
            case "5":
                print(INFO_VARIANZA_POBLACIONAL)
                varianza_poblacional()
                esperar_enter()
                limpiar_consola()
            case "6":
                print(INFO_COC_VARIANZAS_POBLACIONALES)
                coc_varianzas_poblacionales()
                esperar_enter()
                limpiar_consola()
            case "salir":
                break
            case _:
                print(OPCION_NO_VALIDA)
                esperar_enter()
                limpiar_consola()

if __name__ == "__main__":
    main()