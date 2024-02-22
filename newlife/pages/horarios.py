import reflex as rx
from newlife.views.navbar import navbar
from newlife.views.footer import footer
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles

from newlife.views.horarios_view import horarios_view

@rx.page(
    route="/horarios", title='Horarios of New Life'
)
def horarios_function() -> rx.Component:
    return rx.chakra.vstack(
        navbar('#1C1C1A'),
        horarios_view(),
        footer('#1C1C1A'),
        style=styles.BASE_STYLE,
        
    )
