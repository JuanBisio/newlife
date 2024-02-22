import reflex as rx

def parrax() -> rx.Component:
    return rx.chakra.vstack(
        display='flex',
        justify_content='center',
        aling_items='center',
        background_image='/CompressFondo4.jpg',
        background_size='contain',
        background_attachment='fixed',
        height='400px',
        width='100%',
        
    )