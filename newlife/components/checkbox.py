import reflex as rx
from newlife.styles.styles import Color, Size, Font



def Rcheckbox(txt) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.checkbox(
            txt,
            color_scheme='yellow', 
            size="md",
        )
    )
