#
# (c) 2023, Yegor Yakubovich
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


from types import NoneType

from adecty_design.functions import properties_css_get
from adecty_design.properties import Margin, Padding, Color, Font
from adecty_design.properties.color import ColorType
from adecty_design.widgets.text import Text
from adecty_design.widgets.icon import Icon


BUTTON_DEFAULT_HTML = '<a class="button__default" href="{url}" {properties_css}>{icon_html}{text_html}</a>'
BUTTON_CHIP_HTML = '<a class="button__chip" href="{url}" {properties_css}>{icon_html}{text_html}</a>'
BUTTON_CARD_HTML = '<a class="button__card" href="{url}" {properties_css}>{icon_html}{text_html}</a>'


class ButtonType:
    default = 'default'
    chip = 'chip'


class Button:
    type: str
    url: str
    icon: Icon
    text: Text | str
    margin: Margin
    padding: Padding
    color_background: Color

    def __init__(
            self,
            url: str,
            text: Text | str = None,
            type: str = None,
            icon: Icon = None,
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

        if type(self.text) in [str, NoneType]:
            self.text = Text(
                text=self.text,
                margin=Margin(left=6 if self.icon and self.text else 0),
                font=Font(
                    weight=700,
                ),
            )

        if not self.margin:
            if self.type == ButtonType.default:
                self.margin = Margin(horizontal=0)
            elif self.type == ButtonType.chip:
                self.margin = Margin(right=8, down=6)

        if not self.padding:
            if self.type == ButtonType.default:
                self.padding = Padding(horizontal=12, vertical=24)
            elif self.type == ButtonType.chip:
                self.padding = Padding(
                    horizontal=6,
                    right=16 if self.text.text else 8,
                    left=16 if self.text.text else 0,
                )

        if not self.color_background:
            if self.type == ButtonType.default:
                self.color_background = Color(
                    color=kwargs.get('colors').background.color,
                )
            elif self.type == ButtonType.chip:
                self.color_background = Color(
                    color=kwargs.get('colors').background_secondary.color,
                )

        self.color_background.type = ColorType.background

        text_html = self.text.html_get(**kwargs)
        icon_html = self.icon.html_get(height=10, **kwargs,) if self.icon else ''

        if self.type == ButtonType.default:
            properties_css = properties_css_get(
                properties=[self.margin, self.padding, self.color_background],
                properties_additional='cursor: pointer;border: 2px solid {border_color};'
                                      'border-radius: var(--rounding);display: flex;'
                                      'width: fit-content;align-items: center;'.format(
                    border_color=kwargs.get('colors').primary.color,
                ),
            )
            button_html = BUTTON_DEFAULT_HTML.format(
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
            button_html = BUTTON_CHIP_HTML.format(
                properties_css=properties_css,
                url=self.url,
                icon_html=icon_html,
                text_html=text_html,
            )
            return button_html


class ButtonCard:
    url: str
    icon: Icon
    text: Text | str
    margin: Margin
    padding: Padding

    def __init__(
            self,
            url: str,
            text: Text | str = None,
            icon: Icon = None,
            margin: Margin = None,
            padding: Padding = None,
    ):
        self.type = type
        self.url = url
        self.icon = icon
        self.text = text
        self.margin = margin
        self.padding = padding

    def html_get(self, **kwargs):
        if type(self.text) in [str, NoneType]:
            self.text = Text(
                text=self.text,
                margin=Margin(top=8 if self.icon and self.text else 0),
                font=Font(
                    weight=700,
                    size=24,
                ),
            )

        if not self.margin:
            self.margin = Margin(horizontal=0)

        if not self.padding:
            self.padding = Padding(horizontal=12, vertical=24)

        text_html = self.text.html_get(**kwargs)
        icon_html = self.icon.html_get(height=24, **kwargs,) if self.icon else ''

        properties_css = properties_css_get(
            properties=[self.margin, self.padding],
            properties_additional='cursor: pointer;border: 4px solid {border_color};border-radius: var(--rounding);'
                                  'display: flex;width: fit-content;'
                                  'align-items: center;flex-direction: column;'.format(
                border_color=kwargs.get('colors').primary.color,
            ),
        )
        button_html = BUTTON_CARD_HTML.format(
            properties_css=properties_css,
            url=self.url,
            icon_html=icon_html,
            text_html=text_html,
        )
        return button_html
