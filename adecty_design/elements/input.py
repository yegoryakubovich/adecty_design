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


class InputTypes:
    text = 'TEXT'


class Input:
    input_type: str
    name: str

    def __init__(self, input_type: str, name):
        self.input_type = input_type
        self.name = name

    def get_html(self, config: Config):
        styles = 'style="' \
                 'width: 100vh;' \
                 'margin: 8px 0;' \
                 'padding: 12px 18px;' \
                 'box-sizing: border-box;' \
                 'border: 2px solid {border_color};' \
                 'border-radius: var(--rounding);"'.format(border_color=config.colors.main)

        input_html = '<input {styles} type="text" name="{name}">'.format(styles=styles, name=self.name)
        return input_html
