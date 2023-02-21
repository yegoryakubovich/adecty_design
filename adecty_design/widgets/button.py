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


class Button:
    url: str
    value: str

    def __init__(self, url: str, value: str):
        self.url = url
        self.value = value

    def html_get(self, **kwargs):
        styles = 'style="' \
                 'font-family: {font_css};' \
                 'font-weight: 600;' \
                 'background-color: {background_color};' \
                 'color: {color};' \
                 'margin: 8px 0;' \
                 'padding: 12px 24px;' \
                 'cursor: pointer;' \
                 'border: 2px solid {border_color};' \
                 'border-radius: var(--rounding);"'.format(font_css=kwargs.get('fonts').main.css,
                                                           background_color=kwargs.get('colors').background,
                                                           color=kwargs.get('colors').primary,
                                                           border_color=kwargs.get('colors').primary)
        button_html = '<form action="{url}"><input {styles} type="submit" value="{value}" /></form>'

        return button_html.format(url=self.url, value=self.value, styles=styles)
