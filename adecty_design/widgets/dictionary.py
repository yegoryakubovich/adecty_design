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
from adecty_design.properties import Margin, Padding
from adecty_design.widgets.text import Text


class Dictionary:
    keys: list
    values: list
    margin: Margin
    padding: Padding

    def __init__(
            self,
            keys: list,
            values: list,
            margin: Margin = Margin(),
            padding: Padding = Padding(),
    ):
        self.keys = keys
        self.values = values
        self.margin = margin
        self.padding = padding

    def html_get(self, **kwargs):
        properties_css = properties_css_get(properties=[self.margin, self.padding])
        dictionary_html = '<table class="dictionary" {properties_css}>{rows_html}</table>'

        rows_html = ''
        for i in range(len(self.keys)):
            key = self.keys[i]
            value = self.values[i]

            key_html = Text(text=key).html_get(**kwargs) \
                if type(key) is str else key.css_get(**kwargs)
            value_html = Text(text=value).html_get(**kwargs) \
                if type(value) is str else value.css_get(**kwargs)

            rows_html += '<tr>' \
                         '<td class="dictionary__key">{key_html}</td><td class="dictionary__value">{value_html}</td>' \
                         '</tr>'.format(
                key_html=key_html,
                value_html=value_html,
            )

        return dictionary_html.format(rows_html=rows_html, properties_css=properties_css)
