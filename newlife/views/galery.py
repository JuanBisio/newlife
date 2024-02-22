import reflex as rx
import newlife.styles.styles as styles

from newlife.components.cards import cards
from newlife.components.image_galery import image_galery
from newlife.styles.styles import Color, Size, Font


def galery() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                '¿CUÁL ES TU META?',
                size='2xl',
                font_family=Font.SUBTITLE.value,
                margin=Size.SMALL.value,
                color=Color.DARK_RED.value,
            ),
            rx.chakra.box(
                cards('Localizada', '/Kimax.webp', 'En esta clase vas a realizar trabajos de fuerza y resistencia muscular, utilizando diversos elementos con movimientos coordinativos básicos. Trabajamos con bandas, mancuernas, tobilleras, barras y discos, colchonetas, con el objetivo de aumentar la resistencia y fuerza muscular.    '),
                rx.chakra.spacer(),
                cards('Kimax', '/CompressFondo1.webp', 'KI MAX ® se practica con una bolsa de pie exclusivamente diseñada, con guantes para pegar a la bolsa. (Traer vendas y/o guantes) Los “Rounds” de KI MAX ® implementan técnicas de Boxeo, Muay Thai y Kickboxing a través de combinaciones simples, intensas y dinámicas.'),
                rx.chakra.spacer(),
                cards('Karate', '/Karate.webp', 'El karate es un arte marcial de origen japonés que consiste en la defensa personal. Su práctica tiene beneficios a nivel físico y mental. La disciplina es un elemento esencial para practicar karate. Aprende una nueva filosofía de vida. Clases para niños, adolescentes y adultos'),
                max_width='1000px',
                display='flex',
                flex_direction=["column", "column", "column", "row", "row"],
            ),
        ),
        bg=Color.PRIMARY.value,
    )
