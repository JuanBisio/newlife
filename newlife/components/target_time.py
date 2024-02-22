import reflex as rx

from newlife.styles.styles import Color, Size, Font


def target_time(horario, actividad) -> rx.Component:
    return rx.vstack(
        rx.chakra.box(
            rx.text(
                horario,
                margin_top=Size.SMALL.value,
                font_size=Size.DEFAULT.value,
            ),
            display='flex',
            justify_content='left',
            text_aling='left',
        ),
        rx.chakra.vstack(
            rx.chakra.hstack(
                rx.text(
                    actividad,
                    margin_top=Size.SMALL.value,
                    font_size=Size.DEFAULT.value,
                    font_weight='bold',
                ),
                margin_x=Size.SMALL.value,

            ),
            rx.chakra.hstack(
                rx.image(
                    src='/icons/time.svg',
                    width='1.5em',
                    margin_x=Size.SMALL.value,
                    margin_bottom=Size.SMALL.value,
                ),
                rx.text(
                    '60min',
                    font_size=Size.DEFAULT.value,
                ),
            ),
            width='20em',
            border_bottom=f'solid 2px {Color.DARK_RED.value}',
            border_radius='5px',
            bg='#373737',
            display='flex',
            justify_content='left',
            text_aling='left',
            align_items='left',

        ),
        align_items='left',
    )
