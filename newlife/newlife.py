import reflex as rx
import newlife.styles.styles as styles

# Import pages newlife
from newlife.pages.index import index_function
from newlife.pages.horarios import horarios_function
from newlife.pages.actividades import actividades_function
from newlife.pages.instalaciones import instalaciones_function
from newlife.pages.farmacologia import farmacologia_function


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,    
)


