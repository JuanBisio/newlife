import reflex as rx
from newlife.styles.styles import Color, Size, Font


def image_galery(image: str) -> rx.Component:
    return rx.chakra.image(
        src=image,
        width='25em',
        height='30em',
    )
