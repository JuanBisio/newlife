import reflex as rx
import newlife.styles.styles as styles

from newlife.views.navbar import navbar

from newlife.views.header import header
from newlife.views.about_us import about_us
from newlife.views.galery import galery
from newlife.views.cards import cards
from newlife.views.parrax import parrax
from newlife.views.branding import branding
from newlife.views.grid_galery import grid_galery
from newlife.views.footer import footer
from newlife.views.form import form
from newlife.views.registration_form import registration_form

from newlife.components.spacer import spacer
from newlife.components.maps import maps
from newlife.components.ant_components import carrousel_antd


@rx.page(
    route="/",
    title='New Life',
    description='Brindamos propuestas de entrenamiento según objetivos y necesidades a personas que buscan bienestar y salud. Maria Olguin 1324, Río Cuarto 5800.',
    image='/icons/newlife.png',
)
def index_function() -> rx.Component:
    return rx.chakra.box(
        navbar('#1C1C1A'),
        header('#1C1C1ACC'),
        about_us(),
        spacer(),
        galery(),
        spacer(),
        grid_galery(),
        spacer(),
        registration_form(),
        spacer(),
        maps(),
        # branding(),
        spacer(),
        form(),
        spacer(),
        footer('#1C1C1A'),
        # cards(),

        style=styles.BASE_STYLE,

    )
