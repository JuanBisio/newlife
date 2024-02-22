import reflex as rx

from newlife.styles.styles import Color, Size, Font


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


class CVState(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)


color = "rgb(107,99,246)"


class FormErrorState(rx.State):
    name: str

    @rx.var
    def is_error(self) -> bool:
        return len(self.name) <= 3


class TextareaState(rx.State):
    text: str = "Mensaje"


def form() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                '¡FORMÁ PARTE DE NEW LIFE!',
                size='2xl',
                font_family=Font.SUBTITLE.value,
                margin=Size.SMALL.value,
                color=Color.DARK_RED.value,
            ),
            rx.chakra.vstack(
                rx.chakra.form(
                    rx.chakra.box(
                        rx.chakra.form_control(
                            rx.chakra.input(
                                placeholder='Nombre y apellido',
                                on_blur=FormErrorState.set_name,
                                name='nombre y apellido',
                                type_='text',
                                focus_border_color=Color.DARK_RED.value,
                                error_border_color='#777771',
                                border=f"1px dotted #777771",
                                _hover={
                                    'border': f'1px dotted {Color.DARK_RED.value}'
                                },
                            ),
                            rx.cond(
                                FormErrorState.is_error,
                                rx.chakra.form_error_message(
                                    "Almenos debe tener más de cuatro caracteres"
                                ),
                            ),
                            is_invalid=FormErrorState.is_error,
                            is_required=True,
                        ),
                        rx.chakra.form_control(
                            rx.chakra.input(
                                placeholder='Correo electronico',
                                on_blur=FormErrorState.set_name,
                                name='email',
                                type_='email',
                                focus_border_color=Color.DARK_RED.value,
                                error_border_color='#777771',
                                border=f"1px dotted #777771",
                                _hover={
                                    'border': f'1px dotted {Color.DARK_RED.value}'
                                },
                            ),
                            rx.cond(
                                FormErrorState.is_error,
                                rx.chakra.form_error_message(
                                    "Almenos debe tener más de cuatro caracteres"
                                ),
                            ),
                            is_invalid=FormErrorState.is_error,
                            is_required=True,
                        ),
                        rx.chakra.form_control(
                            rx.chakra.input(
                                placeholder='Telefono',
                                on_blur=FormErrorState.set_name,
                                name='Telefono',
                                type_='tel',
                                focus_border_color=Color.DARK_RED.value,
                                error_border_color='#777771',
                                border=f"1px dotted #777771",
                                _hover={
                                    'border': f'1px dotted {Color.DARK_RED.value}'
                                },
                            ),
                            rx.cond(
                                FormErrorState.is_error,
                                rx.chakra.form_error_message(
                                    "Almenos debe tener más de cuatro caracteres"
                                ),
                            ),
                            is_invalid=FormErrorState.is_error,
                            is_required=True,
                        ),
                        # form_upload(),
                        rx.chakra.text_area(
                            value=TextareaState.text,
                            on_change=TextareaState.set_text,
                            name='text',
                            border=f"1px dotted #777771",
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
                                    "color": Color.PRIMARY.value,
                                },
                            ),
                            rx.link(
                                rx.chakra.button(
                                    "Enviar",
                                    # type_="submit",
                                    bg=Color.DARK_RED.value,
                                    color=Color.WHITE.value,
                                    _hover={
                                        "color": Color.PRIMARY.value,
                                    },
                                ),
                                href=f'https://api.whatsapp.com/send?phone=+5493584299645&text={FormState.form_data.to_string()}',
                                is_external=True,
                            ),
                        ),
                    ),
                    width=['20em', '25em', '25em', '40em', '60em'],
                    on_submit=FormState.handle_submit,
                    reset_on_submit=True,
                ),
            ),
            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
    )
