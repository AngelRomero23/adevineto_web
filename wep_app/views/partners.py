import reflex as rx
import wep_app.constants as constants
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor, Color
from wep_app.components.header_text import header_text
from wep_app.components.button import button


def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            header_text(
                'star',
                'patrocinado por',
                'heading-container-author'
            ),
            rx.text(
                'Con el apoyo de la comunidad y los patrocinadores costearé los 24 regalos. Imaginate tu logo aqui y en todas las comunicaciones diarias durante el evento.'
            ),
            rx.text.span(
                '¿Quieres apoyar esta iniciativa? Escribeme a braismoure@mouredev.com o enviame un mensaje en redes sociales ¡Gracias!'
            ),
            class_name='container',
            style=styles.max_width_style
            
        ),
        class_name='partners-color'
    )