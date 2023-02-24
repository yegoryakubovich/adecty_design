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


class ViewType:
    vertical = 'vertical'
    horizontal = 'horizontal'


class View:
    widgets: list
    type: str

    def __init__(self, widgets: list, type: str = ViewType.vertical):
        self.widgets = widgets
        self.type = type

    def html_get(self, **kwargs):
        view_html = MarkupsHtml.view_vertical
        if self.type == ViewType.horizontal:
            view_html = MarkupsHtml.view_horizontal

        widgets_html = ''.join([widget.html_get(**kwargs) for widget in self.widgets])

        return view_html.format(
            widgets_html=widgets_html,
        )
