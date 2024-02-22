import reflex as rx
from newlife.styles.styles import Color, Size, Font
from newlife.styles.cardsStyles import *

def iconCard(icon, title:str,text:str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.center(
            rx.chakra.vstack(
                rx.chakra.image(
                    src=icon,
                    style=iconStyle
                ),
                rx.chakra.heading(title, size='xl', style=titleStyle),
                rx.chakra.text(text, style=textStyle)
            ),
            bg=Color.PRIMARY.value, 
            height='18em',
            #width=Size.LARGE.value,
        )   
    )