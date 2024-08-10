import random

import reflex as rx
from rxconfig import config


class State(rx.State):
    generated_name = ''

    head_options = []
    middle_options = []
    tail_options = []

    def generate_team_name(self):
        if random.randint(0, 3) == 0:
            self.generated_name = self._choice(1) + self._choice(2)
        else:
            self.generated_name = self._choice(0) + self._choice(1) + self._choice(2)
        print(self.generated_name) ## デバッグ用
    
    def _choice(self, index):
        if index == 0:
            option = random.choice(self.head_options)
        elif index == 1:
            option = random.choice(self.middle_options)
        else:
            option = random.choice(self.tail_options)
            print(option)

        return option


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
    )


app = rx.App()
app.add_page(index)