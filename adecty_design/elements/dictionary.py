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
from adecty_design.elements.text import Text


class Dictionary:
    keys: list
    values: list

    def __init__(self, keys: list, values: list):
        self.keys = keys
        self.values = values

    def html_get(self, config: Config):
        dictionary_html = '<table class="dictionary">{rows_html}</table>'

        rows_html = ''
        for i in range(len(self.keys)):
            key = self.keys[i]
            value = self.values[i]

            key_html = Text(text=key).html_get(config=config) \
                if type(key) is str else key.html_get(config=config)
            value_html = Text(text=value).html_get(config=config) \
                if type(value) is str else value.html_get(config=config)

            rows_html += '<tr><td>{key_html}</td><td>{value_html}</td></tr>'.format(
                key_html=key_html,
                value_html=value_html
            )

        return dictionary_html.format(rows_html=rows_html)
