import reflex as rx
from newlife.styles.styles import Color, Size, Font
from newlife.styles.buttonStyle import button

def buttonPrimary(text, borderRadius, onClick,Width=Size.MEGA_BIG.value,Height='2.5em',clr=Color.DARK_RED.value) -> rx.Component:
    return rx.chakra.button(
                text,
                width=Width,
                height=Height,
                border_radius=borderRadius,
                bg=clr,
                _hover={
                    'background_color':Color.PRIMARY.value, 
                },
                on_click=onClick,
            )