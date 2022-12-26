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
from adecty_design.elements.font import Font
from adecty_design.templates.get_element_html import get_element_html


class TextType:
    vertical = 'VERTICAL'
    horizontal = 'HORIZONTAL'


class Text:
    config: Config
    width: int
    height: int
    font: str
    color: str
    text: str
    font_size: int
    font_wight: int

    def __init__(self, font: str, color: str, text: str,
                 width: int = 100, height: int = 100,
                 font_size: int = 12, font_wight: int = 600):
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.text = text
        self.font_size = font_size
        self.font_wight = font_wight

    def generate_html(self, config: Config):
        self.config = config

        font = next((font for font in config.fonts if font.name == self.font), config.fonts[0])
        font: Font

        styles = 'style="' \
                 'font-family: {font_css};' \
                 'font-size: {font_size}px;' \
                 'color: {color};"'.format(font_css=font.html_name, font_size=self.font_size, color=self.color)

        text_html = get_element_html('text').format(text=self.text, styles=styles)
        return text_html
