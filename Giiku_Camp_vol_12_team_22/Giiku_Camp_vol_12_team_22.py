import random

import reflex as rx
from rxconfig import config

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
        self._add_options_of_language("Python")
        if random.randint(0, 3) == 0:
            self.generated_name = self._choice(1) + self._choice(2)
        else:
            self.generated_name = self._choice(0) + self._choice(1) + self._choice(2)
        print(self.generated_name)  ## デバッグ用

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


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.button("test", on_click=State.generate_team_name),
    )


app = rx.App()
app.add_page(index)
