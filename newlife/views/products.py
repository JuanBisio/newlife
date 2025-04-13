import reflex as rx
import newlife.styles.styles as styles

from newlife.components.image_galery import image_galery
from newlife.styles.styles import Color, Size, Font
from newlife.components.cards import cards

def products() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.box(
                cards('Localizada', '/sauna/sauna.png', 'En esta clase vas a realizar trabajos de fuerza y resistencia muscular, utilizando diversos elementos con movimientos coordinativos básicos. Trabajamos con bandas, mancuernas, tobilleras, barras y discos, colchonetas, con el objetivo de aumentar la resistencia y fuerza muscular.    '),
                rx.chakra.spacer(),
                #cards('Kimax', '/sauna/SaunaLogo.png', 'KI MAX ® se practica con una bolsa de pie exclusivamente diseñada, con guantes para pegar a la bolsa. (Traer vendas y/o guantes) Los “Rounds” de KI MAX ® implementan técnicas de Boxeo, Muay Thai y Kickboxing a través de combinaciones simples, intensas y dinámicas.'),
                #rx.chakra.spacer(),
                cards('Karate', '/sauna/SaunaRelax.png', 'El karate es un arte marcial de origen japonés que consiste en la defensa personal. Su práctica tiene beneficios a nivel físico y mental. La disciplina es un elemento esencial para practicar karate. Aprende una nueva filosofía de vida. Clases para niños, adolescentes y adultos'),
                max_width='1000px',
                display='flex',
                flex_direction=["column", "column", "column", "row", "row"],
            ),
        ),
        bg=Color.PRIMARY.value,
    )
