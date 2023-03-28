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


class InputText:
    id: str
    value: str
    margin: Margin
    padding: Padding
    is_password: bool
    is_disabled: bool

    def __init__(
            self,
            id: str = None,
            value: str = None,
            margin: Margin = Margin(horizontal=8, ),
            padding: Padding = Padding(horizontal=12, vertical=12),
            is_password: bool = False,
            is_disabled: bool = False,
    ):
        self.id = id
        self.value = value
        self.margin = margin
        self.padding = padding
        self.is_password = is_password
        self.is_disabled = is_disabled

    def html_get(self, **kwargs):
        properties_css = properties_css_get(
            properties=[
                self.margin,
                self.padding,
            ],
            properties_additional='width: 100%;box-sizing: border-box;border: 2px solid {color_border};'
                                  'background-color : {color_background};color : {color_text};'
                                  'border-radius: var(--rounding);'.format(
                color_border=kwargs.get('colors').primary.color,
                color_background=kwargs.get('colors').background.color,
                color_text=kwargs.get('colors').text.color,
            ),
        )

        input_html = '<input {properties_css} type="{type}" name="{id}" value="{value}" {is_disabled}>'.format(
            properties_css=properties_css,
            type='password' if self.is_password else 'text',
            id=self.id,
            value=self.value if self.value else '',
            is_disabled='disabled' if self.is_disabled else '',
        )
        return input_html


class InputSelect:
    id: str
    options: list
    margin: Margin
    padding: Padding
    is_disabled: bool

    def __init__(
            self,
            id: str,
            options: list,
            margin: Margin = Margin(horizontal=8),
            padding: Padding = Padding(horizontal=8, vertical=12),
            is_disabled: bool = False,
    ):
        self.id = id
        self.options = options
        self.margin = margin
        self.padding = padding
        self.is_disabled = is_disabled

    def html_get(self, **kwargs):
        input_select_options = ''.join(['<option>{}</option>'.format(option) for option in self.options])

        properties_css = properties_css_get(
            properties=[
                self.margin,
                self.padding,
            ],
            properties_additional='-webkit-appearance: none;'
                                  'width: 100%;'
                                  'border: 2px solid {color_border};'
                                  'border-radius: {rounding}px;'
                                  'background: #fff;'
                                  'cursor: pointer;'
                                  'font-family: inherit;'
                                  'font-size: 16px;'.format(
                color_border=kwargs.get('colors').primary.color,
                rounding=kwargs.get('rounding'),
            ),
        )
        input_select_html = '<div class="select">' \
                            '<select name="{input_select_id}" required="required" {properties_css} {is_disabled}>' \
                            '{input_select_options}' \
                            '</select>' \
                            '</div>'.format(
            input_select_id=self.id,
            properties_css=properties_css,
            input_select_options=input_select_options,
            is_disabled='disabled' if self.is_disabled else '',
        )

        return input_select_html


class InputFile:
    id: str
    margin: Margin
    padding: Padding
    is_disabled: bool

    def __init__(
            self,
            id: str,
            margin: Margin = Margin(right=24, ),
            padding: Padding = Padding(horizontal=2, vertical=2),
            is_disabled: bool = False,
    ):
        self.id = id
        self.margin = margin
        self.padding = padding
        self.is_disabled = is_disabled

    def html_get(self, **kwargs):
        properties_css = properties_css_get(
            properties=[
                self.margin,
                self.padding,
            ],
            properties_additional='width: 100%;'
                                  'border: 2px solid {color_border};'
                                  'background: {color_background};'
                                  'border-radius: {rounding}px;'
                                  'color: {color_text};'
                                  'cursor: pointer;'.format(
                color_border=kwargs.get('colors').primary.color,
                color_background=kwargs.get('colors').background.color,
                color_text=kwargs.get('colors').text.color,
                rounding=kwargs.get('rounding'),
            ),
        )
        input_select_html = '<input {properties_css} type="file" name="{id}" {is_disabled}>'.format(
            properties_css=properties_css,
            id=self.id,
            is_disabled='disabled' if self.is_disabled else '',
        )

        return input_select_html


class InputButton:
    text: str
    margin: Margin
    padding: Padding
    is_disabled: bool

    def __init__(
            self,
            text: str,
            margin: Margin = Margin(horizontal=8),
            padding: Padding = Padding(horizontal=12, vertical=24),
            is_disabled: bool = False,
    ):
        self.text = text
        self.margin = margin
        self.padding = padding
        self.is_disabled = is_disabled

    def html_get(self, **kwargs):
        properties_css = properties_css_get(
            properties=[
                self.margin,
                self.padding,
            ],
            properties_additional='cursor: pointer;border: 2px solid {color_border};'
                                  'border-radius: var(--rounding);display: flex;'
                                  'width: fit-content;align-items: center; '
                                  'background-color: {color_background};'.format(
                color_border=kwargs.get('colors').primary.color,
                color_background=kwargs.get('colors').background.color,
            ),
        )
        input_select_html = '<input {properties_css} type="submit" value="{text}" {is_disabled}>'.format(
            properties_css=properties_css,
            text=self.text,
            is_disabled='disabled' if self.is_disabled else '',
        )

        return input_select_html
