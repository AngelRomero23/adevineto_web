import reflex as rx
import wep_app.constants as constants
from wep_app.styles.styles import Size, Color
from wep_app.components.link_icon import link_icon

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src='mouredev.png',
                alt='Imagen pixel art de MoureDev con estilo navideño.',
                width=Size.VERY_BIG.value,
                height=Size.VERY_BIG.value
            ),
            rx.text('aDevineto 2024'),
            rx.spacer(),
            rx.flex(
                link_icon(
                'youtube',
                constants.YOUTUBE_URL
                ),
                link_icon(
                'twitch',
                constants.TWITCH_URL
                ),
                link_icon(
                'github',
                constants.GITHUB_URL
                ),
                spacing='1rem' 
            ),
            width = '100%',
            align='center',
            flex_wrap="wrap"  
        ),
        bg=Color.PRIMARY.value,
        position='sticky',
        border_bottom=f'0.25em solid {Color.SECONDARY.value[0]}',
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        zIndex='999',
        top='0',
        width ='100%'
    )  
    

