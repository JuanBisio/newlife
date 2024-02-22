import reflex as rx
from newlife.styles.styles import Color, Size, Font

from newlife.components.target_time import target_time


def horarios_item_mobile(actividad) -> rx.Component:
    return rx.chakra.flex(
        target_time('08:00', actividad[0]),
        target_time('09:00', actividad[1]),
        target_time('10:00', actividad[2]),
        target_time('11:00', actividad[3]),
        target_time('12:00', actividad[4]),
        target_time('13:00', actividad[5]),
        target_time('14:00', actividad[6]),
        target_time('15:00', actividad[7]),
        target_time('16:00', actividad[8]),
        target_time('17:00', actividad[9]),
        target_time('18:00', actividad[10]),
        target_time('19:00', actividad[11]),
        target_time('20:00', actividad[12]),
        target_time('21:00', actividad[13]),
        target_time('22:00', actividad[14]),
        direction='column',
    )
