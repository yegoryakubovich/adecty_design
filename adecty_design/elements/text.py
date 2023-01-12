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


from adecty_design.elements.config import Config
from adecty_design.elements.fonts import Font
from adecty_design.markups.markups import MarkupsHtml


class TextType:
    vertical = 'VERTICAL'
    horizontal = 'HORIZONTAL'


class Text:
    config: Config
    width: int
    height: int
    font: Font
    color: str
    text: str
    font_size: int
    font_weight: int

    def __init__(self, text: str, font: Font = None, color: str = None,
                 width: int = 100, height: int = 100,
                 font_size: int = 12, font_weight: int = 600):
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.text = text
        self.font_size = font_size
        self.font_weight = font_weight

    def html_get(self, config: Config):
        self.config = config

        font = self.config.fonts.main if not self.font else self.font
        color = config.colors.text if not self.color else self.color

        styles = 'style="' \
                 'font-family: {font_css};' \
                 'font-size: {font_size}px;' \
                 'font-weight: {font_weight}px;' \
                 'color: {color};"'.format(font_css=font.css,
                                           font_size=self.font_size,
                                           font_weight=self.font_weight,
                                           color=color)

        text_html = MarkupsHtml.text.format(text=self.text, styles=styles)
        return text_html
