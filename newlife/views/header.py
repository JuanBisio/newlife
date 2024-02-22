import reflex as rx

from newlife.styles.styles import Color, Size, Font


def header(color_bg) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.hstack(
            rx.chakra.vstack(
                rx.chakra.text(
                    'La transformacion de tu vida inicia aqui',
                    font_size='1.7em',
                    color=Color.DARK_RED.value,
                    margin_bottom='0px',
                    padding_bottom='0px',
                ),
                rx.chakra.text(
                    'Desafía tu limites y comienza ahora una nueva vida mas saludable, dinámica y divertida. Con tan solo 45 minutos de actividad puedes conseguir resultados increíbles. Tenemos varias opciones en nuestros horarios. Encuentra la mejor propuesta para ti y ven a entrenar con nosotros.',
                    font_size=Size.DEFAULT.value,
                    color=Color.WHITE.value,
                    margin_bottom='5px',
                    padding_bottom='0px',
                ),
                rx.chakra.button(
                    'EMPEZAR',
                    bg=Color.DARK_RED.value,
                    border_radius='5px',
                    width='50%',
                    _hover={
                        "background_color": Color.PRIMARY.value,
                    },
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
            width='100%',
            height='89vh',
            margin='0px !important',
            font_family=Font.TITLE.value,
            bg=color_bg,
        ),
        background_image='CompressFondo3.webp',
        background_size='cover',
        background_attachment='fixed',
        background_position='center',
    )
