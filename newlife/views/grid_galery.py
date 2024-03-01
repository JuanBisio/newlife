import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.grid_item import grid_item


def grid_galery() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'INGRESA A LA APP WEB',
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
            rx.chakra.link(
                rx.chakra.button(
                    'Aplicación',
                    bg=Color.DARK_RED.value,
                    border_radius='5px',
                    color=Color.WHITE.value,
                    _hover={
                        'transform': 'scale(1.1)',
                    },
                ),
                href='https://newlifegimnasio.misactividades.com/',
                is_external=True
            ),
            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )
