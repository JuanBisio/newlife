import reflex as rx

from newlife.styles.styles import Color, Size, Font

imageD = '/header/CompressFondo3.webp',
imageM = '/header/FondoMobile.webp',
imageT = '/header/FondoTablet.webp',
imageL = '/header/FondoLaptop.webp',

def headerSauna(color_bg) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.hstack(
            rx.chakra.vstack(
                rx.chakra.text(
                    'Un momento para vos',
                    font_size='3em',
                    color=Color.DARK_RED.value,
                    margin_bottom='0px',
                    padding_bottom='0px',
                ),
                rx.chakra.text(
                    'relax',
                    font_size='1.7em',
                    color=Color.WHITE.value,
                    margin_bottom='5px',
                    padding_bottom='0px',
                ),
                rx.link(
                    rx.chakra.button(
                        'Dias y Horarios',
                        bg=Color.DARK_RED.value,
                        border_radius='5px',
                        width='100%',
                        _hover={
                            "background_color": Color.PRIMARY.value,
                        },
                    ),
                    href='#galery'
                ),
                display='flex',
                justify_content='center',
                align_items='center',
                margin_x=Size.BIG.value,
                max_width=['90%', '90%', '70%', '30%', '30%',]
            ),

            display='flex',
            justify_content='center',
            align_items='center',
            min_width='100vw',
            height='89vh',
            margin='0 !important',
            font_family=Font.TITLE.value,
            bg=color_bg,
        ),
        background_image='/instalaciones/2.webp',
        background_size='cover',
        background_attachment='fixed',
        background_position='center',
    )
