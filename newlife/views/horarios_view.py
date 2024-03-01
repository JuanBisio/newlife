import reflex as rx
import newlife.styles.styles as styles

from newlife.styles.styles import Color, Size, Font
from newlife.components.grid_item import grid_item
from newlife.components.horarios_mobile import horarios_mobile
from newlife.components.horarios_desktop import horarios_desktop


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
            rx.desktop_only(
                horarios_desktop(),
                width=['90vw','90vw','90vw','90vw','94vw','96vw','100vw'],
                overview='overflow'
            ),
            rx.mobile_and_tablet(
                horarios_mobile(),
                max_width='1200px',
            ),

            padding=Size.BIG.value,
        ),
        bg=Color.PRIMARY.value,
    )
