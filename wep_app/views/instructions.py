import reflex as rx
import wep_app.styles.styles as styles
from wep_app.components.button import button
from wep_app.styles.styles import Size, TextColor
import wep_app.constants as constants


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                '¿Como funciona el evento?',
                class_name='title',
                color=TextColor.ACCENT.value
            ),
            rx.text.span(
                '• Del 1 al 24 de diciembre descubriré cada día un nuevo regalo en el calendario.'
            ),
            rx.text.span('• Puedes participar desde cualquier parte del mundo.'),
            rx.text.span('• Sólo tendrás que hacer Retweet a la publicación que enlazaré desde esta web. Tu cuenta de Twitter/X tiene que ser pública.'),
            button(
                'Twitter',
                constants.TWITTER_URL
                ),
            rx.text.span('• Al día siguiente realizaré el sorteo de forma pública y compartiré el ganador en la web y en Twitter/X.'),
            button(
                'Twitch',
                constants.TWITCH_URL,
                ),
            rx.text.span('• ¡Vuelta a empezar! Publicaré un nuevo regalo y comenzará de nuevo el proceso.'),
            class_name='nes-container is-dark with-title',
            align_items='start',
            width='100%'
            
        ),
        style=styles.max_width_style
    )