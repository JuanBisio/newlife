import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles


def about_us_sauna() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'Sauna Finlandesa',
                size='xl',
                color=Color.DARK_RED.value,
                margin=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            rx.chakra.text('El fin de la sauna es administrar calor al cuerpo para producir transpiración, con fines terapéuticos. En la sauna finlandesa se utiliza calor seco, que ronda los 80-100 grados, mientras que la humedad relativa no llega al 15%, lo que propicia una abundante sudoración por parte del cuerpo como mecanismo de refrigeración.',
                           text_aling='center', padding_bottom=Size.SMALL.value),

            color=Color.WHITE.value,
            text_aling='center',
            font_family=Font.DEFAULT.value,
            max_width='800px',
            padding=Size.BIG.value,
        ),
        #bg='#F1F0E4',
        padding_top=Size.BIG.value,
    )
