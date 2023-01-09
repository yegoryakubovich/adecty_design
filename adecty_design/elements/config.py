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


from adecty_design.elements.colors import Colors
from adecty_design.templates import get_css


class Config:
    name: str
    logo: str
    colors: Colors
    rounding = int
    fonts: list

    def __init__(self, name: str, logo: str, colors: Colors, rounding: int, fonts: list):
        self.name = name
        self.logo = logo
        self.colors = colors
        self.rounding = rounding
        self.fonts = fonts

    def get_html(self):
        fonts_html = ''
        for font in self.fonts:
            fonts_html += font.html

        styles_css = ''.join([get_css(name) for name in ['style', 'table']])
        for font in self.fonts:
            styles_css += font.css

        variables = \
            '--background: {color_background};' \
            '--main: {color_main};' \
            '--secondary: {color_secondary};' \
            '--rounding: {rounding}px;'.format(color_background=self.colors.background,
                                               color_main=self.colors.main,
                                               color_secondary=self.colors.secondary,
                                               rounding=self.rounding)
        variables_css = ':root {' + variables + '}'
        styles_html = '<style>{variables_css}{styles_css}</style>'.format(
            variables_css=variables_css, styles_css=styles_css,
        )

        config_html = '{fonts_html}{styles_html}'.format(
            fonts_html=fonts_html, styles_html=styles_html
        )
        return config_html
