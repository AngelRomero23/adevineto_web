import reflex as rx
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size
from wep_app.components.github import github
from wep_app.views.navbar import navbar
from wep_app.views.header import header
from wep_app.views.instructions import instructions
from wep_app.views.footer import footer
from wep_app.views.author import author
from wep_app.views.partners import partners
from wep_app.views.calendar import calendar


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.script(src='/js/snow.js'),
        rx.center(
            rx.vstack(
                header(),
                instructions(),
                calendar(),
                author(),
                partners(),
                footer(),
                github(),
                width='100%',
                align='center',
                spacing=Size.VERY_BIG.value
            ),
        )
        
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)


app.add_page(
    index,
    title = 'Calendario de aDEViento 2023 | 24 días. 24 regalos.',
    description = 'Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra comunidad de developers! Del 1 al 24 de diciembre'
)

app._compile()
