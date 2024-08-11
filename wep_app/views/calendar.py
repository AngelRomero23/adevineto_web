import reflex as rx
import time
import wep_app.constants as constants
import wep_app.styles.styles as styles
from wep_app.styles.styles import Size, TextColor, Color
from wep_app.components.header_text import header_text
from wep_app.components.button import button
from datetime import datetime, timezone



        
class State(rx.State):

    countdown: str

    def update_countdown(self):
        target_date = datetime(2024, 12, 31)
        now = datetime.now()
        time_left = target_date - now
        days_left = time_left.days
        hours_left = time_left.seconds // 3600
        minutes_left = (time_left.seconds % 3600) // 60
        seconds_left = time_left.seconds % 60
        self.countdown = f"{days_left} días, {hours_left} horas, {minutes_left} minutos y {seconds_left} segundos"


def calendar() -> rx.Component:
    return rx.hstack(
        header_text(
            'heart',
            'Caledario de aDEViento',
            'heading'
        ),
        rx.vstack(
            rx.hstack(
                rx.text(
                    'El evento comienza en'
                ),
                rx.text(
                    State.countdown,
                    on_mount=State.update_countdown
                )
            )
        )
    )
