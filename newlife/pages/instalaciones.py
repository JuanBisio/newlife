import reflex as rx
import newlife.styles.styles as styles

from newlife.views.navbar import navbar
from newlife.views.footer import footer
from newlife.styles.styles import Color, Size, Font
from newlife.views.instalaciones_view import instalaciones_view


@rx.page(
    route="/instalaciones",
    title='instalaciones of New Life'
)
def instalaciones_function() -> rx.Component:
    return rx.chakra.vstack(
        navbar('#1C1C1A'),
        instalaciones_view(),
        footer('#1C1C1A'),
        style=styles.BASE_STYLE,

    )
