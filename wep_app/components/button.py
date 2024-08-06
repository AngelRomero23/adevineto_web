import reflex as rx

def button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.html(f'<button type="button" class="nes-btn btn-nes-custom is-error">{text}</button>'),
        href=url,
        is_external=True,
        aling='center'
    )