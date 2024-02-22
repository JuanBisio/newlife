import reflex as rx 

def about_function() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.text('Hola mundo About'),
    )
