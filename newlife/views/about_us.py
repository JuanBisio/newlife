import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles


def about_us() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'VENÍ A CONOCERNOS',
                size='xl',
                color=Color.DARK_RED.value,
                margin=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            rx.chakra.heading(
                '¡Transformá tu vida desde hoy!',
                size='lg',
                color=Color.DARK_RED.value,
                margin=Size.DEFAULT.value,
                padding_bottom=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            rx.chakra.text('New Life ha ayudado a generar cambios positivos en la vida de sus clientes, en Río Cuarto, desde su fundación en el año 1987. Creemos que el entrenamiento físico no es solo un pasatiempo sino un estilo de vida. Creamos nuestro gimnasio para que sea el segundo hogar de todos nuestros usuarios. Ya sea que realices actividad física todos los días o que nunca hayas ido a un gimnasio antes, New Life puede ayudar a darle forma en lo que puedes convertirte mañana. Queremos ser aliados de tu entrenamiento.', text_aling='center', padding_bottom=Size.SMALL.value),
            rx.chakra.text('¡Alcanzá tus metas y disfruta de tu nueva vida!',
                           text_aling='center', padding_bottom=Size.SMALL.value),

            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.button(
                        'Contactar',
                        bg=Color.DARK_RED.value,
                        border_radius='5px',
                        color=Color.WHITE.value,
                        _hover={
                            'transform': 'scale(1.1)',
                        },
                    ),
                    href='#footer'
                ),
                rx.chakra.spacer(),
                rx.chakra.link(
                    rx.chakra.button(
                        'Horarios',
                        bg=Color.DARK_RED.value,
                        border_radius='5px',
                        color=Color.WHITE.value,
                        _hover={
                            'transform': 'scale(1.1)',
                        },
                    ),
                    href='/horarios',
                ),
                display='flex',
                justify_content='space_evenly'
            ),

            color=Color.WHITE.value,
            text_aling='center',
            font_family=Font.DEFAULT.value,
            max_width='800px',
            padding=Size.BIG.value,
        ),
        bg=Color.PRIMARY.value,
        padding_top=Size.BIG.value,
    )
