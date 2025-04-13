import reflex as rx
from newlife.styles.styles import Color, Size, Font



def cards(text_button, img, txt) -> rx.Component:
    return rx.chakra.box(
        display='flex',
        justify_content='center',
        align_items='end',
        background_image=img,
        background_position='center',
        background_size='cover',
        transition='0.5s',
        _hover={
            'transform': 'scale(1.1)'
        },
        width='30em',
        height='35em',
        border=Color.DARK_RED.value,
        border_radius=Size.DEFAULT.value,
        margin=Size.DEFAULT.value
    )
