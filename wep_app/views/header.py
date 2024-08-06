import reflex as rx
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor
import wep_app.constants as constants


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de aDEViento 2023",
            size="lg",
            padding_bottom=Size.DEFAULT.value
            ), 
        rx.flex(
            rx.image(
                src="mouredev.png",
                alt="Imagen pixel art de MoureDev con estilo navideño.",
                width="16em",
                height="16em",
                margin_right=Size.BIG.value
            ),
            rx.vstack(
                rx.box(
                    rx.text("24 días. 24 regalos."),
                    rx.text("Del 1 al 24 de diciembre."),
                    class_name="nes-balloon from-left is-dark"
                ),
                rx.text.span(
                    "Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra ", 
                    rx.text.span('comunidad de developers',
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    '!'                    
                ),
                rx.text.span('Una actividad en la que cada día sortearé un regalo relacionado con programación y desarrollo de software (libros, cursos…).'),
                rx.text.span('Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje en comunidad.'),
                rx.link(
                    '#aDEViento2023',
                    href=constants.ADEVIENTO_HASHTAG_URL,
                    is_external=True,
                    color=TextColor.TERTIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value,
                    class_name='hover-link'
                ),
                align_items='start'
            ),
            flex_direction=['column', 'column', 'column', 'row', 'row']
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )