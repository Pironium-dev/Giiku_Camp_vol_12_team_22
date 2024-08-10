import reflex as rx
from rxconfig import config

class State(rx.State):
    generated_name = ''
    
    def generate_team_name(self):
        # 仮のチーム名を生成するロジック（ここではランダムな例を使用）
        #pass
        import random
        adjectives = ['Dynamic', 'Awesome', 'Creative', 'Innovative', 'Agile']
        nouns = ['Lions', 'Wolves', 'Eagles', 'Tigers', 'Sharks']
        self.generated_name = random.choice(adjectives) + " " + random.choice(nouns)

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.heading("Team Name Generator"),
            rx.text("Click the button to generate a random team name:"),
            rx.button("Generate Team Name", on_click=State.generate_team_name),
            rx.text(State.generated_name, font_size="2em", margin_top="1em"),
            rx.color_mode.button(position="top-right"),
        ),
        padding="2em"
    )
a

app = rx.App()
app.add_page(index)
