import reflex as rx
from newlife.styles.styles import Color, Size

def title(text, size, color) -> rx.Component:
    return rx.chakra.heading(
        text,
        size = size,
        color = color
    )