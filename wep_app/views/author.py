import reflex as rx
import datetime
import wep_app.constants as constants
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor, Color
from wep_app.components.header_text import header_text
from wep_app.components.button import button



def author() -> rx.Component:
    return rx.vstack(
        header_text(
            'like',
            'Hola, mi nombre es  Brais Moure',
            'heading'
        ),
        rx.flex(
            rx.avatar(
                name='Brais Moure',
                src="avatar.jpg",
                radius='full'
            ),
            rx.vstack(
                rx.text.span(f'Soy ingeniero de software por más de {_experience()} años'),
                rx.text.span(
                    'En 2018 comencé a divulgar contenido sobre programación y desarrollo de software en redes sociales como ',
                    rx.text.span(
                        '@mouredev',
                        class_name='footer-user-reference'
                    ),
                    '.'    
                ),
                author_buttons(),
                width='100%',
                align_items='start'
            ),
            align_items='start',
            spacing=Size.BIG.value,
            flex_direction=['column', 'column', 'column', 'row', 'row']
        ),
        style=styles.max_width_style
    )
    
def author_buttons() -> rx.Component:
    return rx.box(
        button(
            'YouTube',
            constants.YOUTUBE_URL
        ),
        button(
            'Twitch',
            constants.TWITCH_URL
        ),
        button(
            'Discord',
            constants.DISCORD_URL
        ),
    )
    
def _experience() -> int:
    return datetime.date.today().year - 2010