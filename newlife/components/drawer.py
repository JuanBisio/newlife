import reflex as rx 
from newlife.styles.styles import Size, Color, TextColor
from newlife.components.link_navbar import link_navbar


class DrawerState(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)


def drawer() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.button(
            rx.chakra.icon(
                tag='hamburger',
                width=Size.MEDIUM.value,
                height=Size.MEDIUM.value,
            ),
            on_click=DrawerState.right,
            bg='none',
            _hover={
                'background_color':Color.DARK_RED.value 
            }
             
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    rx.chakra.drawer_header(
                        "New Life",
                        display='flex',
                        justify_content='center',
                        font_size='1.7em',
                        color=Color.DARK_RED.value,
                    ),
                    rx.chakra.drawer_body(
                        rx.chakra.vstack(
                            link_navbar('Newlife', '/','#FFFFFF00'),
                            link_navbar('Instalaciones', '/instalaciones','#FFFFFF00'),
                            link_navbar('Actividades', '/actividades','#FFFFFF00'),
                            link_navbar('Horarios', '/horarios','#FFFFFF00'),
                        ),
                        font_size=Size.MEDIUM.value,
                        display='flex',
                        justify_content='center',

                        
                    ),
                    rx.chakra.drawer_footer(
                        rx.chakra.button(
                            "Cerrar", 
                            on_click=DrawerState.right,
                            bg=Color.DARK_RED.value,
                        )
                    ),
                    bg="#1C1C1ACC",
                )
            ),
            is_open=DrawerState.show_right,
        ),
    )
