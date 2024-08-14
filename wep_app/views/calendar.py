import reflex as rx
import wep_app.constants as constants
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor, Color
from wep_app.components.header_text import header_text
from wep_app.components.button import button
from wep_app.components.countdown import background_task
from wep_app.components.day import day    



def calendar() -> rx.Component:
    return rx.hstack(
        header_text(
            'heart',
            'Caledario de aDEViento',
            'heading'
        ),
        rx.vstack(
            rx.hstack(
                rx.text('El evento comienza en'),
                background_task()
            ),
            button(
                'Recordar',
                constants.DISCORD_EVENT_URL
            ),
            rx.text.span(
                "• Los regalos son sorpresa, permanecerán ocultos hasta el día de su publicación. No olvides pasarte por aquí cada día para descubrir un nuevo sorteo."
            ),
            rx.text.span(
                "• Puedes seleccionar cada regalo para conocer a los ganadores una vez se haya publicado el nuevo sorteo (aparecerá en rojo)."
            ),
            class_name='nes-container is-dark' 
        ),
        rx.grid(
            rx.foreach(
                list(range(1,25)), 
                lambda number:
                day(
                    number
                )
            ),
            columns=rx.breakpoints(initial="3",xs='3', sm="4",md='5', lg="6"),
            spacing=Size.DEFAULT.value,
            class_name='grid-container'
        ),
        style=styles.max_width_style,
        class_name='calendar-container'
    )
