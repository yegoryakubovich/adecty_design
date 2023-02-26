#
# (c) 2022, Yegor Yakubovich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from adecty_design.functions import properties_css_get
from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Margin, Padding, Color, Font
from adecty_design.widgets.text import Text
from adecty_design.widgets.vector import Vector


class ButtonType:
    default = 'default'
    chip = 'chip'


class Button:
    type: str
    url: str
    icon: Vector
    text: Text | str
    margin: Margin
    padding: Padding
    color_background: Color

    def __init__(
            self,
            url: str,
            text: Text | str,
            type: str = None,
            icon: Vector = None,
            margin: Margin = None,
            padding: Padding = None,
            color_background: Color = None,
    ):
        self.type = type
        self.url = url
        self.icon = icon
        self.text = text
        self.margin = margin
        self.padding = padding
        self.color_background = color_background

    def html_get(self, **kwargs):
        if not self.type:
            self.type = ButtonType.default

        if type(self.text) is str:
            self.text = Text(
                text=self.text,
                margin=Margin(left=6 if self.icon else 0),
                font=Font(
                    color=kwargs.get('colors').text,
                    weight=700,
                ),
            )

        if not self.margin:
            if self.type == ButtonType.default:
                self.margin = Margin(horizontal=8)
            elif self.type == ButtonType.chip:
                self.margin = Margin()

        if not self.padding:
            if self.type == ButtonType.default:
                self.padding = Padding(horizontal=12, vertical=24)
            elif self.type == ButtonType.chip:
                self.padding = Padding(horizontal=6, vertical=16)

        if not self.color_background:
            if self.type == ButtonType.default:
                self.color_background = Color(color=kwargs.get('colors').background)
            elif self.type == ButtonType.chip:
                self.color_background = Color(color=kwargs.get('colors').background_secondary)

        text_html = self.text.html_get(**kwargs)
        icon_html = self.icon.svg_get(height=10) if self.icon else ''

        if self.type == ButtonType.default:
            properties_css = properties_css_get(
                properties=[self.margin, self.padding, self.color_background],
                properties_additional='cursor: pointer;border: 2px solid {border_color};'
                                      'border-radius: var(--rounding);'.format(
                    border_color=kwargs.get('colors').primary,
                ),
            )
            button_html = MarkupsHtml.button_default.format(
                properties_css=properties_css,
                url=self.url,
                icon_html=icon_html,
                text_html=text_html,
            )
            return button_html
        elif self.type == ButtonType.chip:
            properties_css = properties_css_get(
                properties=[self.margin, self.padding, self.color_background],
                properties_additional='cursor: pointer;border: 0;border-radius: 100px;display: flex;'
                                      'width: fit-content;align-items: center;',
            )
            button_html = MarkupsHtml.button_chip.format(
                properties_css=properties_css,
                url=self.url,
                icon_html=icon_html,
                text_html=text_html,
            )
            return button_html
