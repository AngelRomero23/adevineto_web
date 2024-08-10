import reflex as rx
from wep_app.styles.styles import Size


def header_text(icon: str, text: str, class_name: str,) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f'nes-icon is-medium {icon}'    
        ),
        rx.heading(
            text,
            size='4'
        ),align='center',
        spacing=Size.DEFAULT.value,
        padding_bottom=Size.MEDIUM.value,
        class_name=class_name
    )
    