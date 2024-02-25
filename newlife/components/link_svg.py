import reflex as rx
from newlife.styles.styles import Color, Size, Font


def link_svg(text, href: str) -> rx.Component:
    return rx.link(
        rx.chakra.button(
            rx.image(
                src='/icons/whatsapp.svg',
                width=Size.DEFAULT.value,
                height=Size.DEFAULT.value
            ),
            bg='none',
            _hover={
                "background_color": Color.DARK_RED.value,
                'color': Color.DARK_RED.value,
            },
            font_size='1.05em',
            font_family=Font.TITLE.value

        ),
        href='/',
        is_external=True,
        padding_x='.2em',
        text_decoration='none',

    ),
