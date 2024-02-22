import reflex as rx 
from newlife.styles.styles import Size, Color, TextColor
from newlife.components.link_navbar import link_navbar


class New_drawer(rx.State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)


def new_drawer() -> rx.Component:
    return rx.chakra.box(
        rx.chakra.button(
            rx.chakra.text(
                'MENU',
                width=Size.MEDIUM.value,
                height=Size.MEDIUM.value,
            ),
            on_click=New_drawer.right,
            bg='none',
            border_top_left_radius= '10px',
            border_top_right_radius= '10px',
            border_bottom_left_radius= '10px',
            border_bottom_right_radius= '15px',
            _hover={
                'background_color':Color.DARK_RED.value 
            }
             
        ),
        rx.chakra.drawer(
            rx.chakra.drawer_overlay(
                rx.chakra.drawer_content(
                    rx.chakra.drawer_header(
                        "Lethal Supplements",
                        display='flex',
                        justify_content='center',
                        font_size=Size.LARGE.value
                        ),
                    rx.chakra.drawer_body(
                        rx.chakra.vstack(
                            link_navbar('About Us', '/aboutus'),
                            link_navbar('Proteina', '/proteina'),
                            link_navbar('Creatina', '/creatina'),
                            link_navbar('Pre entreno', '/preentreno'),
                        ),
                        font_size=Size.MEDIUM.value,
                        display='flex',
                        justify_content='center',

                        
                    ),
                    rx.chakra.drawer_footer(
                        rx.chakra.button(
                            "Cerrar", 
                            on_click=New_drawer.right,
                            bg=Color.DARK_RED.value,
                        )
                    ),
                    bg="#212529CC",
                )
            ),
            is_open=New_drawer.show_right,
        ),
    )
