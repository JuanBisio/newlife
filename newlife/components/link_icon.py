import reflex as rx 
from newlife.styles.styles import Size, Color

def link_icon(icon:str, url:str) -> rx.Component:
    return rx.chakra.link(
        '',
        rx.chakra.image(
            src=icon,
            width=Size.MEDIUM.value,
            height=Size.MEDIUM.value,
        ),
        href=url,
        is_external=True,
        _hover={
            'background_color':Color.DARK_RED.value,
             
        },
        
    )