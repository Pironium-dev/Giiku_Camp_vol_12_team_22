import reflex as rx
from rxconfig import config

class State(rx.State):
    generated_name = ''
    
    def generate_team_name(self):
        # 仮のチーム名を生成するロジック（ここではランダムな例を使用）
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
            rx.link(
                rx.button("Next", bg="blue", color="white", padding="0.5em 1em", margin_top="2em"),
                href="/index2"
            ),
            rx.color_mode.button(position="top-right"),
        ),
        padding="2em"
    )

    

def index2() -> rx.Component:
    # Second Page (Index2)
    return rx.container(
        rx.vstack(
            rx.heading("Team Name Generator - Step 2"),
            rx.text("This is the second page."),
            rx.color_mode.button(position="top-right"),
        ),
        padding="2em"
    )

app = rx.App()
app.add_page(index, route="/index")
app.add_page(index2, route="/index2")

