import reflex as rx
import newlife.styles.styles as styles

from newlife.views.navbar import navbar
from newlife.views.footer import footer
from newlife.views.headerSauna import headerSauna
from newlife.views.about_us_sauna import about_us_sauna
from newlife.views.sauna_view import sauna_view
from newlife.styles.styles import Color, Size, Font
from newlife.views.products import products


@rx.page(
    route="/sauna",
    title='Sauna of New Life'
)
def sauna_function() -> rx.Component:
    return rx.chakra.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar('#1C1C1A'),
        headerSauna('#1C1C1ACC'),
        about_us_sauna(),
        products(),
        sauna_view(),
        footer('#1C1C1A'),
        style=styles.BASE_STYLE_SAUNA,  
        
    )
