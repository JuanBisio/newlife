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

txt2 = """
Sobre el sistema cardiovascular: el calor hace que aumente el ritmo cardiaco y la vasodilatación, influyendo a su vez sobre el metabolismo muscular, que se acelera.

Elimina toxinas: al abrirse los poros para eliminar el sudor se eliminan impurezas de la piel. También en el propio sudor que sale se eliminan productos de desecho como metales pesados, alcohol y nicotina.

Mejora la respiración: se despejan las vías respiratorias al hacer más fluida la mucosidad. Se ha comprobado que en personas con enfermedades respiratorias obstructivas mejoran de manera transitoria sus funciones corporales.

Influencia sobre las articulaciones: el calor, aumento de la circulación y producción de endorfinas alivia el dolor y molestias articulares.

Importancia en el deporte: ayuda a recuperar a los músculos y el organismo después del esfuerzo, ya que aumenta el riego al músculo y permite recuperarse de los procesos catabólicos sucedidos durante el ejercicio. También mejora las dolencias osteo-musculares, disminuyendo el dolor.
"""

txt3 = """
El aumento de ritmo cardiaco que se produce hace que esté desaconsejado en ancianos, embarazadas y personas con problemas de salud (hipertensión, cardiopatía, varices).

Si es la primera vez que entras no superes los 10 minutos para evitar bajadas de tensión.

También deben evitar la sauna personas que sufran de enfermedad bronquial severa, epilepsia, anorexia o cólicos renales.

Si es la primera vez que tomas una sauna hazlo siempre en compañía de alguien experimentado y no estés mucho tiempo en la sauna

Si vas a darte una sauna después de hacer ejercicio espera 15 minutos o haz un baño de agua fría para que tu temperatura descienda y así evitar un golpe de calor.

No te olvides de beber agua al salir, ya que vas a someter al cuerpo a una continua deshidratación. Y evita entrar a la sauna si tienes excesiva hambre o acabas de comer.

Al inicio sitúate en los asientos más bajos y procura tumbarte para que todo tu cuerpo esté a la misma temperatura.

Evita realizar ejercicios o hablar en exceso durante la sesión, ya que de por sí el sistema cardiaco y pulmonar están sobrecargados.

Lo habitual es salir cada 12-15 minutos de sauna para refrigerar al cuerpo con agua fría y así hacer una vasoconstricción que recuperará la presión arterial.

Antes de salir si estás tumbado incorpórate lentamente y mantén la posición de sentado durante un minuto para que la circulación se restablezca y al levantarnos no nos dé un pequeño mareo o síncope.

No es recomendable tomar más de dos sesiones semanales.
"""

def sauna_view() -> rx.Component:
    return rx.chakra.center(
        rx.box(
            rx.chakra.tabs(
                rx.chakra.tab_list(
                    rx.chakra.tab("¿Cómo se hace?"),
                    rx.chakra.tab("Beneficios"),
                    rx.chakra.tab("Precauciones"),
                ),
                rx.chakra.tab_panels(
                    rx.chakra.tab_panel(rx.chakra.text(txt)),
                    rx.chakra.tab_panel(rx.chakra.text(txt2)),
                    rx.chakra.tab_panel(rx.chakra.text(txt3)),
                ),
                bg=Color.PRIMARY.value,
                color="white",
                shadow="lg",
            ),
            # rx.vstack(
            #    rx.chakra.heading(
            #        '¿Cómo se hace?',
            #        size='xl',
            #        color=Color.DARK_RED.value,
            #        margin_top=Size.DEFAULT.value,
            #        font_family=Font.SUBTITLE.value,
            #    ),
            #    rx.chakra.text(txt, text_aling='center',padding_bottom=Size.SMALL.value),
            #
            #    color=Color.WHITE.value,
            #    text_aling='center',
            #    font_family=Font.DEFAULT.value,
            #    padding_x=Size.DEFAULT.value,
            #    margin_y=Size.DEFAULT.value,
            #
            # ),
            max_width='90%',
            display='flex',
            justify_content='center',
            aling_items='center',
            flex_direction=['column', 'column', 'column', 'row', 'row',]
        ),
        max_width='1200px',
    )
