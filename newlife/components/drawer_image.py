import reflex as rx
from newlife.styles.styles import Size, Color, TextColor
from newlife.components.link_navbar import link_navbar


class ImageDrawerState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def drawer_image(txt,img) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.button(
            txt,
            #rx.chakra.icon(
            #    tag='hamburger',
            #    width=Size.MEDIUM.value,
            #    height=Size.MEDIUM.value,
            #),
            on_click=ImageDrawerState.change,
            width='100%',
            height='27em',
            opacity='0%',
            color=Color.WHITE.value,
            animation='5s easy',
            _hover={
                'background':'#FFFFFF00',
                'border': '5px solid red',
                'opacity': '100%'
            },
        ),
        rx.chakra.modal(
            rx.chakra.modal_overlay(
                rx.chakra.modal_content(
                    rx.chakra.modal_header(txt,rx.chakra.divider()),
                    rx.chakra.modal_body(
                        rx.chakra.image(
                            src=img
                        )
                    ),
                    rx.chakra.modal_footer(
                        rx.chakra.button(
                            "Cerrar",
                            on_click=ImageDrawerState.change,
                            bg=Color.DARK_RED.value,
                            _hover={
                                'background_color': '#5F2C23DD'
                            },

                        )
                    ),
                    bg=Color.PRIMARY.value
                ),
            ),
            is_open=ImageDrawerState.show,
            width='30em',
            height='30em',
        ),
    )
