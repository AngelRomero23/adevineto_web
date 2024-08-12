import asyncio
import datetime
import time
import reflex as rx


class MyTaskState(rx.State):
    dias: int = 0
    horas: int = 0
    minutos: int = 0
    segundos: int = 0
    formatted_time: str
    time_delta: int = 0
    running: bool = True
    _n_tasks: int = 0

    @rx.var
    def get_time_remaining(self):
        now = datetime.datetime.now()
        event_datetime = datetime.datetime(2024, 12, 31, 23, 59, 59)
        self.time_delta = event_datetime - now
        days, seconds = divmod(self.time_delta.seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        self.dias = self.time_delta.days 
        self.horas= hours 
        self.minutos = minutes 
        self.segundos = seconds
        self.formatted_time = f"{self.dias:02d}d:{self.horas:02d}h:{self.minutos:02d}m:{self.segundos:02d}s"
        
    @rx.background
    async def my_task(self):
        async with self:
            # The latest state values are always available inside the context
            if self._n_tasks > 0:
                # only allow 1 concurrent task
                return

            # State mutation is only allowed inside context block
            self._n_tasks += 1

        while True:
                async with self:
                    # Check for stopping conditions inside context
                    if self.dias <= 0 and self.horas <= 0 and self.minutos <= 0 and self.segundos <= 0:
                        self.formatted_time = "¡Comienza el calendario de aDEViento"
                        self.running = False
                    if not self.running:
                        self._n_tasks -= 1
                        return
                    
                    self.segundos -= 1


                    if self.segundos < 0:
                        self.segundos = 59
                        self.minutos -= 1

                    if self.minutos < 0:
                        self.minutos = 59
                        self.horas -= 1

                    if self.horas < 0:
                        self.horas = 23
                        self.dias -= 1

                    self.formatted_time = f"{self.dias:02d}d:{self.horas:02d}h:{self.minutos:02d}m:{self.segundos:02d}s"

                await asyncio.sleep(0.5)
    


                
        
    def toggle_running(self):
    
        if self.running:
            return MyTaskState.my_task

def background_task():
    
    return rx.text(MyTaskState.formatted_time,
                on_mount=MyTaskState.toggle_running)
            

        

