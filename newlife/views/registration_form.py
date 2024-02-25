import reflex as rx
from newlife.styles.styles import Color, Size, Font


class RegistrationFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data


class RegistrationTextareaState(rx.State):
    text: str = "Consulta o Duda"


class RegistrationFormErrorState(rx.State):
    name: str

    @rx.var
    def is_error(self) -> bool:
        return len(self.name) <= 3


def registration_form() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                '¡COMIENZA TU EXPERIENCIA AHORA!',
                size='2xl',
                font_family=Font.SUBTITLE.value,
                margin=Size.SMALL.value,
                color=Color.DARK_RED.value,
            ),
            rx.chakra.vstack(
                rx.chakra.form(
                    rx.chakra.input(
                        placeholder='Nombre',
                        on_blur=RegistrationFormErrorState.set_name,
                        name='Nombre: ',
                        type_='text',
                        focus_border_color=Color.DARK_RED.value,
                        error_border_color='#777771',
                        border=f"1px dotted #777771",
                        _hover={
                            'border': f'1px dotted {Color.DARK_RED.value}'
                        },
                    ),
                    rx.chakra.input(
                        placeholder='Apellido',
                        on_blur=RegistrationFormErrorState.set_name,
                        name='Apellido: ',
                        type_='text',
                        focus_border_color=Color.DARK_RED.value,
                        error_border_color='#777771',
                        border=f"1px dotted #777771",
                        _hover={
                            'border': f'1px dotted {Color.DARK_RED.value}'
                        },
                    ),
                    rx.chakra.heading(
                        "Clases", size='lg', color=Color.DARK_RED.value, margin_y=Size.SMALL.value),
                    rx.vstack(
                        rx.chakra.checkbox(
                            'Localizada',
                            color_scheme='yellow',
                            size="md",
                            name='Localizada'
                        ),
                        rx.chakra.checkbox(
                            'Kimax',
                            color_scheme='yellow',
                            size="md",
                            name='Kimax'
                        ),
                        rx.chakra.checkbox(
                            'Full Hit',
                            color_scheme='yellow',
                            size="md",
                            name='Full Hit'
                        ),
                        rx.chakra.checkbox(
                            'Karate',
                            color_scheme='yellow',
                            size="md",
                            name='Karate'
                        ),
                        rx.chakra.checkbox(
                            'Piernas/Abdominales',
                            color_scheme='yellow',
                            size="md",
                            name='Piernas/Abdominales'
                        ),
                        rx.chakra.checkbox(
                            'Ritmos Latinos',
                            color_scheme='yellow',
                            size="md",
                            name='Ritmos Latinos'
                        ),
                        rx.chakra.checkbox(
                            'Piernas/Gluteos',
                            color_scheme='yellow',
                            size="md",
                            name='Kimax'
                        ),
                        rx.chakra.checkbox(
                            'Power Flex',
                            color_scheme='yellow',
                            size="md",
                            name='Power Flex'
                        ),
                        rx.chakra.checkbox(
                            'Entrenamiento Funcional',
                            color_scheme='yellow',
                            size="md",
                            name='Entrenamiento Funcional'
                        ),
                        rx.chakra.checkbox(
                            'Power',
                            color_scheme='yellow',
                            size="md",
                            name='Power'
                        ),
                        rx.chakra.checkbox(
                            'Musculacion',
                            color_scheme='yellow',
                            size="md",
                            name='Musculacion'
                        ),
                        display='flex',
                        text_aling='left',
                        justify_content='left',
                        align_items='left',
                    ),
                    rx.chakra.text_area(
                        value=RegistrationTextareaState.text,
                        on_change=RegistrationTextareaState.set_text,
                        border=f"1px dotted #777771",
                        name='Mensaje: ',
                        focus_border_color=Color.DARK_RED.value,
                        _hover={
                            'border': f'1px dotted {Color.DARK_RED.value}'
                        },
                        margin_y=Size.DEFAULT.value,
                    ),
                    rx.hstack(
                        rx.chakra.button(
                            "Guardar",
                            type_="submit",
                            bg=Color.DARK_RED.value,
                            color=Color.WHITE.value,
                            _hover={
                                'transform': 'scale(1.1)',
                            },
                        ),
                        rx.link(
                            rx.chakra.button(
                                "Enviar a WhatsApp",
                                type_="submit",
                                bg=Color.DARK_RED.value,
                                color=Color.WHITE.value,
                                _hover={
                                    'transform': 'scale(1.1)',
                                },
                            ),
                            href=f'https://api.whatsapp.com/send?phone=+5493584299645&text={RegistrationFormState.form_data.to_string()}',
                            is_external=True
                        ),
                    ),
                    on_submit=RegistrationFormState.handle_submit,
                    reset_on_submit=True,
                    width=['20em', '15em', '15em', '20em', '30em']
                ),
            ),
            max_width='1200px',
        ),
        id='galery',
        bg=Color.PRIMARY.value,
        overflow='overview'
    )
