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


from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties import Properties, Margin, Padding


class Card:
    properties: Properties
    widgets: list

    def __init__(self, widgets: list, properties: Properties = Properties(padding=Padding(horizontal=12, vertical=12))):
        self.properties = properties
        self.widgets = widgets

    def html_get(self, **kwargs):
        widgets_html = ''.join([widget.html_get(**kwargs) for widget in self.widgets])
        properties = self.properties.html_get()

        card_html = MarkupsHtml.card.format(
            properties=properties,
            widgets_html=widgets_html,
        )
        return card_html
