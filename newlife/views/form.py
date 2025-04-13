import reflex as rx
from newlife.styles.styles import Color, Size, Font

options = ["Cardio/Local", "Kimax", "Full Hit", "Karate", "Piernas/Abdominales", "Ritmos Latinos",
           "Piernas/Gluteos", "Power Flex", "Entrenamiento Funcional", "Power", "Musculación"]


def form() -> rx.Component:
    return rx.chakra.center(
        rx.script(src='/js/form.js'),
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
                    rx.chakra.box(
                        rx.chakra.input(
                            placeholder='Nombre',
                            name='nombre',
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
                            name='Apellido',
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
                        rx.chakra.select(
                            options,
                            name="options",
                            placeholder="Selecciona la clase",
                            color="white",
                            border_color="#777771",
                        ),
                        rx.chakra.input(
                            placeholder='Consulta',
                            name='Consulta',
                            type_='text',
                            focus_border_color=Color.DARK_RED.value,
                            error_border_color='#777771',
                            border=f"1px dotted #777771",
                            _hover={
                                'border': f'1px dotted {Color.DARK_RED.value}'
                            },
                        ),
                        rx.hstack(
                            rx.chakra.button(
                                "Enviar a Whatsapp",
                                type_="submit",
                                bg=Color.DARK_RED.value,
                                color=Color.WHITE.value,
                                _hover={
                                    "color": Color.PRIMARY.value,
                                },
                            ),
                        ),
                    ),
                    width=['20em', '25em', '25em', '40em', '60em'],
                ),
            ),
            max_width='1200px',
        ),
        bg=Color.PRIMARY.value,
        id='galery',
    )
