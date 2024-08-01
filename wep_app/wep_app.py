import reflex as rx
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size
from wep_app.views.navbar import navbar
from wep_app.views.header import header


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                header(),
                header(),
                width='100%',
                align='center',
                spacing=Size.VERY_BIG.value
            )
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
