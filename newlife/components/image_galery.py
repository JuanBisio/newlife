import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles

def image_galery(image:str) -> rx.Component:
    return rx.chakra.image(
            src=image,
            width='25em',
            height='30em',
            #padding_x=Size.BIG.value,
        )