import reflex as rx
from newlife.styles.styles import Color, Size, Font
import newlife.styles.styles as styles
from newlife.components.actividades_component import actividad


def actividades_view() -> rx.Component:
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(
                'ACTIVIDADES',
                size='xl',
                color=Color.DARK_RED.value,
                margin=Size.SMALL.value,
                font_family=Font.SUBTITLE.value,
            ),
            actividad('/activity/Compress1.webp', 'Cardio/Local', 'Esta actividad es para mejorar la condición física, está destinada a personas con entrenamientos de media intensidad. Se realizan trabajos intermitentes, coordinativos durante 30 minutos y 15 minutos con trabajos de fuerza y resistencia muscular. Objetivo condición física, tonicidad y fuerza.', 'row'),
            actividad('/activity/Compress2.webp', 'Kimax', 'KI MAX ® se practica con una bolsa de pie exclusivamente diseñada, con guantes para pegar a la bolsa. (Traer vendas y/o guantes) Los “Rounds” de KI MAX ® implementan técnicas de Boxeo, Muay Thai y Kickboxing a través de combinaciones simples, intensas y dinámicas.'),
            actividad('/activity/Compress3.webp', 'Full Hiit', 'Esta actividad es para mejorar la condición física, está destinada a personas con entrenamientos de media y alta intensidad. Se realizan trabajos intermitentes, coordinativos, intensivos. (Trabajamos Fuerza, Potencia y Resistencia)', 'row'),
            actividad('/activity/Compress4.webp', 'Entrenamiento Funcional', 'La clase te brinda la posibilidad de mejorar y mantener tu nivel de fitness y entrenar utilizando entrenamientos muy simples e intensos, basados en Circuitos y bandas de Suspensión. En 45 minutos te ofrecemos una propuesta que se adapta a tu ritmo de vida actual con resultados reales'),
            actividad('/activity/Compress5.webp', 'Piernas/Abdominales',
                      'Esta clase está basada en trabajos de fuerza y resistencia muscular, de tren inferior, utilizando variedad de elementos con movimientos coordinativos moderados. Objetivo tonicidad y fuerza.', 'row'),
            actividad('/activity/Compress6.webp', 'Ritmos Latinos', 'Ven a divertirte y pasar un buen día bailando con esta propuesta pensada para todo público. Quema calorías, fortalece tus huesos, reduce tu estrés y ansiedad y pasa un momento agradable junto a grupo que comparte la misma pasión que tú. ¡Si todavía no bailas, nada te impide hacerlo!'),
            actividad('/activity/Compress7.webp', 'Piernas/Gluteos',
                      'Esta clase está basada en trabajos de fuerza y resistencia muscular de tren inferior, utilizando variedad de elementos, con movimientos coordinativos moderados. Objetivo tonicidad y fuerza. ', 'row'),
            actividad('/activity/Compress8.webp', 'Power Flex', 'Esta actividad está orientada a realizar ejercicios de flexibilidad progresivos, con dos clases semanales será suficiente para que puedas ir viendo tus avances y te sientas cada vez más ágil y con mayor movilidad. Ven con ropa cómoda y prepárate para una nueva vida.'),
            actividad('/activity/Compress9.webp', 'Karate', 'El karate es un arte marcial de origen japonés que consiste en la defensa personal. Su práctica tiene beneficios a nivel físico y mental. La disciplina es un elemento esencial para practicar karate. Aprende una nueva filosofía de vida. Clases para niños, adolescentes y adultos', 'row'),
            actividad('/activity/Compress10.webp', 'Power', 'Esta clase es ideal para tonificar todo cuerpo, se trabaja con barras y discos, se enfoca en fuerza y resistencia, disfrutaras de buena música y coreografías progresivas para lograr tus objetivos.'),
            actividad('/activity/Compress11.webp', 'Musculación','Trabajamos segun los objetivos y necesidades de casa persona, realizamos analisis de la composicion corporal para realizar la planificacion del entrenamiento y control mensual. ', 'row'),
            actividad('/activity/Compress12.webp', 'Fight Do', 'FIGHT DO ® es una lucha imaginaria contra varios oponentes, combinando lo mejor del Box y de las Artes Marciales. Golpes, rodillazos, patadas, bloqueos y saltos a la soga brindan una clase divertida y efectiva proporcionando un entrenamiento de combate muy simple, dinámico e intenso que asegura por sesión un gasto calórico de entre 600 y 700 calorías, libera estrés y tonifica todo el cuerpo.'),


            max_width='1200px',
            padding=Size.BIG.value,
        ),
        bg=Color.PRIMARY.value,
    )
