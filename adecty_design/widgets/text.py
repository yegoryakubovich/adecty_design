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


from adecty_design.functions import properties_css_get
from adecty_design.properties.font import Font
from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Margin, Padding


class Text:
    font: Font
    color: str
    text: str
    font_size: int
    font_weight: int
    margin: Margin
    padding: Padding

    def __init__(
            self,
            text: str,
            font: Font = Font(),
            margin: Margin = Margin(),
            padding: Padding = Padding(),
    ):
        self.text = text
        self.font = font
        self.margin = margin
        self.padding = padding

    def html_get(self, **kwargs):
        properties_css = properties_css_get(
            properties=[self.font, self.margin, self.padding],
            properties_additional='align-self: center;', **kwargs,
        )
        text_html = MarkupsHtml.text.format(
            properties_css=properties_css,
            text=self.text if self.text else '',
        )

        return text_html
