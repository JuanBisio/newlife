import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles
from newlife.components.grid_item import grid_item


def instalaciones_view() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'Instalaciones',
                size='xl',
                color=Color.DARK_RED.value,
                margin=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            rx.desktop_only(
                rx.chakra.grid(
                    grid_item(2, 2, '/instalaciones/1.webp','Entrenamiento Funcional'),
                    grid_item(2, 2, '/instalaciones/4.webp','Sala de Musculación'),
                    grid_item(2, 2, '/instalaciones/2.webp','Sauna'),
                    grid_item(2, 2, '/instalaciones/3.webp','Dojo de Karate'),
                    template_rows="repeat(4, 1fr)",
                    template_columns="repeat(4, 1fr)",
                    gap=5,
                ),
                max_width='1200px',
                padding=Size.BIG.value,
            ),
            rx.mobile_and_tablet(
                rx.chakra.grid(
                    grid_item(2, 2, '/instalaciones/1.webp','Entrenamiento Funcional'),
                    grid_item(2, 2, '/instalaciones/4.webp','Sala de Musculación'),
                    grid_item(2, 2, '/instalaciones/2.webp','Sauna'),
                    grid_item(2, 2, '/instalaciones/3.webp','Dojo de Karate'),
                    template_rows="repeat(4, 0.5fr)",
                    template_columns="repeat(2, 0.5fr)",
                    gap=5,
                ),
                max_width='1200px',
                padding=Size.BIG.value,
            ),
        ),
        bg=Color.PRIMARY.value,
    )
