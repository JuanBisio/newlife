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
                color= Color.DARK_RED.value,
            ),
            rx.chakra.hstack(
                rx.chakra.vstack(
                    rx.chakra.box(
                        rx.chakra.link(
                            rx.chakra.Image(src='google.webp'),
                            href='https://play.google.com/store/apps/details?id=com.socioplus&hl=es_AR&gl=US&pli=1',
                            is_external=True,
                        ),
                        width='20em',
                        height='4em',
                        margin_bottom='3em',
                    ),
                    rx.chakra.spacer(),
                    rx.chakra.box(
                        rx.chakra.link(
                            rx.chakra.Image(src='apple.webp'),
                            href='https://apps.apple.com/ar/app/socioplus-ux/id1621587015',
                            is_external=True,
                        ),
                        width='20em',
                        height='4em',
                    )
                ),
                rx.tablet_and_desktop(
                    rx.chakra.image(src='SocioP.webp')
                ),
            ),
            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )
