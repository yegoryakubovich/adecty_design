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
    text = 'text'
    button = 'button'
    file = 'file'


class Input:
    input_type: str
    kwargs: dict

    def __init__(self, input_type: str, **kwargs):
        self.input_type = input_type
        self.kwargs = kwargs

    def html_get(self, config: Config):
        if self.input_type == InputTypes.text:
            styles = 'style="' \
                     'width: 100vh;' \
                     'margin: 8px 0;' \
                     'padding: 12px 18px;' \
                     'box-sizing: border-box;' \
                     'border: 2px solid {border_color};' \
                     'border-radius: var(--rounding);"'.format(border_color=config.colors.primary)

            input_html = '<input {styles} type="text" name="{name}">'.format(styles=styles, name=self.kwargs['name'])
        elif self.input_type == InputTypes.button:
            styles = 'style="' \
                     'font-family: {font_css};' \
                     'font-weight: 600;' \
                     'background-color: {background_color};' \
                     'color: {color};' \
                     'margin: 8px 0;' \
                     'padding: 12px 24px;' \
                     'cursor: pointer;' \
                     'border: 2px solid {border_color};' \
                     'border-radius: var(--rounding);"'.format(font_css=config.fonts.main.css,
                                                               background_color=config.colors.background,
                                                               color=config.colors.primary,
                                                               border_color=config.colors.primary)

            input_html = '<input {styles} type="submit" value="{text}">'.format(
                styles=styles, text=self.kwargs['text']
            )
        elif self.input_type == InputTypes.file:
            input_html = '<input type="file" name="file">'
        else:
            return ''
        return input_html
