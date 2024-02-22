import reflex as rx 
import newlife.styles.styles as styles

from newlife.views.header import header
from newlife.views.navbar import navbar 

def farmacologia_function() -> rx.Component:
    return rx.chakra.box(
        navbar('#212529CC'),
        header('#212529CC'),
        background_image='/protein1.jpeg',    
        style=styles.BASE_STYLE,
    )