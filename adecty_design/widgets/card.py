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


from adecty_design.functions import properties_css_get
from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Padding, Margin, Color
from adecty_design.properties.color import ColorType


class Card:
    widgets: list
    margin: Margin
    padding: Padding
    color_background: Color

    def __init__(
            self,
            widgets: list,
            margin: Margin = Margin(),
            padding: Padding = Padding(horizontal=12, vertical=12),
            color_background: Color = None,
    ):
        self.widgets = widgets
        self.margin = margin
        self.padding = padding
        self.color_background = color_background

    def html_get(self, **kwargs):
        if not self.color_background:
            self.color_background = Color(color=kwargs.get('colors').background.color)

        self.color_background.type = ColorType.background

        widgets_html = ''.join([widget.html_get(**kwargs) for widget in self.widgets])
        properties_css = properties_css_get(
            properties=[self.margin, self.padding, self.color_background],
            properties_additional='box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);border-radius: var(--rounding);',
            **kwargs,
        )

        card_html = MarkupsHtml.card.format(
            properties_css=properties_css,
            widgets_html=widgets_html,
        )
        return card_html
