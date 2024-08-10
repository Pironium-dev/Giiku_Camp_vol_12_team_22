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
    #タイトル画面
    return rx.container(
        rx.vstack(
            rx.heading("チーム名生成アプリ"),
            rx.text("作チャレンジャーズ"),
            rx.color_mode.button(position="top-right"),
            rx.link(
            rx.button("開始する", bg="blue", color="white", padding="0.5em 1em", margin_top="2em"),
                href="/index2"
            ),
        ),
        padding="2em"
    )

def index2() -> rx.Component:
    #メイン画面
    return rx.container(
        rx.vstack(
            rx.heading("チーム名生成アプリ"),
            rx.text("ボタンをクリックするとチーム名を生成します:"),
            rx.button("生成", on_click=State.generate_team_name),
            rx.link(
            rx.button("戻る", bg="red", color="white", padding="0.5em 1em", margin_top="2em"),
                href="/"
            ),
            rx.text(State.generated_name, font_size="2em", margin_top="1em"),

            rx.color_mode.button(position="top-right"),
        ),
        padding="2em"
    )



app = rx.App()
app.add_page(index, route="/index")
app.add_page(index2, route="/index2")