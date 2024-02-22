import reflex as rx
from newlife.styles.styles import Color, Size, Font


def horarios_item_mobile(horarios) -> rx.Component:
    return rx.chakra.table_container(
        rx.chakra.table(
            rx.chakra.thead(
                rx.chakra.tr(
                    rx.chakra.th("H"),
                    rx.chakra.th("Horarios Verano"),
                ),
            ),
            rx.chakra.tbody(
                rx.chakra.tr(
                    rx.chakra.td('8:00'),
                    rx.chakra.td(horarios[0]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('9:00'),
                    rx.chakra.td(horarios[1]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('10:00'),
                    rx.chakra.td(horarios[2]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('11:00'),
                    rx.chakra.td(horarios[3]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('12:00'),
                    rx.chakra.td(horarios[4]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('13:00'),
                    rx.chakra.td(horarios[5]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('14:00'),
                    rx.chakra.td(horarios[6]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('15:00'),
                    rx.chakra.td(horarios[7]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('16:00'),
                    rx.chakra.td(horarios[8]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('17:00'),
                    rx.chakra.td(horarios[9]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('18:00'),
                    rx.chakra.td(horarios[10]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('19:00'),
                    rx.chakra.td(horarios[11]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('20:00'),
                    rx.chakra.td(horarios[12]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('21:00'),
                    rx.chakra.td(horarios[13]),
                ),
                rx.chakra.tr(
                    rx.chakra.td('22:00'),
                    rx.chakra.td(horarios[14]),
                ),
            ),
            variant="striped",
            color_scheme=Color.DARK_RED.value,

        )
    )
