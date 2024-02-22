import reflex as rx
from newlife.styles.styles import Color, Size, Font


def grid_item(row, col, img, txt) -> rx.Component:
    return rx.chakra.grid_item(
        rx.chakra.box(
            rx.chakra.heading(
                txt,
                size='lg',
                color=Color.DARK_RED.value,
                font_family=Font.SUBTITLE.value,
            ),
            display='flex',
            justify_content='center',
            align_items='center',
            width='100%',
            height='27em',
            opacity='0%',
            color=Color.WHITE.value,
            animation='5s easy',
            _hover={
                'background': '#1C1C1ACC',
                'opacity': '100%'
            },
        ),
        overflow='hidden',
        row_span=row,
        col_span=col,
        background_image=img,
        background_repeat='no-repeat',
        width=['22em','22em','22em','34em','34em'],
        height=['17em','17em','17em','27em','27em'],
        background_size='contain',
        transition='0.5s',


    )
