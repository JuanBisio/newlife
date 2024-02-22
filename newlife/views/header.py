import reflex as rx

from newlife.components.button import buttonPrimary
from newlife.styles.styles import Color, Size, Font


def header(color_bg) -> rx.Component:
    return rx.chakra.hstack(
            rx.chakra.vstack(
                rx.chakra.text(
                    'ES HORA DE COMENZAR',
                    font_size= '1.7em',
                    color=Color.DARK_RED.value,
                    margin_bottom='0px',
                    padding_bottom='0px',
                ),
                rx.chakra.button(
                    'EMPEZAR',
                    bg=Color.DARK_RED.value,
                    border_radius='5px',
                    width='70%',
                    _hover= {
                        "background_color": Color.PRIMARY.value,
                    },
                ),
                rx.chakra.button(
                    'PROMOCIONES',
                    bg=Color.DARK_RED.value,
                    border_radius='5px',
                    width='70%',
                    _hover= {
                        "background_color": Color.PRIMARY.value,
                    },
                ),
                display='flex',
                text_aling='right',
                justify_content='right',
                align_items='right',
                margin_x=Size.BIG.value
            ),

        display='flex',
        justify_content='right',
        align_items='center',
        background_image='CompressFondo3.jpg',  
        background_size= 'cover',
        background_attachment='fixed', 
        background_position='center',
        width='100%',
        height='89vh',
        margin='0px !important',
        font_family=Font.TITLE.value
    )