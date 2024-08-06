import reflex as rx
from wep_app.styles.styles import Size


def header_text(icon: str, text: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            class_name=f'nes-icon is-medium {icon}'    
        ),
        rx.heading(
            text,
            size='md'
        ),
        spacing=Size.DEFAULT.value,
        padding_bottom=Size.MEDIUM
    )