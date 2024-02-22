import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.item_desktop import item_desktop

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


def card_tittle(dia):
    return rx.chakra.flex(
        rx.chakra.vstack(
            rx.chakra.hstack(
                rx.text(
                    dia,
                    margin_top=Size.SMALL.value,
                    font_size=Size.DEFAULT.value,
                    font_weight='bold',
                ),
                margin_x=Size.SMALL.value,

            ),
        ),
        width="14.3em",
        height="4em",
        display='flex',
        justify_content='center',
        text_aling='center',
        align_items='center',

    )


def title():
    return rx.chakra.hstack(
        rx.chakra.vstack(
            rx.chakra.hstack(
                rx.image(
                src='/icons/calendar.svg',
                width='1.3em',
            ),
                
            ),
        ),
        card_tittle('Lunes'),
        card_tittle('Martes'),
        card_tittle('Miercoles'),
        card_tittle('Jueves'),
        card_tittle('Viernes'),

        # width="100em",
        display='flex',
        justify_content='space-around',
        text_aling='center',
        align_items='center',
        bg=Color.PRIMARY.value,
        border_bottom=f'solid 2px {Color.WHITE.value}',
        color="white",
        position='sticky',
        z_index='999',
        top='0',
        width='100%',

    )


def function(horario, lun, mar, mie, jue, vie):
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.hstack(
                rx.text(horario),
            ),
            display='flex',
            justify_content='center',
            text_aling='center',
            align_items='center',
        ),
        item_desktop(lun),
        item_desktop(mar),
        item_desktop(mie),
        item_desktop(jue),
        item_desktop(vie),


        # width="80em",
        width='100%',

        display='flex',
        justify_content='space-around',
        bg=Color.PRIMARY.value,
        color="white",

    )


def horarios_desktop() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            title(),
            function('08:00', Lunes[0], Martes[0],
                     Miercoles[0], Jueves[0], Viernes[0]),
            function('09:00', Lunes[1], Martes[1],
                     Miercoles[1], Jueves[1], Viernes[1]),
            function('10:00', Lunes[2], Martes[2],
                     Miercoles[2], Jueves[2], Viernes[2]),
            function('11:00', Lunes[3], Martes[3],
                     Miercoles[3], Jueves[3], Viernes[3]),
            function('12:00', Lunes[4], Martes[4],
                     Miercoles[4], Jueves[4], Viernes[4]),
            function('13:00', Lunes[5], Martes[5],
                     Miercoles[5], Jueves[5], Viernes[5]),
            function('14:00', Lunes[6], Martes[6],
                     Miercoles[6], Jueves[6], Viernes[6]),
            function('15:00', Lunes[7], Martes[7],
                     Miercoles[7], Jueves[7], Viernes[7]),
            function('16:00', Lunes[8], Martes[8],
                     Miercoles[8], Jueves[8], Viernes[8]),
            function('17:00', Lunes[9], Martes[9],
                     Miercoles[9], Jueves[9], Viernes[9]),
            function('18:00', Lunes[10], Martes[10],
                     Miercoles[10], Jueves[10], Viernes[10]),
            function('19:00', Lunes[11], Martes[11],
                     Miercoles[11], Jueves[11], Viernes[11]),
            function('20:00', Lunes[12], Martes[12],
                     Miercoles[12], Jueves[12], Viernes[12]),
            function('21:00', Lunes[13], Martes[13],
                     Miercoles[13], Jueves[13], Viernes[13]),
            function('22:00', Lunes[14], Martes[14],
                     Miercoles[14], Jueves[14], Viernes[14]),
            width='100%',

        ),
        width='100%',

    )
