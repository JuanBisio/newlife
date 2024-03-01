import reflex as rx

from newlife.styles.styles import Color, Size, Font
from newlife.components.item_desktop import item_desktop
import newlife.horarios_constanst as c


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
                    src='/iconsImage/calendar.webp',
                    width='1.3em',
                ),

            ),
        ),
        card_tittle('Lunes'),
        card_tittle('Martes'),
        card_tittle('Miercoles'),
        card_tittle('Jueves'),
        card_tittle('Viernes'),
        card_tittle('Sabado'),

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


def function(horario, lun, mar, mie, jue, vie, sab):
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
        item_desktop(sab),

        width='100%',
        display='flex',
        justify_content='space-around',
        bg=Color.PRIMARY.value,
        color="white",
        border_bottom='solid 2px #2e2e2ecc',
    )


def horarios_desktop() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            title(),
            function('08:00', c.LUNES[0], c.MARTES[0], c.MIERCOLES[0],
                     c.JUEVES[0], c.VIERNES[0], c.SABADO[0]),
            function('09:00', c.LUNES[1], c.MARTES[1], c.MIERCOLES[1],
                     c.JUEVES[1], c.VIERNES[1], c.SABADO[1]),
            function('10:00', c.LUNES[2], c.MARTES[2], c.MIERCOLES[2],
                     c.JUEVES[2], c.VIERNES[2], c.SABADO[2]),
            function('11:00', c.LUNES[3], c.MARTES[3], c.MIERCOLES[3],
                     c.JUEVES[3], c.VIERNES[3], c.SABADO[3]),
            function('12:00', c.LUNES[4], c.MARTES[4], c.MIERCOLES[4],
                     c.JUEVES[4], c.VIERNES[4], c.SABADO[4]),
            function('13:00', c.LUNES[5], c.MARTES[5], c.MIERCOLES[5],
                     c.JUEVES[5], c.VIERNES[5], c.SABADO[5]),
            function('14:00', c.LUNES[6], c.MARTES[6], c.MIERCOLES[6],
                     c.JUEVES[6], c.VIERNES[6], c.SABADO[6]),
            function('15:00', c.LUNES[7], c.MARTES[7], c.MIERCOLES[7],
                     c.JUEVES[7], c.VIERNES[7], c.SABADO[7]),
            function('16:00', c.LUNES[8], c.MARTES[8], c.MIERCOLES[8],
                     c.JUEVES[8], c.VIERNES[8], c.SABADO[8]),
            function('17:00', c.LUNES[9], c.MARTES[9], c.MIERCOLES[9],
                     c.JUEVES[9], c.VIERNES[9], c.SABADO[9]),
            function('18:00', c.LUNES[10], c.MARTES[10], c.MIERCOLES[10],
                     c.JUEVES[10], c.VIERNES[10], c.SABADO[10]),
            function('19:00', c.LUNES[11], c.MARTES[11], c.MIERCOLES[11],
                     c.JUEVES[11], c.VIERNES[11], c.SABADO[11]),
            function('20:00', c.LUNES[12], c.MARTES[12], c.MIERCOLES[12],
                     c.JUEVES[12], c.VIERNES[12], c.SABADO[12]),
            function('21:00', c.LUNES[13], c.MARTES[13], c.MIERCOLES[13],
                     c.JUEVES[13], c.VIERNES[13], c.SABADO[13]),
            function('22:00', c.LUNES[14], c.MARTES[14], c.MIERCOLES[14],
                     c.JUEVES[14], c.VIERNES[14], c.SABADO[14]),
            width='100%',
        ),
        width='100%',

    )
