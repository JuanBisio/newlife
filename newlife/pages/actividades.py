import reflex as rx
import newlife.styles.styles as styles

from newlife.views.navbar import navbar
from newlife.views.footer import footer
from newlife.styles.styles import Color, Size, Font
from newlife.views.actividades_view import actividades_view
from newlife.components.spacer import spacer


@rx.page(
    route="/actividades",
    title='Actividades - New Life'
)
def actividades_function() -> rx.Component:
    return rx.chakra.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar('#1C1C1A'),
        actividades_view(),
        spacer(),
        footer('#1C1C1A'),
        style=styles.BASE_STYLE,

    )
