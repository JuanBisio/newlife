import reflex as rx
from newlife.styles.styles import Color, Size, Font
from newlife.components.horarios_item_mobile import horarios_item_mobile

Lunes = [
    'Apertura',
    'Ritmos Latinos(CG)',
    '-',
    '-',
    'Cierre',
    'Reapertura (13:30)',
    'Full Hiit (14:15)',
    '-',
    'Cierre',
    '-',
    'Reapertura',
    '-',
    'Kimax (20:30)',
    '-',
    'Cierre (22:30)'
]
Martes = [
    'Apertura',
    '-',
    '-',
    'Cierre',
    '-',
    'Reapertura (13:30)',
    'Piernas/Gluteos (14:15)',
    '-',
    'Cierre',
    '-',
    'Reapertura',
    'Entrenamiento Funcional (18:30)',
    'Power Flex (19:45)',
    'Karate',
    'Cierre (22:30)'
]
Miercoles = [
    'Apertura',
    'Ritmos Latinos(CG)',
    '-',
    '-',
    'Cierre',
    'Reapertura (13:30)',
    'Full Hiit (14:15)',
    '-',
    'Cierre',
    '-',
    'Reapertura',
    '-',
    'Kimax (20:30)',
    '-',
    'Cierre (22:30)'
]
Jueves = [
    'Apertura',
    '-',
    '-',
    'Cierre',
    '-',
    'Reapertura (13:30)',
    'Piernas/ABS (14:15)',
    '-',
    'Cierre',
    '-',
    'Reapertura',
    'Entrenamiento Funcional (18:30)',
    'Power Flex (19:45)',
    'Karate',
    'Cierre (22:30)'
]
Viernes = [
    'Apertura',
    'Ritmos Latinos(CG)',
    '-',
    '-',
    'Cierre',
    'Reapertura (13:30)',
    'Full Hiit (14:15)',
    '-',
    'Cierre',
    '-',
    'Reapertura',
    '-',
    'Kimax (20:30)',
    '-',
    'Cierre (22:30)'
]

def horarios_mobile() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.accordion(
            items=[
                ("Lunes", rx.chakra.center(horarios_item_mobile(Lunes))),
                ("Martes", rx.chakra.center(horarios_item_mobile(Martes))),
                ("Miercoles", rx.chakra.center(horarios_item_mobile(Miercoles))),
                ("Jueves", rx.chakra.center(horarios_item_mobile(Jueves))),
                ("Viernes", rx.chakra.center(horarios_item_mobile(Viernes))),
            ],
            width="100%",
            bg=Color.DARK_RED.value,
            allow_multiple=False,
            allow_toggle=True,
            color="white",
        )
    )
