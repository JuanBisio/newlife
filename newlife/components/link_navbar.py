import reflex as rx
from newlife.styles.styles import Color, Size, Font


def link_navbar(text, href: str, bg_color=Color.DARK_RED.value, is_external=True, on_click=rx.redirect('#')) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.button(
            text,
            bg='none',
            _hover={
                "background_color": bg_color,
                'color': Color.DARK_RED.value,
            },
            font_size='1.05em',
            font_family=Font.TITLE.value,
            # type_="button",
            id='reload',
        ),
        href=href,
        is_external=is_external,
        padding_x='.2em',
        text_decoration='none',

    )
