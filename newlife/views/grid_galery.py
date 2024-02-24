import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.grid_item import grid_item


def grid_galery() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'DESCARGA LA APP',
                size='2xl',
                font_family=Font.SUBTITLE.value,
                margin=Size.SMALL.value,
                color=Color.DARK_RED.value,
            ),
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.Image(src='/app/iphone.png'),
                    href='https://play.google.com/store/apps/details?id=com.socioplus&hl=es_AR&gl=US&pli=1',
                    is_external=True,
                )
            ),
            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )
