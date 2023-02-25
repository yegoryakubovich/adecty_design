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


from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Properties, Margin, Padding
from adecty_design.widgets.text import Text
from adecty_design.widgets.vector import Vector


class ButtonType:
    default = 'default'
    chip = 'chip'


class Button:
    type: str
    url: str
    icon: Vector
    text: Text
    properties: Properties

    def __init__(self,
                 url: str, text: str | Text,
                 icon: Vector = None,
                 type: str = ButtonType.default,
                 properties: Properties = Properties()):
        self.type = type
        self.url = url
        self.icon = icon if icon else None
        self.text = text if not text.isalpha() else Text(text=text, properties=Properties(margin=Margin(left=6 if self.icon else 0)))

        if type == ButtonType.default:
            self.properties = Properties(
                margin=properties.margin if not properties.margin.is_empty() else
                Margin(horizontal=8),
                padding=properties.padding if not properties.padding.is_empty() else
                Padding(horizontal=12, vertical=24),
                background_color=properties.background_color if properties.background_color else
                'var(--background)',
                text_color=properties.text_color if properties.text_color else
                'var(--text)',
            )
        elif type == ButtonType.chip:
            self.properties = Properties(
                margin=properties.margin if not properties.margin.is_empty() else
                Margin(horizontal=4, right=8),
                padding=properties.padding if not properties.padding.is_empty() else
                Padding(horizontal=6, vertical=16),
                background_color=properties.background_color if properties.background_color else
                'var(--background_secondary)',
                text_color=properties.text_color if properties.text_color else
                'var(--text)',
            )

    def html_get(self, **kwargs):
        text_html = self.text.html_get(**kwargs)
        icon_html = self.icon.svg_get(height=10) if self.icon else ''

        if self.type == ButtonType.default:
            style = 'font-family: {font_css};' \
                    'font-weight: 600;' \
                    'background-color: {background_color};' \
                    'color: {color};' \
                    'margin: {margin};' \
                    'padding: {padding};' \
                    'cursor: pointer;' \
                    'border: 2px solid {border_color};' \
                    'border-radius: var(--rounding);'.format(font_css=kwargs.get('font').css,
                                                             background_color=kwargs.get('colors').background,
                                                             color=kwargs.get('colors').primary,
                                                             margin=self.properties.margin.html_get(),
                                                             padding=self.properties.padding.html_get(),
                                                             border_color=kwargs.get('colors').primary)
            button_html = MarkupsHtml.button_default
            return button_html.format(url=self.url, icon_html=icon_html, text_html=text_html, style=style)
        elif self.type == ButtonType.chip:
            button_chip = MarkupsHtml.button_chip
            style = 'font-family: {font_css};' \
                    'font-weight: 600;' \
                    'background-color: {background_color};' \
                    'color: {color};' \
                    'margin: {margin};' \
                    'padding: {padding};' \
                    'cursor: pointer;' \
                    'border: 0;' \
                    'border-radius: 100px;' \
                    'display: flex;' \
                    'width: fit-content;' \
                    'align-items: center;'.format(
                font_css=kwargs.get('font').css,
                background_color=self.properties.background_color,
                color=self.properties.text_color,
                margin=self.properties.margin.html_get(),
                padding=self.properties.padding.html_get(),
            )
            return button_chip.format(url=self.url, icon_html=icon_html, text_html=text_html, style=style)
