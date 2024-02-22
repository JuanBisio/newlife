import reflex as rx
from newlife.styles.styles import Color, Size, Font


def spacer() -> rx.Component:
    return rx.chakra.vstack(
        bg=Color.PRIMARY.value,
        width='100%',
        height=Size.MEGA_BIG.value
    )
