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
                    font_size='1.7em',
                    color=Color.DARK_RED.value,
                    margin_bottom='0px',
                    padding_bottom='0px',
                ),
                rx.chakra.text(
                    'relax',
                    font_size=Size.DEFAULT.value,
                    color=Color.WHITE.value,
                    margin_bottom='5px',
                    padding_bottom='0px',
                ),
                rx.link(
                    rx.chakra.button(
                        'EMPEZAR',
                        bg=Color.DARK_RED.value,
                        border_radius='5px',
                        width='50%',
                        _hover={
                            "background_color": Color.PRIMARY.value,
                        },
                    ),
                    href='#galery'
                ),
                display='flex',
                text_aling='left',
                justify_content='left',
                align_items='left',
                margin_x=Size.BIG.value,
                max_width=['90%', '90%', '70%', '30%', '30%',]
            ),

            display='flex',
            justify_content='left',
            align_items='center',
            min_width='100vw',
            height='89vh',
            margin='0px !important',
            font_family=Font.TITLE.value,
            bg=color_bg,
        ),
        background_image='/instalaciones/2.webp',
        background_size='contain',
        background_attachment='fixed',
        background_position='center',
    )
