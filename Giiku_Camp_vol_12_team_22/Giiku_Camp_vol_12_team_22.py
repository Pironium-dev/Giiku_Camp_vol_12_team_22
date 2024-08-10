import random

import reflex as rx
from rxconfig import config

## 質問により追加される単語
PYTHON_OPTIONS = (('Pythonicな',), ('蛇使いの', '空飛ぶモンティ・パイソン好きの'), ('とぐろ', 'イッツマン'))

class State(rx.State):
    generated_name = ''

    head_options = ["僕の", "駆け出し", "新しい", "大人の", "スペシャル", "動的", "ふつうの", "自称", "Dr.", "新しい"]
    middle_options = ["ヒーロー", "学校", "研究", "明太子", "虎ノ門", "Youtube", "無課金", "サッカー", "キーボード", "ライブ"]
    tail_options = ["部", ".txt", "同好会", "（仮）", "アカデミア", "中毒", "のリーダーズ", "のために", "w", "・改"]
    def generate_team_name(self):
        self._add_options_of_language('Python')
        if random.randint(0, 3) == 0:
            self.generated_name = self._choice(1) + self._choice(2)
        else:
            self.generated_name = self._choice(0) + self._choice(1) + self._choice(2)
        print(self.generated_name) ## デバッグ用
    
    def _choice(self, index):
        self._add_options_of_language('Python')
        if index == 0:
            option = random.choice(self.head_options)
        elif index == 1:
            option = random.choice(self.middle_options)
        else:
            option = random.choice(self.tail_options)
        return option

    def _add_options_of_language(self, l:str):
        match l:
            case 'Python':
                self.head_options.extend(PYTHON_OPTIONS[0])
                self.middle_options.extend(PYTHON_OPTIONS[1])
                self.tail_options.extend(PYTHON_OPTIONS[2])

def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.button('test', on_click=State.generate_team_name)
    )


app = rx.App()
app.add_page(index)