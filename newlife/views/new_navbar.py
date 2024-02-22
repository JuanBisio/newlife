
import reflex as rx
import newlife.constants as constants

from newlife.styles.styles import Size, Color, TextColor, Font
from newlife.components.link_icon import link_icon
from newlife.components.drawer import drawer
from newlife.components.new_drawer import new_drawer
from newlife.components.link_navbar import link_navbar


def new_navbar(scroll) -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
            drawer(),
            rx.chakra.spacer(),
            rx.chakra.text(
                'LETHAL SUPPLEMENTS',
                font_size= '2.3em',
                text_aling='center',
                margin_bottom='0px',
                font_family=Font.TITLE.value,
                padding_bottom='0px',
            ),
            rx.chakra.spacer(),
            new_drawer(),
            width='100%',
        ),
        bg=scroll,
        position='sticky',
        padding_x=Size.BIG.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0',
        width='100%',
    )
