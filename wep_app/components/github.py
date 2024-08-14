import reflex as rx
import wep_app.constants as constants
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor, Color
from wep_app.components.header_text import header_text
from wep_app.components.button import button
from wep_app.components.countdown import background_task
from wep_app.components.day import day    



def github() -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.vstack(
                rx.text.span(
                    'Proyecto'
                ),
                rx.text.span(
                    'en GitHub'
                ),
                class_name='nes-balloon from-right is-dark octocat-container'
            ),
            rx.box(
                rx.text.span(
                    constants.VERSION,
                    class_name='is-error'
                ),
                class_name='nes-badge'
            )
            ),
            rx.box(
                class_name='nes-octocat animate'
        ),
        href=constants.GITHUB_REPO_URL,
        is_external=True,
        class_name='githubrepo-container'
)

