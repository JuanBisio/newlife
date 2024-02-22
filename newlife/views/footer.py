
import reflex as rx
import newlife.constants as constants

from newlife.styles.styles import Size, Color, TextColor, Font
from newlife.components.link_icon import link_icon
from newlife.components.drawer import drawer
from newlife.components.link_navbar import link_navbar
from newlife.components.ant_components import float_button


def footer(bg) -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            rx.desktop_only(
                rx.chakra.hstack(
                    link_navbar('Newlife', '/', '#FFFFFF00'),
                    link_navbar('Instalaciones',
                                '/instalaciones', '#FFFFFF00'),
                    link_navbar('Actividades', '/actividades', '#FFFFFF00'),
                    link_navbar('Horarios', '/suplementos', '#FFFFFF00'),
                ),
            ),
            rx.mobile_and_tablet(
                drawer()
            ),
            rx.chakra.spacer(),
            rx.chakra.hstack(
                rx.chakra.text('This is', color=Color.WHITE.value,
                        font_size=Size.LARGE.value),
                rx.chakra.text('New Life', color=Color.DARK_RED.value,
                        font_size=Size.LARGE.value)
            ),
            rx.chakra.spacer(),
            rx.desktop_only(
                rx.chakra.hstack(
                    rx.chakra.hstack(
                        link_navbar(
                            rx.chakra.image(
                                src='/icons/instagram.svg',
                                width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            'https://www.instagram.com/newlifegimnasio/'
                        ),
                        link_navbar(
                            rx.chakra.image(
                                src='/icons/whatsapp.svg',
                                width=Size.DEFAULT.value, 
                                height=Size.DEFAULT.value),
                            """https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0"""
                        ),
                        link_navbar(
                            rx.chakra.image(
                                src='/icons/facebook.svg', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            "https://www.facebook.com/newliferiocuarto/"
                        ),
                        link_navbar(
                            rx.chakra.image(
                                src='/icons/twitter.svg', width=Size.DEFAULT.value, height=Size.DEFAULT.value),
                            "https://twitter.com/newlifegimnasio"
                        ),
                    ),
                ),
            ),
            width='100%',

        ),
        float_button(),
        bg=bg,
        position='sticky',
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0',
        width='100%',
        font_family=Font.DEFAULT.value
    )
