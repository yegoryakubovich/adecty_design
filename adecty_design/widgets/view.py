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
from adecty_design.functions import widgets_html_get
from adecty_design.markups.markups import MarkupsHtml
from adecty_design.properties.margin import Margin
from adecty_design.properties.padding import Padding


class ViewType:
    vertical = 'vertical'
    horizontal = 'horizontal'


class View:
    widgets: list
    type: str
    margin: Margin
    padding: Padding

    def __init__(
            self,
            widgets: list,
            type: str = ViewType.vertical,
            margin: Margin = Margin(),
            padding: Padding = Padding(),
    ):
        self.widgets = widgets
        self.type = type
        self.margin = margin
        self.padding = padding

    def html_get(self, **kwargs):
        properties_css = properties_css_get(properties=[self.margin, self.padding])
        widgets_html = widgets_html_get(widgets=self.widgets, **kwargs)

        if self.type == ViewType.vertical:
            view_html = MarkupsHtml.view_vertical
            return view_html.format(
                properties_css=properties_css,
                widgets_html=widgets_html,
            )
        elif self.type == ViewType.horizontal:
            view_html = MarkupsHtml.view_horizontal
            return view_html.format(
                properties_css=properties_css,
                widgets_html=widgets_html,
            )
