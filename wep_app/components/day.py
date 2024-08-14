import reflex as rx
from wep_app.styles.styles import Size, Color


def day(number: int, image: str = 'gift.png', url: str = '',) -> rx.Component:
    return rx.box(
        rx.cond(
            url != '',
            rx.link(
                rx.image(
                    src=image,
                    alt=f'Regalo asociado al dia {number}'
                ),
                href=url,
                is_external=True,
                class_name='container-gifts'
            )
        ),
        rx.cond(
            url == '',
                rx.image(
                    src=image,
                    alt=f'Regalo asociado al dia {number}',
                    class_name='container-gifts'
            ) 
        ),
        rx.text(
            number,
            padding=Size.DEFAULT.value,
            position='absolute'
        ),
        bg=Color.ACCENT.value,
        width='100%',
        aspect_ratio='1',
        position='relative'
        
    )