import reflex as rx
from newlife.styles.styles import Color, Size, Font


def actividad(img, title, txt, row='row-reverse') -> rx.Component:
    return rx.chakra.center(
        rx.chakra.box(
            rx.chakra.image(
                src=img,
                height='14em',
                width='25em'
            ),
            min_width='40%',
            margin=Size.DEFAULT.value
        ),
        rx.chakra.box(
            rx.chakra.vstack(
                rx.chakra.heading(
                    title,
                    size='lg',
                    color=Color.DARK_RED.value,
                ),
                rx.chakra.text(
                    txt,
                    color=Color.SECONDARY.value,
                ),
            ),
        ),
        display='flex',
        flex_direction=['column', 'column', 'column', row, row],
        margin_y=Size.LARGE.value

    )
