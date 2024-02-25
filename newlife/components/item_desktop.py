import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.target_time import target_time


def item_desktop(actividad='Actividad') -> rx.Component:
    return rx.link(
        rx.chakra.vstack(
            rx.chakra.box(
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
                    src='/iconsImage/time.webp',
                    width='1.3em',
                ),
                rx.text(
                    '60min',
                    font_size=Size.DEFAULT.value,
                ),
                padding=Size.SMALL.value,

            ),
            width="14.3em",
            height="6.5em",
            border_bottom=f'solid 2px {Color.DARK_RED.value}',
            border_radius='5px',
            bg='#373737',
            display='flex',
            justify_content='space-between',
            align_items='left',
            _hover={
                'background_color': Color.DARK_RED.value,
            },
        ),
        _hover={
            'text_decoration': 'none',
        },

    )
