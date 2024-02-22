import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.grid_item import grid_item


def maps() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.desktop_only(
                rx.html('<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d6682.547276147136!2d-64.358636!3d-33.128175!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95d200166883e809%3A0xbdb203d7d982775!2sMar%C3%ADa%20Olguin%201324%2C%20X5800%20R%C3%ADo%20Cuarto%2C%20C%C3%B3rdoba%2C%20Argentina!5e0!3m2!1ses-419!2sus!4v1707879795092!5m2!1ses-419!2sus" width="1140" height="534" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'),
            ),
            rx.mobile_and_tablet(
                rx.html('<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d26729.565413549644!2d-64.3455468!3d-33.1302235!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95d200166883e809%3A0xbdb203d7d982775!2sMar%C3%ADa%20Olguin%201324%2C%20X5800%20R%C3%ADo%20Cuarto%2C%20C%C3%B3rdoba%2C%20Argentina!5e0!3m2!1ses-419!2sus!4v1707931235099!5m2!1ses-419!2sus" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>')
            ),
            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )
