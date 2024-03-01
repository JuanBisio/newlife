import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.horarios_item_mobile import horarios_item_mobile
import newlife.horarios_constanst as c


def horarios_mobile() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.tabs(
            rx.chakra.tab_list(
                rx.chakra.tab("Lun"),
                rx.chakra.tab("Mar"),
                rx.chakra.tab("Mie"),
                rx.chakra.tab("Jue"),
                rx.chakra.tab("Vie"),
                rx.chakra.tab("Sab"),

            ),
            rx.chakra.tab_panels(
                rx.chakra.tab_panel(
                    rx.chakra.center(horarios_item_mobile(c.LUNES))
                ),
                rx.chakra.tab_panel(
                    rx.chakra.center(horarios_item_mobile(c.MARTES))
                ),
                rx.chakra.tab_panel(
                    rx.chakra.center(horarios_item_mobile(c.MIERCOLES))
                ),
                rx.chakra.tab_panel(
                    rx.chakra.center(horarios_item_mobile(c.JUEVES))
                ),
                rx.chakra.tab_panel(
                    rx.chakra.center(horarios_item_mobile(c.VIERNES))
                ),
                rx.chakra.tab_panel(
                    rx.chakra.center(horarios_item_mobile(c.SABADO))
                ),
            ),
            width="100%",
            bg=Color.PRIMARY.value,
            color="white",
            align='center'
        ),
    )
