import reflex as rx
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor
import wep_app.constants as constants


def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                'Calendario de aDeviento 2023',
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value
            ),
            rx.link(
                "Creado con ",
                rx.text(class_name='nes-icon is-small heart'),
                " (y gracias a ti) por MoureDev by Brais Moure",
                href=constants.MOUREDEV_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value,
                class_name='hover-link'
            ),
            align_items='start',
            spacing=Size.MEDIUM.value
        ),rx.spacer(),
        rx.image(
            src='logo.png',
            alt='Logo Mouredev. Una letra "m" entre dos corchetes.',
            class_name='nes-avatar is-large'
        ),
        padding_botton=Size.BIG.value,
        align_items='center',
        style=styles.max_width_style
    )