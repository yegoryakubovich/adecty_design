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


from adecty_design.font import Font
from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Properties


class TextType:
    vertical = 'VERTICAL'
    horizontal = 'HORIZONTAL'


class Text:
    width: int
    height: int
    font: Font
    color: str
    text: str
    font_size: int
    font_weight: int
    properties: Properties

    def __init__(self, text: str, font: Font = None, color: str = None,
                 width: int = 100, height: int = 100,
                 font_size: int = 12, font_weight: int = 600,
                 properties: Properties = Properties()):
        self.width = width
        self.height = height
        self.font = font
        self.color = color
        self.text = text
        self.font_size = font_size
        self.font_weight = font_weight
        self.properties = properties

    def html_get(self, **kwargs):
        font = kwargs.get('font') if not self.font else self.font
        color = kwargs.get('colors').text if not self.color else self.color

        styles = 'style="' \
                 'margin: {margin};' \
                 'font-family: {font_css};' \
                 'font-size: {font_size}px;' \
                 'font-weight: {font_weight};' \
                 'color: {color};"'.format(
            margin=self.properties.margin.html_get(),
            font_css=font.css,
            font_size=self.font_size,
            font_weight=self.font_weight,
            color=color,
        )

        text_html = MarkupsHtml.text.format(text=self.text, styles=styles)
        return text_html
