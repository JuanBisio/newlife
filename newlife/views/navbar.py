
import reflex as rx

from newlife.styles.styles import Size, Color, TextColor, Font
from newlife.components.link_icon import link_icon
from newlife.components.drawer import drawer
from newlife.components.link_navbar import link_navbar
from newlife.components.ant_components import float_button


def navbar(bg, position='sticky') -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            # LOGO
            rx.chakra.image(
                src='/header/LogoR.webp',
                alt='Logo de New Life Gym',
                width='14em',
                height=Size.VERY_BIG.value,
                # border_radius=Size.BIG.value
            ),
            rx.chakra.spacer(),
            # Celular y Tablets

            # Escritorio
            rx.desktop_only(
                rx.chakra.hstack(
                    link_navbar('Newlife', '/', '#FFFFFF00'),
                    link_navbar('Instalaciones',
                                '/instalaciones', '#FFFFFF00'),
                    link_navbar('Actividades', '/actividades', '#FFFFFF00'),
                    link_navbar('Horarios', '/horarios', '#FFFFFF00'),
                ),
            ),

            rx.chakra.spacer(),
            rx.mobile_and_tablet(
                drawer()
            ),
            rx.desktop_only(
                    rx.chakra.hstack(
                        link_navbar(
                                rx.chakra.image(src='/iconsImage/instagram.webp',
                                            width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            'https://www.instagram.com/newlifegimnasio/'
                        ),
                        link_navbar(
                                rx.chakra.image(src='/iconsImage/whatsapp.webp', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            """https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0"""
                        ),
                        link_navbar(
                            rx.chakra.image(
                                    src='/iconsImage/facebook.webp', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            "https://www.facebook.com/newliferiocuarto/"
                        ),
                        link_navbar(
                            rx.chakra.image(
                                    src='/iconsImage/twitter.webp', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            "https://twitter.com/newlifegimnasio"
                        ),
                    ),
            ),
            width='100%',

        ),
        float_button(),
        bg=bg,
        position=position,
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0',
        width='100%',
        font_family=Font.DEFAULT.value
    )
