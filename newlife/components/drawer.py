import reflex as rx

from newlife.styles.styles import Size, Color, TextColor
from newlife.components.link_navbar import link_navbar


def drawer(dr='drawner') -> rx.Component:
    return rx.chakra.box(
        rx.script(src=f'/js/{dr}.js'),
        rx.chakra.button(
           rx.chakra.icon(
               tag='hamburger',
               width=Size.MEDIUM.value,
               height=Size.MEDIUM.value,
           ),
           class_name='c-hamburger c-hamburger--htx',
           bg='none',
           _hover={
               'background_color': Color.DARK_RED.value
           }
        
        ),
        rx.chakra.box(
            rx.chakra.box(
                rx.chakra.box(
                    rx.chakra.box(
                        "New Life",
                        display='flex',
                        justify_content='center',
                        font_size='1.7em',
                        color=Color.DARK_RED.value,
                    ),
                    rx.chakra.box(
                        rx.chakra.vstack(
                            link_navbar('Newlife', '/', '#FFFFFF00', False),
                            link_navbar('Instalaciones',
                                        '/instalaciones', '#FFFFFF00', False),
                            link_navbar('Actividades',
                                        '/actividades', '#FFFFFF00', False),
                            link_navbar('Horarios', '/horarios',
                                        '#FFFFFF00', False),
                            # link_navbar('Sauna', '/sauna', '#FFFFFF00', False,),
                            link_navbar(
                                'Sauna', 'https://sites.google.com/view/newlife-sauna/inicio', '#FFFFFF00', False),
                        ),
                        font_size=Size.MEDIUM.value,
                        display='flex',
                        justify_content='center',
                    ),
                    bg="#1C1C1ACC",
                    id='menu'
                ),
                class_name='list-unstyled'
            ),
            class_name='sub-menu open',
            role='navigation'
        ),
    )
