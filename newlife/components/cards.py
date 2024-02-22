import reflex as rx
from newlife.styles.styles import Color, Size, Font


class ModalState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def cards(text_button, img, txt) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.button(
            text_button,
            width='100%',
            height='2.5em',
            border_radius=Size.SMALL.value,
            bg=Color.DARK_RED.value,
            _hover={
                'background_color': Color.PRIMARY.value,
            },
            on_click=ModalState.change,
            margin='.7em'
        ),
        rx.chakra.modal(
            rx.chakra.modal_overlay(
                rx.chakra.modal_content(
                    rx.chakra.modal_header(text_button, rx.chakra.divider()),
                    rx.chakra.modal_body(
                        txt,
                    ),
                    rx.chakra.modal_footer(
                        rx.chakra.button(
                            "Cerrar",
                            on_click=ModalState.change,
                            bg=Color.DARK_RED.value,
                            _hover={
                                'background_color': '#5F2C23DD'
                            },

                        )
                    ),
                    bg=Color.PRIMARY.value
                ),
            ),
            is_open=ModalState.show,
            width='30em',
            height='30em',
        ),
        display='flex',
        justify_content='center',
        align_items='end',
        background_image=img,
        background_position='center',
        background_size='cover',
        transition='0.5s',
        _hover={
            'transform': 'scale(1.1)'
        },
        width='20em',
        height='30em',
        border=Color.DARK_RED.value,
        border_radius=Size.DEFAULT.value,
        margin=Size.DEFAULT.value
    )
