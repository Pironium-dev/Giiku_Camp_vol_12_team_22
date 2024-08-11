import reflex as rx
from rxconfig import config
import random


class AppState(rx.State):
    generated_name = ''
    selected_hobby = ''
    selected_prefecture = ''  # 選択された都道府県を格納する変数

## 質問により追加される単語
PYTHON_OPTIONS = (
    ("Pythonicな",),
    ("蛇使いの", "空飛ぶモンティ・パイソン好きの"),
    ("とぐろ", "イッツマン"),
)
C_OPTIONS = (("",), ("",), ("",))
JAVA_OPTIONS = (("ジャワ島生まれ",), ("コーヒー好き",), ("仮想マシン",))
JAVASCRIPT_OPTIONS = (("",), ("",), ("",))
GO_OPTIONS = (("",), ("",), ("",))

HOKKAIDO_TOHOKU_OPTIONS = (
    ("海産物系の", "しばれる", "めんこい"),
    ("木彫りの", "牛乳製の", "道産子"),
    ("熊", "シャケ", "ぼっこ", "マグロ"),
)
KANTOU_OPTIONS = (("",), ("",), ("",))
KANSAI_OPTIONS = (("",), ("",), ("",))
KYUUSYUU_OPTIONS = (("",), ("",), ("",))
THUUGOKU_SIKOKU_OPTIONS = (("",), ("",), ("",))
THUUBU_OPTIONS = (("",), ("",), ("",))
KYUSHU_OPTIONS = (("暖かい", "熊本の"), ("ハウステンボス", "マンゴー"), ("の湯", "島"))


class State(rx.State):
    generated_name = ""

    head_options = [
        "僕の",
        "駆け出し",
        "新しい",
        "大人の",
        "スペシャル",
        "新・",
        "ふつうの",
        "自称",
        "Dr.",
        "新しい",
        "しかのこ",
        "影薄め",
    ]
    middle_options = [
        "ヒーロー",
        "学校",
        "研究",
        "明太子",
        "虎ノ門",
        "Youtube",
        "無課金",
        "サッカー",
        "キーボード",
        "ライブ",
        "のこのこ",
        "寿司",
        "まんまる",
    ]
    tail_options = [
        "部",
        ".txt",
        "同好会",
        "（仮）",
        "アカデミア",
        "中毒",
        "のリーダーズ",
        "のために",
        "w",
        "・改",
        "こしたんたん",
        "エンジニア",
        "チャレンジャーズ",
    ]

    def generate_team_name(self):
        if random.randint(0, 3) == 0:
            self.generated_name = self._choice(1) + self._choice(2)
        else:
            self.generated_name = self._choice(0) + self._choice(1) + self._choice(2)

    def _choice(self, index):
        if index == 0:
            option = random.choice(self.head_options)
        elif index == 1:
            option = random.choice(self.middle_options)
        else:
            option = random.choice(self.tail_options)
        return option

    def _add_options_of_language(self, l: str):
        match l:
            case "Python":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    PYTHON_OPTIONS,
                ):
                    i.extend(j)
            case "C":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    C_OPTIONS,
                ):
                    i.extend(j)
            case "Java":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    JAVA_OPTIONS,
                ):
                    i.extend(j)
            case "JavaScript":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    JAVASCRIPT_OPTIONS,
                ):
                    i.extend(j)
            case "Go":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    GO_OPTIONS,
                ):
                    i.extend(j)

    def _add_options_of_region(self, r: str):
        match r:
            case "北海道・東北":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    HOKKAIDO_TOHOKU_OPTIONS,
                ):
                    i.extend(j)
            case "関東":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    KANTOU_OPTIONS,
                ):
                    i.extend(j)
            case "関西":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    KANSAI_OPTIONS,
                ):
                    i.extend(j)
            case "九州":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    KYUSHU_OPTIONS,
                ):
                    i.extend(j)
            case "中国・四国":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    THUUGOKU_SIKOKU_OPTIONS,
                ):
                    i.extend(j)
            case "中部":
                for i, j in zip(
                    (self.head_options, self.middle_options, self.tail_options),
                    THUUBU_OPTIONS,
                ):
                    i.extend(j)
    def do_nothing(self):
        pass

class UIHelper:
    """共通のUI要素を作成するヘルパークラス"""

    @staticmethod
    def create_button(text, href=None, bg="blue.600", font_size="1.5em", *, on_click=State.do_nothing):
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
            _active={"bg": "blue.700", "transform": "scale(1.05)"},
            on_click=on_click
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
    '北海道・東北', '関東', '中部', '関西', '中国・四国', '九州']

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
    adjectives = ['C', 'Python', 'Java', 'JavaScript', 'Go']
    
    return rx.container(
        rx.center(
            rx.vstack(
                UIHelper.create_page_heading("使用言語を選択してください"),
                UIHelper.create_text("以下の選択肢から使用言語を選んでください。"),
                rx.select(
                    adjectives,
                    placeholder="Select favorite language",
                    label="language",
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
                rx.select(
                    prefectures,
                    placeholder="Select favorite area",
                    label="area",
                ),
                UIHelper.create_button("次へ", href="/index4", font_size="3em", on_click=State.generate_team_name),
                UIHelper.create_button("戻る", href="/index2", font_size="2em"),
                UIHelper.create_button("最初に戻る", href="/index1", bg="gray.600"),
                UIHelper.create_rule_box("地方を選択したら、戻るボタンをクリックしてください！"),
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
                UIHelper.create_page_heading("チーム名生成"),
                UIHelper.create_text(State.generated_name),
                UIHelper.create_button("更新", href="/index4", font_size="3em", on_click=State.generate_team_name),
                UIHelper.create_button("最初に戻る", href="/index1", bg="gray.600"),
                UIHelper.create_rule_box("地方を選択したら、戻るボタンをクリックしてください！"),
            ),
        ),
        padding="4em",
        height="100vh",
        bg="linear-gradient(to right, #4facfe, #00f2fe)",
    )


app = rx.App()
app.add_page(index1, route="/index1")
app.add_page(index1, route="/")
app.add_page(index2, route="/index2")
app.add_page(index3, route="/index3")
app.add_page(index4, route="/index4")