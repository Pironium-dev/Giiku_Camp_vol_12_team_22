import reflex as rx
from rxconfig import config

class AppState(rx.State):
    generated_name = ''
    selected_hobby = ''
    selected_prefecture = ''  # 選択された都道府県を格納する変数

    def generate_team_name(self):
        pass

class UIHelper:
    """共通のUI要素を作成するヘルパークラス"""

    @staticmethod
    def create_button(text, href=None, bg="blue.600", font_size="1.5em"):
        """共通のボタンスタイルを適用する"""
        button = rx.button(
            text,
            bg=bg,
            color="white",
            padding="1em 2em",
            font_size=font_size,
            border_radius="full",
            box_shadow="0px 4px 15px rgba(0, 0, 0, 0.3)",
            transition="transform 0.2s ease, background-color 0.2s ease",
            _hover={"bg": "blue.500", "transform": "scale(1.05)"},
            _active={"bg": "blue.700", "transform": "scale(1.05)"}
        )
        return rx.link(button, href=href) if href else button

    @staticmethod
    def create_page_heading(text, margin_bottom="0.5em"):
        """ページの見出しを作成する"""
        return rx.heading(
            text,
            font_size="4em",
            margin_bottom=margin_bottom,
            color="white",
            text_transform="uppercase",
            letter_spacing="wider",
            text_shadow="2px 2px 4px rgba(0, 0, 0, 0.5)"
        )

    @staticmethod
    def create_text(text, font_size="1.5em"):
        """共通のテキストスタイルを適用する"""
        return rx.text(
            text,
            font_size=font_size,
            margin_bottom="2em",
            color="white",
            text_align="center"
        )

    @staticmethod
    def create_rule_box(text, heading="ルール"):
        """共通のルールボックスを作成する"""
        return rx.box(
            rx.vstack(
                rx.heading(
                    heading,
                    font_size="1.5em",
                    color="black",
                    text_align="center",
                    margin_bottom="0.5em"
                ),
                rx.text(
                    text,
                    font_size="1.2em",
                    color="black",
                    text_align="center",
                    padding="0.5em 0"
                ),
            ),
            border="2px solid black",
            border_radius="8px",
            margin_top="2em",
            bg="white",
            padding="1em"
        )

# Prefecture list
prefectures = [
    '北海道、東北', '関東', '中部', '関西', '中国、四国', '九州']

def index1() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                UIHelper.create_page_heading("チーム名生成アプリ"),
                UIHelper.create_text("ボタンをクリックして、あなたのチーム名を生成しましょう！"),
                UIHelper.create_button("スタート", href="/index2", font_size="2em"),
                UIHelper.create_rule_box(""),
            ),
        ),
        padding="4em",
        height="100vh",
        bg="linear-gradient(to right, #4facfe, #00f2fe)",
    )

def index2() -> rx.Component:
    adjectives = ['C', 'Python', 'JAVA', 'JAVASCRIPT', 'GO']
    
    return rx.container(
        rx.center(
            rx.vstack(
                UIHelper.create_page_heading("使用言語を選択してください"),
                UIHelper.create_text("以下の選択肢から使用言語を選んでください。"),
                rx.hstack(
                    *[UIHelper.create_button(adjective) for adjective in adjectives],
                    spacing="1em"
                ),
                UIHelper.create_button("次へ", href="/index3", font_size="2em"),
                UIHelper.create_button("最初に戻る", href="/index1", bg="gray.600"),
                UIHelper.create_rule_box(""),
            ),
        ),
        padding="4em",
        height="100vh",
        bg="linear-gradient(to right, #4facfe, #00f2fe)",
    )

def index3() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                UIHelper.create_page_heading("地方を選択してください"),
                UIHelper.create_text("以下の選択肢から地方を選んでください。"),
                rx.hstack(
                    *[UIHelper.create_button(prefecture) for prefecture in prefectures],
                    spacing="1em",
                    wrap="wrap",
                    justify="center"
                ),
                UIHelper.create_button("生成", href="/index4", font_size="3em"),
                UIHelper.create_button("戻る", href="/index2", font_size="2em"),
                UIHelper.create_button("最初に戻る", href="/index1", bg="gray.600"),
                UIHelper.create_rule_box("地方を選択したら、戻るボタンをクリッしてください！"),
            ),
        ),
        padding="4em",
        height="100vh",
        bg="linear-gradient(to right, #4facfe, #00f2fe)",
    )
    
def index4() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                UIHelper.create_page_heading("チーム名生成アプリ"),
                UIHelper.create_text("ボタンをクリックして、あなたのチーム名を生成しましょう！"),
                UIHelper.create_button("スタート", href="/index2", font_size="2em"),
                UIHelper.create_rule_box(""),
            ),
        ),
        padding="4em",
        height="100vh",
        bg="linear-gradient(to right, #4facfe, #00f2fe)",
    )


app = rx.App()
app.add_page(index1, route="/index1")
app.add_page(index2, route="/index2")
app.add_page(index3, route="/index3")
app.add_page(index3, route="/index4")

