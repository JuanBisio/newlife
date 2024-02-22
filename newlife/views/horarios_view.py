import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles
from newlife.components.grid_item import grid_item
from newlife.components.horarios_mobile import horarios_mobile

def horarios_view() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'Horarios',
                size='xl',
                color=Color.DARK_RED.value,
                margin=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            horarios_mobile(),
            max_width='1200px',
            padding=Size.BIG.value,
        ),
        bg=Color.PRIMARY.value,
    )
