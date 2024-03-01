import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles

txt = """Lo primero que hay que hacer antes de entrar en la sauna es darse un baño o una ducha de aguar fria/tibia. No se debe olvidar que el objetivo de la sauna no es la higiene, sino que se trata de un tratamiento terapéutico. Por ello, al interior de la sauna se debe llegar limpio.

Al interior de la sauna se accede con una toalla. Esta toalla se coloca doblada sobre uno de los bancos de madera y el usuario se sienta sobre la toalla. Este gesto tiene una doble finalidad. Por un lado, evita que el usuario se pueda quemar, ya que la madera de los bancos está caliente, además sentarse directamente sobre esta puede ser incómodo. Por otro lado, asegura la higiene para los demás usuarios, ya que evita que varias personas se sienten directamente sobre la misma superficie.

Paralelamente, aunque hay personas que prefieren entrar en la sauna finlandesa con la piel mojada, lo más aconsejable es hacerlo con la piel seca. De esta forma, se favorece la sudoración y la eliminación de toxinas.

De media, lo más común es permanecer en el interior de la sauna en torno a unos 15 minutos. Sin embargo, no es una costumbre inalterable, puesto que algunas personas pueden estar solo 5 o 10 minutos, mientras que otras pueden alargar su estancia hasta los 20 minutos, pero este debe ser el máximo.

Verter agua sobre las piedras aumenta la humedad en la habitación y la sensación de temperatura más alta, pero baja la temperatura del sauna. 

Al salir de la sauna finlandesa, se recomienda enfriar la piel. Esto se puede hacer dándose una ducha de agua fría. Lo más aconsejable es realizarlo poco a poco, empezando por los pies e ir ascendiendo de forma paulatina. Después, se puede volver al interior de la sauna y repetir el proceso completo hasta un máximo de dos veces.

"""


def sauna_view() -> rx.Component:
    return rx.chakra.center(
        rx.box(
            rx.vstack(
                rx.box(
                    rx.image(src='/sauna/sauna.png', width='100%',),
                    height='25em',
                    width='25em'
                ),
                rx.box(
                    rx.image(src='/sauna/saunaLogo.png', width='100%',),
                    height='20em',
                    width='25em'
                ),

            ),
            rx.vstack(
                rx.chakra.heading(
                    '¿Cómo se hace?',
                    size='xl',
                    color=Color.DARK_RED.value,
                    margin_top=Size.DEFAULT.value,
                    font_family=Font.SUBTITLE.value,
                ),
                rx.chakra.text(txt, text_aling='center',padding_bottom=Size.SMALL.value),

                color=Color.PRIMARY.value,
                text_aling='center',
                font_family=Font.DEFAULT.value,
                padding_x=Size.DEFAULT.value,
                margin_y=Size.DEFAULT.value,

            ),
            max_width='90%',
            display='flex',
            justify_content='center',
            aling_items='center',
            flex_direction=['column', 'column', 'column', 'row', 'row',]
        ),
        max_width='1200px',
    )
